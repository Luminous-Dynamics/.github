#!/usr/bin/env python3
"""Read-only owner-wide GitHub Actions allocation auditor with stale-queue evidence."""
from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import datetime as dt
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

API = "https://api.github.com"
QUEUE = ("queued", "waiting", "pending", "requested")
UA = "luminous-dynamics-actions-runner-audit/2"


def parse_time(value: Any) -> dt.datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed.astimezone(dt.timezone.utc)


@dataclasses.dataclass(frozen=True)
class RepoState:
    name: str
    private: bool
    counts: dict[str, int]
    newest_waiting_run_id: int | None
    newest_waiting_workflow: str | None
    newest_waiting_created_at_utc: str | None
    newest_waiting_age_seconds: int | None
    errors: tuple[str, ...] = ()

    @property
    def waiting_total(self) -> int:
        return sum(self.counts.get(status, 0) for status in QUEUE)

    def as_dict(self) -> dict[str, Any]:
        return {
            "repository": self.name,
            "private": self.private,
            **self.counts,
            "waiting_total": self.waiting_total,
            "newest_waiting_run_id": self.newest_waiting_run_id,
            "newest_waiting_workflow": self.newest_waiting_workflow,
            "newest_waiting_created_at_utc": self.newest_waiting_created_at_utc,
            "newest_waiting_age_seconds": self.newest_waiting_age_seconds,
            "errors": list(self.errors),
        }


