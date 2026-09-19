# GitHub Actions Hosted-Runner Allocation Runbook

This runbook is for the case where multiple Luminous Dynamics repositories have queued GitHub Actions work while no inspected repository has an in-progress run.

## 1. Establish the owner-wide observation

Run the read-only auditor from a trusted machine:

```bash
GITHUB_TOKEN=... python3 scripts/actions-runner-allocation-audit.py \
  --org Luminous-Dynamics \
  --suspect-min-age-minutes 15 \
  --json-output /tmp/luminous-actions-audit.json
```

Treat `ORG_HOSTED_RUNNER_ALLOCATION_SUSPECT` as an operational observation, not a root-cause diagnosis. It means:

- at least two repositories have waiting Actions runs;
- at least two repositories have a newest waiting run older than the configured threshold;
- no inspected repository reports an in-progress run.

Preserve the JSON report with the incident. Do not edit evidence-bearing scientific subjects merely because they are queued.

## 2. Watch an exact critical run without mutating it

Use the read-only critical-run watcher for evidence-bearing runs:

```bash
GITHUB_TOKEN=... python3 scripts/actions-critical-run-watch.py \
  --repo Luminous-Dynamics/symthaea \
  --run-id 35439414230 \
  --expected-head 460b4c8a8f457f4bbf22820716ed6057d260d4fd \
  --expected-name 'REL-005A Qualification Pipeline V3' \
  --json-output /tmp/rel-005a-qualification-watch.json
```

Interpretations:

- `REAL_QUEUED_JOB`: the run is queued and has at least one visible nonterminal job. Preserve it; do not rerun it merely to seek priority.
- `RUNNING`: runner allocation has reached the exact subject. Begin consuming only that run's formal evidence.
- `GHOST_PREQUEUE_SUSPECT`: queued, stale, and no visible jobs; handle separately from a real queued subject.
- `TERMINAL_*`: inspect the exact conclusion, jobs, logs, and artifacts before deciding whether the result is scientific, infrastructure, or process evidence.

`queued_created_before_target` and `creation_order_position_lower_bound` are observations only. GitHub does not promise strict FIFO scheduling, so these values must never be presented as an execution-time prediction.

## 3. Check public GitHub status

Check GitHub Status for Actions. Record the time and reported state in the incident. A green public status does not rule out organization-specific policy, account, capacity, or support-side issues.

## 4. Inspect organization Actions controls

An organization owner should inspect GitHub UI settings that the repository-scoped API connection cannot read:

1. **Organization Settings → Actions → General**
   - Verify Actions are enabled for the organization.
   - Verify standard GitHub-hosted runners are enabled where applicable.
   - Review allowed-actions restrictions and reusable-workflow policy.
2. **Organization Settings → Actions → Runners / Runner groups**
   - Confirm no runner-group policy accidentally excludes the affected repositories.
   - Confirm any larger/self-hosted runner groups expected by workflows are online and permitted.
3. **Enterprise settings**, if the organization is governed by an enterprise account
   - Review inherited Actions policy.
   - Review runner-group access and concurrency restrictions.
4. **Billing / budgets / spending controls**
   - Check for private-repository Actions restrictions, disabled spending, or budget policy that may block hosted execution.

Record what was checked and by whom. Do not infer the setting from queue behavior alone.

## 5. Distinguish owner-wide allocation from repository-local defects

Use the auditor plus direct run inspection:

- Multiple repositories waiting + zero active across the owner: treat as owner-wide allocation suspect.
- One repository waiting + other repositories actively running: inspect repository workflow labels, concurrency, environment gates, and required approvals.
- A run that is `queued` with zero jobs: classify separately as ghost-prequeue/control-plane state.
- A run whose parent is `in_progress` but every child job is terminal: classify separately as terminal-zombie/control-plane state.

Do not cancel or rewrite scientific evidence runs merely to make the queue look healthier.

## 6. Safely prune only provably obsolete queued runs

When the backlog contains large numbers of old queued runs from PRs that are already closed, use the local queue-pruner. It does **not** require GitHub Actions and defaults to read-only mode.

Dry run first:

```bash
GITHUB_TOKEN=... python3 scripts/actions-safe-queue-prune.py \
  --repo Luminous-Dynamics/symthaea \
  --min-age-hours 12 \
  --protect-run-id 35439414230 \
  --json-output /tmp/symthaea-queue-prune.json
```

Review every candidate. The tool only considers runs that are still `queued`, are `pull_request` runs, exceed the minimum age, have exactly one associated PR, and whose PR is currently `closed`.

Apply in small batches only after reviewing the dry-run report:

```bash
GITHUB_TOKEN=... python3 scripts/actions-safe-queue-prune.py \
  --repo Luminous-Dynamics/symthaea \
  --min-age-hours 12 \
  --protect-run-id 35439414230 \
  --max-cancels 25 \
  --apply \
  --json-output /tmp/symthaea-queue-prune-apply.json
```

Safety properties:

- `--apply` is mandatory for mutation;
- REL-005A ComparisonOnly run `35349750595` and Qualification Pipeline run `35439414230` are hard-protected by default;
- additional `--protect-run-id` values may be supplied repeatedly;
- only closed-PR runs are eligible;
- every run and PR is re-fetched immediately before cancellation;
- an open PR, changed run state, changed PR identity, insufficient age, or protected run causes a skip;
- non-PR scheduled/manual evidence runs are never candidates;
- queue cleanup does not imply any execution-priority guarantee.

Never use this tool to cancel an exact evidence-bearing subject merely because another run seems more important.

## 7. Recovery criteria

Do not declare recovery on the first server-side skip or metadata update. Recovery requires at least one real hosted job to enter `in_progress` and preferably complete successfully.

Classify partial recovery separately when some repositories have genuine in-progress hosted jobs but other repositories still have stale waiting work and zero active jobs.

For REL-005A specifically, the decisive current signal is that run `35439414230` at head `460b4c8a8f457f4bbf22820716ed6057d260d4fd` leaves `queued` and job `105887532584` begins executing. Only then consume its formal QualificationOnly evidence.

## 8. After recovery

Once runner allocation resumes:

- allow the backlog to drain without mass re-runs;
- avoid manually re-running already-queued evidence subjects unless their run is conclusively dead/cancelled;
- retain preventive draft-CI admission controls;
- keep PR Governance safety checks intact;
- prioritize frozen evidence-line runs before opening new workflow-bearing PRs;
- for REL-005A, preserve the frozen chain: ComparisonOnly → projection → assembly → firewall → QualificationOnly → durable evidence → transparent capsule → offline verification → attestation.

## Nonclaims

This runbook does not prove the outage is caused by GitHub, billing, organization policy, concurrency, or runner groups. It provides a disciplined escalation and cleanup path and keeps scientific evidence distinct from infrastructure diagnosis.
