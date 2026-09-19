#!/usr/bin/env python3
"""Two-phase cleanup of provably obsolete queued GitHub Actions runs.

Default mode is read-only and emits a content-addressed prune plan. Mutation
requires --apply plus the reviewed plan and its expected SHA-256. A run is
eligible only when it is still queued, is a pull_request run, is old enough,
has exactly one associated PR, that PR is closed, and the run is not protected.

Every candidate is re-fetched immediately before cancellation. This tool is
OperationalQueueHygieneOnly and must not be used to rewrite or cancel active
scientific/evidence subjects merely to seek scheduling priority.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

API = "https://api.github.com"
PLAN_SCHEMA = "luminous.actions.safe-queue-prune-plan.v2"
APPLY_SCHEMA = "luminous.actions.safe-queue-prune-apply-receipt.v2"
AUTHORITY = "OperationalQueueHygieneOnly"
DEFAULT_PROTECTED_RUN_IDS = {
    35349750595,  # REL-005A ComparisonOnly V3 R2
    35439414230,  # REL-005A Qualification Pipeline V3
}


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_time(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()


def request_json(path: str, token: str | None, method: str = "GET") -> Any:
    req = urllib.request.Request(API + path, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "luminous-actions-safe-queue-prune/2")
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
    owner, name = repo.split("/", 1)
    out: list[dict[str, Any]] = []
    for page in range(1, max_pages + 1):
        query = urllib.parse.urlencode({"status": "queued", "per_page": 100, "page": page})
        payload = request_json(f"/repos/{owner}/{name}/actions/runs?{query}", token)
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
    if now - parse_time(run["created_at"]) < min_age:
        return False, "too_new", None
    prs = run.get("pull_requests") or []
    if len(prs) != 1:
        return False, f"pr_census_{len(prs)}", None
    return True, "needs_pr_check", int(prs[0]["number"])


def revalidate(repo: str, run_id: int, pr_number: int, token: str, *, min_age: dt.timedelta, protected: set[int]) -> tuple[bool, str, dict[str, Any], dict[str, Any]]:
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


def immutable_plan_surface(report: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": report["schema"],
        "authority": report["authority"],
        "repo": report["repo"],
        "min_age_hours": report["min_age_hours"],
        "protected_run_ids": report["protected_run_ids"],
        "eligible": report["eligible"],
        "claims": report["claims"],
    }


def plan_sha256(report: dict[str, Any]) -> str:
    return hashlib.sha256(canonical(immutable_plan_surface(report))).hexdigest()


def build_plan(args: argparse.Namespace, token: str | None) -> dict[str, Any]:
    protected = DEFAULT_PROTECTED_RUN_IDS | set(args.protect_run_id)
    min_age = dt.timedelta(hours=args.min_age_hours)
    now = utcnow()
    runs = list_queued_runs(args.repo, token, args.max_pages)
    report: dict[str, Any] = {
        "schema": PLAN_SCHEMA,
        "authority": AUTHORITY,
        "repo": args.repo,
        "mode": "plan",
        "observed_at": now.isoformat(),
        "min_age_hours": args.min_age_hours,
        "protected_run_ids": sorted(protected),
        "queued_runs_scanned": len(runs),
        "eligible": [],
        "skipped": [],
        "errors": [],
        "claims": {
            "scientific_result_changed": False,
            "evidence_subject_rewritten": False,
            "queue_priority_guaranteed": False,
        },
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
            report["eligible"].append({
                "run_id": int(run["id"]),
                "workflow": run.get("name"),
                "workflow_path": run.get("path"),
                "created_at": run.get("created_at"),
                "head_sha": run.get("head_sha"),
                "pr": pr_number,
                "pr_state": pr.get("state"),
                "pr_merged": bool(pr.get("merged_at")),
            })
        except Exception as exc:
            report["errors"].append({"run_id": run.get("id"), "stage": "candidate_check", "error": str(exc)})
    report["eligible_count"] = len(report["eligible"])
    report["plan_sha256"] = plan_sha256(report)
    return report


def load_plan(path: pathlib.Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit("--plan must contain one JSON object")
    if value.get("schema") != PLAN_SCHEMA or value.get("authority") != AUTHORITY:
        raise SystemExit("--plan schema/authority mismatch")
    return value


def apply_plan(args: argparse.Namespace, token: str, plan: dict[str, Any]) -> dict[str, Any]:
    actual_sha = plan_sha256(plan)
    if actual_sha != args.expect_plan_sha256:
        raise SystemExit(f"plan SHA-256 mismatch: expected {args.expect_plan_sha256}, recomputed {actual_sha}")
    if plan.get("plan_sha256") != actual_sha:
        raise SystemExit("plan embedded plan_sha256 is missing or inconsistent")
    if plan.get("repo") != args.repo:
        raise SystemExit("--repo does not match plan repo")
    if float(plan.get("min_age_hours")) != args.min_age_hours:
        raise SystemExit("--min-age-hours does not match reviewed plan")
    protected = DEFAULT_PROTECTED_RUN_IDS | set(args.protect_run_id)
    if sorted(protected) != plan.get("protected_run_ids"):
        raise SystemExit("protected run set does not match reviewed plan")

    min_age = dt.timedelta(hours=args.min_age_hours)
    receipt: dict[str, Any] = {
        "schema": APPLY_SCHEMA,
        "authority": AUTHORITY,
        "repo": args.repo,
        "mode": "apply",
        "source_plan_sha256": actual_sha,
        "source_plan_observed_at": plan.get("observed_at"),
        "started_at": utcnow().isoformat(),
        "requested_max_cancels": args.max_cancels,
        "cancelled": [],
        "skipped_after_revalidation": [],
        "errors": [],
        "claims": {
            "scientific_result_changed": False,
            "evidence_subject_rewritten": False,
            "queue_priority_guaranteed": False,
        },
    }

    for entry in list(plan.get("eligible") or [])[: args.max_cancels]:
        run_id = int(entry["run_id"])
        pr_number = int(entry["pr"])
        if run_id in protected:
            receipt["skipped_after_revalidation"].append({"run_id": run_id, "reason": "protected_run"})
            continue
        try:
            ok, reason, fresh_run, fresh_pr = revalidate(
                args.repo, run_id, pr_number, token,
                min_age=min_age, protected=protected,
            )
            if not ok:
                receipt["skipped_after_revalidation"].append({"run_id": run_id, "pr": pr_number, "reason": reason})
                continue
            if fresh_run.get("head_sha") != entry.get("head_sha"):
                receipt["skipped_after_revalidation"].append({"run_id": run_id, "pr": pr_number, "reason": "head_sha_changed"})
                continue
            if fresh_run.get("path") != entry.get("workflow_path"):
                receipt["skipped_after_revalidation"].append({"run_id": run_id, "pr": pr_number, "reason": "workflow_path_changed"})
                continue
            cancel_run(args.repo, run_id, token)
            receipt["cancelled"].append({
                "run_id": run_id,
                "pr": pr_number,
                "head_sha": fresh_run.get("head_sha"),
                "workflow_path": fresh_run.get("path"),
                "pr_state": fresh_pr.get("state"),
                "cancel_requested_at": utcnow().isoformat(),
            })
            time.sleep(0.15)
        except Exception as exc:
            receipt["errors"].append({"run_id": run_id, "stage": "cancel", "error": str(exc)})

    receipt["cancelled_count"] = len(receipt["cancelled"])
    receipt["completed_at"] = utcnow().isoformat()
    return receipt


def write_report(report: dict[str, Any], output: str | None) -> None:
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if output:
        pathlib.Path(output).write_text(text, encoding="utf-8")
    print(text, end="")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="Luminous-Dynamics/symthaea")
    parser.add_argument("--min-age-hours", type=float, default=12.0)
    parser.add_argument("--protect-run-id", action="append", type=int, default=[])
    parser.add_argument("--max-pages", type=int, default=20)
    parser.add_argument("--max-cancels", type=int, default=25)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--plan", type=pathlib.Path)
    parser.add_argument("--expect-plan-sha256")
    parser.add_argument("--json-output")
    args = parser.parse_args()

    if "/" not in args.repo:
        raise SystemExit("--repo must be owner/name")
    if args.min_age_hours < 1:
        raise SystemExit("--min-age-hours must be >= 1")
    if args.max_cancels < 1:
        raise SystemExit("--max-cancels must be >= 1")

    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if args.apply:
        if not token:
            raise SystemExit("--apply requires GITHUB_TOKEN or GH_TOKEN")
        if args.plan is None or not args.expect_plan_sha256:
            raise SystemExit("--apply requires --plan and --expect-plan-sha256")
        report = apply_plan(args, token, load_plan(args.plan))
    else:
        if args.plan is not None or args.expect_plan_sha256:
            raise SystemExit("--plan/--expect-plan-sha256 are valid only with --apply")
        report = build_plan(args, token)

    write_report(report, args.json_output)


if __name__ == "__main__":
    main()