class Client:
    def __init__(self, token: str | None) -> None:
        self.token = token

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        query = urllib.parse.urlencode(params or {})
        url = f"{API}{path}" + (f"?{query}" if query else "")
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": UA,
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")[:500]
            raise RuntimeError(f"GitHub HTTP {exc.code} for {url}: {body}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"GitHub request failed for {url}: {exc}") from exc

    def repos(self, org: str) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        page = 1
        while True:
            payload = self.get(f"/orgs/{org}/repos", {"type": "all", "sort": "pushed", "per_page": 100, "page": page})
            if not isinstance(payload, list):
                raise RuntimeError("expected repository list")
            out.extend(payload)
            if len(payload) < 100:
                return out
            page += 1


def inspect_repo(client: Client, repo: dict[str, Any], observed: dt.datetime) -> RepoState:
    full = str(repo["full_name"])
    counts = {status: 0 for status in (*QUEUE, "in_progress")}
    samples: list[tuple[dt.datetime, int, str]] = []
    errors: list[str] = []
    for status in counts:
        try:
            payload = client.get(f"/repos/{full}/actions/runs", {"status": status, "per_page": 1})
            count = payload.get("total_count") if isinstance(payload, dict) else None
            runs = payload.get("workflow_runs") if isinstance(payload, dict) else None
            if not isinstance(count, int) or count < 0:
                raise RuntimeError("invalid total_count")
            counts[status] = count
            if status in QUEUE and count:
                if not isinstance(runs, list) or len(runs) != 1:
                    raise RuntimeError("missing newest waiting run")
                run = runs[0]
                created = parse_time(run.get("created_at"))
                run_id = run.get("id")
                name = run.get("name")
                if created is None or not isinstance(run_id, int) or not isinstance(name, str):
                    raise RuntimeError("invalid newest waiting run identity")
                samples.append((created, run_id, name))
        except Exception as exc:
            errors.append(f"{status}: {exc}")
    if samples:
        created, run_id, workflow = max(samples, key=lambda item: item[0])
        age = max(0, int((observed - created).total_seconds()))
        created_text = created.isoformat()
    else:
        run_id = None
        workflow = None
        age = None
        created_text = None
    return RepoState(
        name=full,
        private=bool(repo.get("private", False)),
        counts=counts,
        newest_waiting_run_id=run_id,
        newest_waiting_workflow=workflow,
        newest_waiting_created_at_utc=created_text,
        newest_waiting_age_seconds=age,
        errors=tuple(errors),
    )


def classify(states: list[RepoState], stale_seconds: int) -> str:
    good = [state for state in states if not state.errors]
    waiting = [state for state in good if state.waiting_total > 0]
    stale = [state for state in waiting if state.newest_waiting_age_seconds is not None and state.newest_waiting_age_seconds >= stale_seconds]
    active = sum(state.counts["in_progress"] for state in good)
    if len(waiting) >= 2 and active == 0:
        return "ORG_HOSTED_RUNNER_ALLOCATION_SUSPECT" if len(stale) >= 2 else "OWNER_WIDE_QUEUE_OBSERVED_NOT_YET_STALE"
    if waiting and active > 0:
        return "ACTIVE_DRAINING_OR_CONCURRENCY_LIMITED"
    if len(waiting) == 1 and active == 0:
        return "REPOSITORY_LOCAL_BACKLOG_OR_LABEL_BLOCK"
    if not waiting and active == 0:
        return "IDLE"
    return "ACTIVE_WITHOUT_REPORTED_QUEUE"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--org", default="Luminous-Dynamics")
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--suspect-min-age-minutes", type=int, default=15)
    parser.add_argument("--include-archived", action="store_true")
    parser.add_argument("--json-output", type=pathlib.Path)
    parser.add_argument("--fail-on-suspect", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.workers <= 32:
        raise SystemExit("--workers must be between 1 and 32")
    if not 1 <= args.suspect_min_age_minutes <= 1440:
        raise SystemExit("--suspect-min-age-minutes must be between 1 and 1440")

    observed = dt.datetime.now(dt.timezone.utc)
    client = Client(os.environ.get(args.token_env) or None)
    repos = client.repos(args.org)
    if not args.include_archived:
        repos = [repo for repo in repos if not repo.get("archived", False)]

    states: list[RepoState] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(inspect_repo, client, repo, observed) for repo in repos]
        for future in concurrent.futures.as_completed(futures):
            states.append(future.result())

    good = [state for state in states if not state.errors]
    stale_seconds = args.suspect_min_age_minutes * 60
    report = {
        "schema": "luminous.actions.runner-allocation-audit.v2",
        "authority": "ObservationOnly",
        "organization": args.org,
        "observed_at_utc": observed.isoformat(),
        "suspect_min_age_seconds": stale_seconds,
        "classification": classify(states, stale_seconds),
        "totals": {
            "repositories_inspected": len(states),
            "repositories_with_errors": sum(bool(state.errors) for state in states),
            "repositories_with_waiting_work": sum(state.waiting_total > 0 for state in good),
            "repositories_with_stale_waiting_work": sum(state.waiting_total > 0 and state.newest_waiting_age_seconds is not None and state.newest_waiting_age_seconds >= stale_seconds for state in good),
            "waiting_total": sum(state.waiting_total for state in good),
            "in_progress": sum(state.counts["in_progress"] for state in good),
        },
        "repositories": [state.as_dict() for state in sorted(states, key=lambda state: (-state.waiting_total, state.name.lower()))],
        "does_not_prove": [
            "the root cause is GitHub rather than organization or enterprise policy",
            "standard GitHub-hosted runners are enabled",
            "billing, spending, concurrency, or runner-group policy is correctly configured",
        ],
    }
    print(f"classification: {report['classification']}")
    print(f"waiting={report['totals']['waiting_total']} in_progress={report['totals']['in_progress']}")
    shown = 0
    for repo in report["repositories"]:
        if repo["waiting_total"] <= 0:
            continue
        print(f"{repo['repository']}: waiting={repo['waiting_total']} in_progress={repo['in_progress']} newest_waiting_age_seconds={repo['newest_waiting_age_seconds']}")
        shown += 1
        if shown >= args.top:
            break
    if report["totals"]["repositories_with_errors"]:
        print("warning: one or more repositories had API errors", file=sys.stderr)
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    if args.fail_on_suspect and report["classification"] == "ORG_HOSTED_RUNNER_ALLOCATION_SUSPECT":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
