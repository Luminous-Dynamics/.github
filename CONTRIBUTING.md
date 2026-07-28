# Contributing to Luminous Dynamics

Thank you for your interest in contributing. This organization's public work lives in standalone repositories, not a shared monorepo — the internal `luminous-dynamics` repo referenced by an earlier version of this document is **private** and is not where public contributions land. If a link in an issue or doc points you at it, treat that as stale.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Active Projects](#active-projects)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Communication Channels](#communication-channels)

## Code of Conduct

By participating, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## How to Contribute

1. **Choose a currently active project** — see [Active Projects](#active-projects) below, or the pinned repos / "Start Here" table on the [organization profile](https://github.com/Luminous-Dynamics).
2. **Run that repository's own quick start.** Each active repo's README has a verified `git clone` + build/test sequence for that repo specifically — there is no single org-wide setup command, because there is no single org-wide codebase.
3. **Pick an issue** labeled `good-first-issue` or `help-wanted` in that repository. If none exist yet in a repo you're interested in, open a Discussion first rather than guessing at scope.
4. **Run the project-specific preflight/test command** before opening a PR (again: per-repo, check that repo's README/CONTRIBUTING notes — most are `cargo test`/`cargo nextest run` for Rust projects, but check first).
5. **Submit a focused PR** with evidence: what you changed, why, and how you verified it (test output, a reproduction command, a screenshot for UI changes). Small, well-scoped PRs are much easier to review than large ones.

### Types of Contributions

1. **Code** — bug fixes, features, performance improvements
2. **Documentation** — improve guides, fix typos, correct stale claims
3. **Testing** — write tests, improve coverage, report edge cases
4. **Research review** — for the research-flavored repos (Symthaea, Symtropy), independent reproduction of a claimed result is one of the most valuable contributions you can make; see that repo's evidence table/status docs for what's asking to be checked

## Active Projects

The organization's active, currently-maintained public repositories (see the [org profile](https://github.com/Luminous-Dynamics) for the full, kept-current list — this file intentionally doesn't duplicate the full status table to avoid drifting out of sync with it):

- **[Symthaea](https://github.com/Luminous-Dynamics/symthaea)** — cognitive architecture research (Rust, `cargo nextest run --workspace --lib`)
- **[Mycelix](https://github.com/Luminous-Dynamics/mycelix)** — decentralized civic/commons coordination (Rust/Holochain)
- **[Symtropy](https://github.com/Luminous-Dynamics/symtropy)** — math/physics/simulation substrate (Rust)
- **[Xenia](https://github.com/Luminous-Dynamics/xenia-peer)** (+ [`xenia-wire`](https://github.com/Luminous-Dynamics/xenia-wire)) — consent-first remote sessions, pre-alpha (Rust)
- **[Nix Signature Policy](https://github.com/Luminous-Dynamics/nix-signature-policy)** — Nix signature-policy reference implementation

Older repositories not in this list (e.g. `luminous-nix`, `terra-atlas`) are archived or superseded — check a repo's own archive status and README before assuming it's the current place to contribute.

## Pull Request Process

1. **Ensure your PR**:
   - Has a clear title and description
   - References any related issues
   - Includes tests for new functionality, or a reproduction command for research claims
   - Passes that repository's CI
   - Has no merge conflicts

2. **Review process**: at least one maintainer review required; address feedback constructively.

3. **After merge**: delete your feature branch; update any related issues.

## Issue Reporting

Before creating an issue: search existing issues, check the repo's own status docs for whether the behavior is already a known/documented limitation, and confirm you're on the latest commit.

**Bug reports** should include a clear title, reproduction steps, expected vs. actual behavior, environment details, and relevant logs.

**Feature requests** should include the use case/motivation and, if it's a research-flavored repo, ideally a falsifiable claim rather than an open-ended ask — see that repo's issue template for the expected fields (hypothesis, evidence, falsification condition, etc.) where applicable.

## Communication Channels

- **GitHub Issues** — bug reports, feature requests, technical discussions (per-repo)
- **GitHub Discussions** — general questions, ideas
- **Security issues** — see [SECURITY.md](SECURITY.md); do not report vulnerabilities via public issues
- **Email** — tristan.stoltz@evolvingresonantcocreationism.com

## Development Principles

- **Test before claiming** — verify performance/correctness claims with benchmarks or reproducible commands, not estimates
- **Honest metrics** — real measurements, with limitations stated alongside them
- **Clean architecture** — maintainable, documented code
- **No invented scale or inflated certainty** — if a number in this org's docs looks wrong or stale, flag it; that's a welcome contribution in its own right

## Recognition

Contributors are recognized in release notes and project README files.

## Questions?

Open a GitHub Discussion on the relevant repository, or email tristan.stoltz@evolvingresonantcocreationism.com.

Thank you for helping build this.
