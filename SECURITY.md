# Security Policy

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub issues.**

The preferred path is **GitHub private vulnerability reporting**, enabled on this org's active repositories ([`symthaea`](https://github.com/Luminous-Dynamics/symthaea), [`mycelix`](https://github.com/Luminous-Dynamics/mycelix), [`symtropy`](https://github.com/Luminous-Dynamics/symtropy), [`xenia-peer`](https://github.com/Luminous-Dynamics/xenia-peer), [`xenia-wire`](https://github.com/Luminous-Dynamics/xenia-wire), [`nix-signature-policy`](https://github.com/Luminous-Dynamics/nix-signature-policy)) — open the repo's **Security** tab → **Report a vulnerability**. This reaches maintainers directly and keeps the report private until resolved.

If you can't use that (e.g. a repo where it isn't enabled yet), email:

**tristan.stoltz@evolvingresonantcocreationism.com**

*(A dedicated `security@` address and a published PGP key are planned but not yet live — this personal address is the real, current contact until that lands. If you need to encrypt a report in the meantime, say so in your first message and we'll arrange a channel.)*

Include: type of vulnerability, affected repo/commit/file paths, reproduction steps, proof of concept, and impact.

### What to Expect

These are **target response times**, not contractual guarantees — this is a small, largely solo-maintained research organization, and actual response time depends on maintainer availability:

- **Acknowledgment**: aim for 48 hours, may take longer on nights/weekends
- **Severity assessment and initial triage**: aim for 7 days
- **Fix timeline**: depends on severity and whether the affected code is production-facing or pre-alpha research (see Scope below) — critical issues in an active flagship's supported surface get priority; issues in explicitly pre-alpha/research code are triaged but not held to the same clock

## Scope

This policy covers the **currently active, non-archived repositories** in this organization — primarily [`symthaea`](https://github.com/Luminous-Dynamics/symthaea), [`mycelix`](https://github.com/Luminous-Dynamics/mycelix), [`symtropy`](https://github.com/Luminous-Dynamics/symtropy), [`xenia-peer`](https://github.com/Luminous-Dynamics/xenia-peer)/[`xenia-wire`](https://github.com/Luminous-Dynamics/xenia-wire), and [`nix-signature-policy`](https://github.com/Luminous-Dynamics/nix-signature-policy). Check a given repository's own archive status and README before assuming it's in scope — `terra-atlas` and `luminous-nix`, for example, are archived and not actively maintained.

### A note on maturity

Most of this organization's public code is **pre-alpha research**, explicitly labeled as such in each repo's README. We do want security reports on pre-alpha code — a real vulnerability in experimental cryptographic or consent-flow code (Xenia especially) is worth knowing about even before it's "production." But "pre-alpha" also means: don't assume any given surface has been threat-modeled or audited unless its docs say so. Repo-specific threat models, where they exist, are linked below.

### Vulnerability classes

- **Protocol-level vulnerabilities** (e.g. a flaw in `xenia-wire`'s wire format or handshake, or in a Holochain zome's validation logic in Mycelix) — always in scope, highest priority regardless of the specific repo's maturity label.
- **Application-level vulnerabilities** (e.g. a bug in `xenia-peer`'s daemon, a Symthaea binary, a Mycelix frontend) — in scope for active repos.
- **Unsupported/explicitly-experimental modules** — code a repo's own docs mark as scaffold, mock, or research-only is lower priority; we'd still like to know, but it's not held to the response-time targets above.
- **Dependency vulnerabilities** — a vulnerability in a third-party dependency this org's code integrates is **in scope for how we use it**, even though the fix ultimately belongs upstream. If a dependency's CVE is exploitable through one of these repos' actual usage of it (not just present in a lockfile), report it here too, not only to the upstream maintainer — we'll assess whether our integration needs its own mitigation (e.g. pinning, a wrapper, disabling a feature) independent of the upstream fix timeline.

### Out of Scope

- Third-party services this org integrates with (report to their own security contact)
- User-deployed instances with custom modifications
- Social engineering, physical security
- Denial-of-service reports against research/demo infrastructure not intended for production load

## Repository-Specific Threat Models

Where a repo has published its own threat model or audit status, that supersedes the general guidance above for that repo:

- **Xenia** (`xenia-peer`, `xenia-wire`): see `docs/security/OPERATOR_SECURITY_MODEL.md` and `docs/security/LEDGER_VERIFICATION_BOUNDARY.md` in `xenia-peer`, and `SECURITY.md` in `xenia-wire`. Both repos are pre-alpha and explicitly document open gaps — read those before assuming a given code path has been hardened.
- **Mycelix**: DHT/zome-level integrity validation status varies by cluster; check the specific cluster's own docs.

## Coordinated Disclosure

We ask that you give us a reasonable window to investigate and, where applicable, ship a fix before public disclosure — informally, aim for 90 days unless we're unresponsive well past the target acknowledgment window above, in which case earlier disclosure is reasonable. We will credit you in release notes / a security advisory unless you prefer anonymity, and we do not currently run a paid bug bounty program.

## Security Best Practices

### For Users

- Use the latest commit/release of an active repo; older or archived repos do not receive security fixes
- Use secure connections; never commit secrets
- For pre-alpha code (most of this org's work), treat it as research software, not something to deploy against real user data or real infrastructure without your own review

### For Contributors

- No hardcoded secrets — use environment variables or a secret manager
- Validate and sanitize all external input
- All changes require review before merging

## Security Contacts

**Primary contact**: tristan.stoltz@evolvingresonantcocreationism.com, or GitHub private vulnerability reporting on the relevant repo (preferred).

---

Thank you for helping keep this work — and the people who rely on it — safe.
