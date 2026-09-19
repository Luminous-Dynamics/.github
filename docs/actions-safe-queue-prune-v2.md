# Safe Queue Pruning v2

`actions-safe-queue-prune.py` uses a two-phase protocol so the candidate set cannot silently change between review and cancellation.

## Phase 1 — produce a plan

Run read-only discovery and save the plan:

```bash
GITHUB_TOKEN=... python3 scripts/actions-safe-queue-prune.py \
  --repo Luminous-Dynamics/symthaea \
  --min-age-hours 12 \
  --protect-run-id 35439414230 \
  --json-output /tmp/symthaea-prune-plan.json
```

Review `eligible` and record `plan_sha256`. The SHA-256 covers the immutable authorization surface: repository, minimum age, protected run IDs, exact eligible run identities/heads/workflow paths/PRs, and nonclaims.

## Phase 2 — apply exactly the reviewed plan

Apply only that reviewed plan and hash:

```bash
GITHUB_TOKEN=... python3 scripts/actions-safe-queue-prune.py \
  --repo Luminous-Dynamics/symthaea \
  --min-age-hours 12 \
  --protect-run-id 35439414230 \
  --max-cancels 25 \
  --apply \
  --plan /tmp/symthaea-prune-plan.json \
  --expect-plan-sha256 <reviewed-plan-sha256> \
  --json-output /tmp/symthaea-prune-apply.json
```

Apply refuses to run if the plan hash, repository, age threshold, or protected-run set differs from what was reviewed.

For every selected candidate it then re-fetches the run and PR and requires all of the following immediately before cancellation:

- run is still `queued`;
- event is still `pull_request`;
- minimum age still holds;
- exactly one associated PR still matches;
- PR is still `closed`;
- run ID is not protected;
- run head SHA still matches the reviewed plan;
- workflow path still matches the reviewed plan.

The apply receipt records the source plan SHA-256, every cancellation request, every revalidation skip, and every error.

## Protected REL-005A subjects

These runs are hard-protected in the tool:

- `35349750595` — REL-005A ComparisonOnly V3 R2
- `35439414230` — REL-005A Qualification Pipeline V3

Additional protected IDs can be supplied with repeated `--protect-run-id` options.

## Authority boundary

This utility has authority `OperationalQueueHygieneOnly`. Queue cleanup is not scientific evidence, does not mutate a scientific result, does not rewrite an evidence subject, and does not guarantee execution priority.
