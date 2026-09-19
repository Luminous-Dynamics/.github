#!/usr/bin/env python3
"""Safely prune provably obsolete queued GitHub Actions runs.

Default mode is read-only. Mutation requires --apply. A run is eligible only if:
- status is still queued;
- event is pull_request;
- it is older than --min-age-hours;
- it is associated with exactly one PR;
- that PR is currently closed;
- its run id is not protected.

Every candidate is re-fetched immediately before cancellation. This tool is
operational queue hygiene only; it must never be used to prioritize by rewriting
or cancelling active scientific/evidence subjects.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

API = "https://api.github.com"
DEFAULT_PROTECTED_RUN_IDS = {
    35349750595,  # REL-005A ComparisonOnly V3 R2
    35439414230,  # REL-005A Qualification Pipeline V3
}


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_time(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def request_json(path: str, token: str | None, method: str = "GET") -> Any:
    req = urllib.request.Request(API + path, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "luminous-actions-safe-queue-prune/1")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    data = b"" if method != "GET" else None
    try:
        with urllib.request.urlopen(req, data=data, timeout=30) as response:
            raw = response.read()
            return json.loads(raw) if raw else {"http_status": response.status}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {method} {path}: HTTP {exc.code}: {body[:500]}") from exc


def list_queued_runs(repo: str, token: str | None, max_pages: int) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    owner, name = repo.split("/", 1)
    for page in range(1, max_pages + 1):
        q = urllib.parse.urlencode({"status": "queued", "per_page": 100, "page": page})
        payload = request_json(f"/repos/{owner}/{name}/actions/runs?{q}", token)
        runs = payload.get("workflow_runs", [])
        out.extend(runs)
        if len(runs) < 100:
            break
    return out


def get_pr(repo: str, pr_number: int, token: str | None) -> dict[str, Any]:
    owner, name = repo.split("/", 1)
    return request_json(f"/repos/{owner}/{name}/pulls/{pr_number}", token)


def get_run(repo: str, run_id: int, token: str | None) -> dict[str, Any]:
    owner, name = repo.split("/", 1)
    return request_json(f"/repos/{owner}/{name}/actions/runs/{run_id}", token)


def cancel_run(repo: str, run_id: int, token: str) -> Any:
    owner, name = repo.split("/", 1)
    return request_json(f"/repos/{owner}/{name}/actions/runs/{run_id}/cancel", token, method="POST")


def candidate(run: dict[str, Any], *, now: dt.datetime, min_age: dt.timedelta, protected: set[int]) -> tuple[bool, str, int | None]:
    run_id = int(run["id"])
    if run_id in protected:
        return False, "protected_run", None
    if run.get("status") != "queued":
        return False, "not_queued", None
    if run.get("event") != "pull_request":
        return False, "not_pull_request", None
    created = parse_time(run["created_at"])
    if now - created < min_age:
        return False, "too_new", None
    prs = run.get("pull_requests") or []
    if len(prs) != 1:
        return False, f"pr_census_{len(prs)}", None
    return True, "needs_pr_check", int(prs[0]["number"])


def revalidate(repo: str, run_id: int, pr_number: int, token: str | None, *, min_age: dt.timedelta, protected: set[int]) -> tuple[bool, str, dict[str, Any], dict[str, Any]]:
    run = get_run(repo, run_id, token)
    pr = get_pr(repo, pr_number, token)
    ok, reason, pr2 = candidate(run, now=utcnow(), min_age=min_age, protected=protected)
    if not ok:
        return False, reason, run, pr
    if pr2 != pr_number:
        return False, "pr_identity_changed", run, pr
    if pr.get("state") != "closed":
        return False, "pr_not_closed", run, pr
    return True, "eligible_closed_pr", run, pr


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="Luminous-Dynamics/symthaea")
    parser.add_argument("--min-age-hours", type=float, default=12.0)
    parser.add_argument("--protect-run-id", action="append", type=int, default=[])
    parser.add_argument("--max-pages", type=int, default=20)
    parser.add_argument("--max-cancels", type=int, default=25)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--json-output")
    args = parser.parse_args()

    if "/" not in args.repo:
        raise SystemExit("--repo must be owner/name")
    if args.min_age_hours < 1:
        raise SystemExit("--min-age-hours must be >= 1")
    if args.max_cancels < 1:
        raise SystemExit("--max-cancels must be >= 1")

    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if args.apply and not token:
        raise SystemExit("--apply requires GITHUB_TOKEN or GH_TOKEN")

    protected = DEFAULT_PROTECTED_RUN_IDS | set(args.protect_run_id)
    min_age = dt.timedelta(hours=args.min_age_hours)
    now = utcnow()
    runs = list_queued_runs(args.repo, token, args.max_pages)

    report: dict[str, Any] = {
        "schema": "luminous.actions.safe-queue-prune.v1",
        "authority": "OperationalQueueHygieneOnly",
        "repo": args.repo,
        "mode": "apply" if args.apply else "dry-run",
        "observed_at": now.isoformat(),
        "min_age_hours": args.min_age_hours,
        "protected_run_ids": sorted(protected),
        "queued_runs_scanned": len(runs),
        "eligible": [],
        "skipped": [],
        "cancelled": [],
        "errors": [],
    }

    pr_cache: dict[int, dict[str, Any]] = {}
    for run in sorted(runs, key=lambda x: x.get("created_at", "")):
        ok, reason, pr_number = candidate(run, now=now, min_age=min_age, protected=protected)
        if not ok:
            report["skipped"].append({"run_id": run.get("id"), "reason": reason})
            continue
        assert pr_number is not None
        try:
            pr = pr_cache.get(pr_number)
            if pr is None:
                pr = get_pr(args.repo, pr_number, token)
                pr_cache[pr_number] = pr
            if pr.get("state") != "closed":
                report["skipped"].append({"run_id": run["id"], "pr": pr_number, "reason": "pr_not_closed"})
                continue
            entry = {
                "run_id": int(run["id"]),
                "workflow": run.get("name"),
                "created_at": run.get("created_at"),
                "head_sha": run.get("head_sha"),
                "pr": pr_number,
                "pr_state": pr.get("state"),
                "pr_merged": bool(pr.get("merged_at")),
            }
            report["eligible"].append(entry)
        except Exception as exc:  # operational report should continue
            report["errors"].append({"run_id": run.get("id"), "stage": "candidate_check", "error": str(exc)})

    if args.apply:
        for entry in report["eligible"][: args.max_cancels]:
            run_id = int(entry["run_id"])
            pr_number = int(entry["pr"])
            try:
                ok, reason, fresh_run, fresh_pr = revalidate(
                    args.repo, run_id, pr_number, token,
                    min_age=min_age, protected=protected,
                )
                if not ok:
                    report["skipped"].append({"run_id": run_id, "pr": pr_number, "reason": f"revalidation:{reason}"})
                    continue
                cancel_run(args.repo, run_id, token)
                report["cancelled"].append({
                    "run_id": run_id,
                    "pr": pr_number,
                    "head_sha": fresh_run.get("head_sha"),
                    "pr_state": fresh_pr.get("state"),
                })
                time.sleep(0.15)
            except Exception as exc:
                report["errors"].append({"run_id": run_id, "stage": "cancel", "error": str(exc)})

    report["eligible_count"] = len(report["eligible"])
    report["cancelled_count"] = len(report["cancelled"])
    report["claims"] = {
        "scientific_result_changed": False,
        "evidence_subject_rewritten": False,
        "queue_priority_guaranteed": False,
    }

    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.json_output:
        with open(args.json_output, "w", encoding="utf-8") as handle:
            handle.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
