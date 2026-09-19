#!/usr/bin/env python3
"""Read-only watcher for one critical GitHub Actions run."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

API = "https://api.github.com"
UA = "luminous-dynamics-critical-run-watch/1"


def parse_time(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.timezone.utc)


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


def count_runs(client: Client, repo: str, status: str, created: str | None = None) -> int:
    params: dict[str, Any] = {"status": status, "per_page": 1}
    if created:
        params["created"] = created
    payload = client.get(f"/repos/{repo}/actions/runs", params)
    count = payload.get("total_count") if isinstance(payload, dict) else None
    if not isinstance(count, int) or count < 0:
        raise RuntimeError(f"invalid total_count for {repo} status={status}")
    return count


def classify(run: dict[str, Any], jobs: list[dict[str, Any]], age_seconds: int) -> str:
    status = run.get("status")
    conclusion = run.get("conclusion")
    if status == "completed":
        return f"TERMINAL_{str(conclusion).upper()}"
    if status == "in_progress":
        return "RUNNING"
    if status == "queued":
        nonterminal = [job for job in jobs if job.get("status") != "completed"]
        if nonterminal:
            return "REAL_QUEUED_JOB"
        if not jobs and age_seconds >= 1800:
            return "GHOST_PREQUEUE_SUSPECT"
        return "QUEUED_WITHOUT_VISIBLE_JOB_YET"
    return f"STATUS_{str(status).upper()}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="owner/repository")
    parser.add_argument("--run-id", required=True, type=int)
    parser.add_argument("--expected-head")
    parser.add_argument("--expected-name")
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    parser.add_argument("--json-output", type=pathlib.Path)
    args = parser.parse_args()

    client = Client(os.environ.get(args.token_env) or None)
    run = client.get(f"/repos/{args.repo}/actions/runs/{args.run_id}")
    if not isinstance(run, dict) or run.get("id") != args.run_id:
        raise SystemExit("run identity mismatch")
    if args.expected_head and run.get("head_sha") != args.expected_head:
        raise SystemExit(f"head mismatch: {run.get('head_sha')} != {args.expected_head}")
    if args.expected_name and run.get("name") != args.expected_name:
        raise SystemExit(f"workflow name mismatch: {run.get('name')} != {args.expected_name}")

    created = parse_time(str(run["created_at"]))
    observed = dt.datetime.now(dt.timezone.utc)
    age_seconds = max(0, int((observed - created).total_seconds()))

    jobs_payload = client.get(f"/repos/{args.repo}/actions/runs/{args.run_id}/jobs", {"per_page": 100})
    if not isinstance(jobs_payload, dict):
        raise SystemExit("invalid jobs response")
    total_jobs = jobs_payload.get("total_count")
    jobs = jobs_payload.get("jobs")
    if not isinstance(total_jobs, int) or not isinstance(jobs, list):
        raise SystemExit("invalid jobs response shape")
    if total_jobs > 100:
        raise SystemExit("job census exceeds one page; refuse incomplete classification")

    queue_total = count_runs(client, args.repo, "queued")
    active_total = count_runs(client, args.repo, "in_progress")
    before = created - dt.timedelta(seconds=1)
    created_range = f"2008-01-01T00:00:00Z..{before.strftime('%Y-%m-%dT%H:%M:%SZ')}"
    older_queued = count_runs(client, args.repo, "queued", created_range)

    report = {
        "schema": "luminous.actions.critical-run-watch.v1",
        "authority": "ObservationOnly",
        "observed_at_utc": observed.isoformat(),
        "repository": args.repo,
        "run_id": args.run_id,
        "workflow_name": run.get("name"),
        "head_sha": run.get("head_sha"),
        "created_at_utc": created.isoformat(),
        "run_age_seconds": age_seconds,
        "status": run.get("status"),
        "conclusion": run.get("conclusion"),
        "classification": classify(run, jobs, age_seconds),
        "jobs": [
            {"id": job.get("id"), "name": job.get("name"), "status": job.get("status"), "conclusion": job.get("conclusion")}
            for job in jobs
        ],
        "repository_scheduler_snapshot": {
            "queued_total": queue_total,
            "in_progress_total": active_total,
            "queued_created_before_target": older_queued,
            "creation_order_position_lower_bound": older_queued + 1 if run.get("status") == "queued" else None,
        },
        "interpretation": {
            "creation_order_position_is_not_scheduler_priority": True,
            "real_queued_job_means": "the target run is queued and has at least one visible nonterminal job",
            "ghost_prequeue_suspect_means": "the target run is queued, stale, and has no visible jobs",
            "does_not_prove": [
                "GitHub schedules strictly FIFO",
                "the target will run after exactly queued_created_before_target other runs",
                "runner capacity will remain continuously available",
            ],
        },
    }

    print(json.dumps(report, indent=2, sort_keys=True))
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
