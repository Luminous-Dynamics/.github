# 📦 Dependency Management

> "Choose dependencies wisely. Each one is a promise of maintenance forever."

*Last updated: January 2025*

This document outlines our **dependency management philosophy and practices**—how we select, maintain, and manage external dependencies to build secure, stable, and maintainable systems.

---

## 🎯 Dependency Philosophy

### The Dependency Paradox

**Benefits of dependencies**:
- ✅ Don't reinvent the wheel
- ✅ Leverage expert implementations
- ✅ Faster development
- ✅ Battle-tested code

**Costs of dependencies**:
- ❌ Security vulnerabilities
- ❌ License incompatibilities
- ❌ Maintenance burden
- ❌ Breaking changes
- ❌ Supply chain attacks
- ❌ Abandoned projects

**Our approach**: **Prudent adoption, active maintenance.**

### Dependency Principles

1. **Deliberate over default**: Every dependency is a conscious choice
2. **Maintained over popular**: Active maintenance beats popularity
3. **Small over large**: Prefer focused libraries to kitchen sinks
4. **Stable over cutting-edge**: Proven stability over newest features
5. **Few over many**: Minimize dependency count
6. **Auditable over opaque**: Understand what code you're running
7. **Licensed over incompatible**: Respect licenses (especially AGPL-3.0)
8. **Secure by default**: Security scanning from day one

---

## 🔍 Dependency Selection

### Evaluation Criteria

**Before adding a dependency, evaluate**:

#### 1. Necessity
- [ ] Is this dependency truly necessary?
- [ ] Can I implement this myself reasonably?
- [ ] Is the complexity worth the dependency?
- [ ] What's the cost of not using it?

**Red flags**:
- Adding dependency for one function you could write in 10 lines
- Adding large framework when small library would do
- Using dependency just because it's familiar

#### 2. Maintenance

**Check repository**:
- [ ] Last commit: <6 months ago
- [ ] Open issues: Reasonable count, being addressed
- [ ] Open PRs: Being reviewed and merged
- [ ] Maintainer response time: <1 week for issues
- [ ] Clear roadmap or vision
- [ ] Breaking changes: Infrequent, well-communicated

**Red flags**:
- ⚠️ Last commit >1 year ago (likely abandoned)
- ⚠️ Hundreds of open issues, no responses
- ⚠️ PRs from months/years ago with no activity
- ⚠️ "Looking for maintainer" notice
- ⚠️ Major version 0.x with no stability plan

#### 3. Maturity

**Version and adoption**:
- [ ] Version ≥1.0 (stable API)
- [ ] Used in production by others
- [ ] Good test coverage
- [ ] Semantic versioning followed
- [ ] Changelog maintained

**Exceptions**: Carefully consider pre-1.0 dependencies
- Must be actively maintained
- Roadmap to 1.0 clear
- Worth the instability risk

#### 4. License

**License compatibility**:
- [ ] License is compatible with ours (AGPL-3.0)
- [ ] License is OSI-approved
- [ ] License terms are acceptable
- [ ] No restrictive clauses

**Our license**: AGPL-3.0 (copyleft)

**Compatible**:
- ✅ MIT, Apache 2.0, BSD
- ✅ GPL, LGPL (with care)
- ✅ AGPL (same license)

**Potentially problematic**:
- ⚠️ GPL (in some cases)
- ⚠️ SSPL, BSL (not OSI-approved)
- ⚠️ Custom licenses (review carefully)

**Incompatible**:
- ❌ Proprietary/closed source
- ❌ Non-commercial licenses
- ❌ Licenses requiring patent grants we can't make

See [LEGAL.md](LEGAL.md) for detailed license guidance.

#### 5. Security

**Security posture**:
- [ ] No known critical vulnerabilities
- [ ] Security policy documented
- [ ] Past vulnerabilities handled well
- [ ] Regular security updates
- [ ] Minimal attack surface

**Check**:
- npm audit, cargo audit, pip-audit, etc.
- Snyk, Dependabot, GitHub Security Advisories
- CVE databases

#### 6. Size and Performance

**Dependency weight**:
- [ ] Reasonable size (not bloated)
- [ ] No unnecessary sub-dependencies
- [ ] Good performance characteristics
- [ ] Tree-shakeable (if applicable)

**Example checks**:
```bash
# npm package size
npm install --dry-run <package>
bundlephobia.com  # Check bundle size

# Python package dependencies
pipdeptree

# Rust dependency tree
cargo tree
```

#### 7. Documentation

**Quality documentation**:
- [ ] README explains what it does
- [ ] Examples provided
- [ ] API documentation
- [ ] Migration guides for breaking changes
- [ ] Active community/support

**Red flags**:
- Minimal README
- No examples
- Outdated docs contradicting code
- No community support

#### 8. Community

**Healthy community**:
- [ ] Multiple contributors (not single-person project)
- [ ] Responsive to community
- [ ] Welcoming culture
- [ ] Clear contribution guidelines

**Bus factor**: What happens if the main maintainer disappears?
- **High risk**: Single maintainer, no successors
- **Lower risk**: Multiple active maintainers, clear governance

---

## 📋 Dependency Checklist

**Before adding a dependency**, complete this checklist:

```markdown
## Dependency: [package-name]

### Why do we need this?
[Explain the problem it solves]

### Why not implement ourselves?
[Explain why custom implementation isn't feasible]

### Evaluation

**Necessity**: [1-5, 5=critical] __/5
**Maintenance**: [Last commit, issue response] ___
**Maturity**: [Version, production usage] ___
**License**: [License name, compatible?] ___
**Security**: [Known vulnerabilities?] ___
**Size**: [Bundle size, dependencies] ___
**Documentation**: [Quality: Good/OK/Poor] ___
**Community**: [Bus factor, responsiveness] ___

### Alternatives Considered

1. **[Alternative 1]**: [Why not?]
2. **[Alternative 2]**: [Why not?]
3. **Build ourselves**: [Why not?]

### Decision

[ ] Approved - Benefits outweigh costs
[ ] Rejected - Costs outweigh benefits
[ ] Deferred - Needs more research

**Approver**: @[maintainer]
**Date**: [YYYY-MM-DD]
```

---

## 🔄 Dependency Maintenance

### Keeping Dependencies Updated

**Why update?**
- Security patches
- Bug fixes
- Performance improvements
- New features
- Stay current (easier to upgrade incrementally)

**Update strategy**:

**Patch updates** (1.2.3 → 1.2.4):
- Auto-update with tests passing
- Low risk, high value

**Minor updates** (1.2.0 → 1.3.0):
- Review changelog
- Test thoroughly
- Update monthly

**Major updates** (1.x → 2.x):
- Review migration guide
- Expect breaking changes
- Test extensively
- Schedule dedicated time

### Automated Dependency Updates

**Tools**:
- **Dependabot** (GitHub native)
- **Renovate** (highly configurable)
- **Snyk** (security-focused)

**Example Dependabot config** (`.github/dependabot.yml`):
```yaml
version: 2
updates:
  # JavaScript dependencies
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    reviewers:
      - "engineering-team"
    labels:
      - "dependencies"
    # Auto-merge patch updates
    auto-merge:
      - match:
          dependency-type: "all"
          update-type: "semver:patch"

  # Python dependencies
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
```

**Best practices**:
- Group related updates (e.g., all ESLint plugins)
- Auto-merge patch updates if tests pass
- Review minor/major updates manually
- Limit open PRs (avoid PR fatigue)

### Security Vulnerability Management

**Process**:

1. **Detection**: Automated scanning (Dependabot, Snyk)
2. **Triage**: Assess severity and exploitability
3. **Prioritize**:
   - Critical: Immediate (hours)
   - High: Urgent (days)
   - Medium: Soon (weeks)
   - Low: Eventually (months)
4. **Remediate**: Update dependency or apply workaround
5. **Verify**: Confirm vulnerability is patched
6. **Monitor**: Watch for regression

**Severity guide**:

**Critical** 🔴:
- Remote code execution
- SQL injection
- Authentication bypass
- Data exposure

**High** 🟠:
- Privilege escalation
- XSS (Cross-Site Scripting)
- CSRF (Cross-Site Request Forgery)

**Medium** 🟡:
- Information disclosure
- DoS (Denial of Service)

**Low** 🟢:
- Minor issues with limited impact

**Response times**:
- Critical: <24 hours
- High: <7 days
- Medium: <30 days
- Low: Next regular update cycle

### Dependency Auditing

**Regular audits** (monthly or quarterly):

```bash
# npm
npm audit
npm outdated

# Python
pip-audit
pip list --outdated

# Rust
cargo audit
cargo outdated

# Ruby
bundle audit
bundle outdated
```

**Review**:
- Any vulnerabilities?
- Outdated packages?
- Abandoned dependencies?
- Unnecessary dependencies?

---

## 🔐 Supply Chain Security

### Threats

**Supply chain attacks**:
1. **Compromised package**: Malicious code injected
2. **Typosquatting**: Similar-named malicious package
3. **Dependency confusion**: Internal names hijacked
4. **Account takeover**: Maintainer account compromised

**Notable incidents**:
- event-stream (2018): Bitcoin wallet stealer
- ua-parser-js (2021): Cryptocurrency miner
- colors/faker (2022): Protestware/sabotage
- PyTorch (2023): Dependency confusion

### Protection Strategies

#### 1. Lock Files

**Use lock files** to ensure reproducible builds:

**npm**: `package-lock.json`
**Python**: `requirements.txt` + `pip freeze` or `Pipfile.lock`
**Rust**: `Cargo.lock`
**Ruby**: `Gemfile.lock`

**Lock files ensure**:
- Same versions installed every time
- Sub-dependencies locked
- Integrity verified

**Commit lock files to version control!**

#### 2. Checksum Verification

**Verify package integrity**:

**npm**: Uses package-lock.json integrity hashes
```json
"lodash": {
  "version": "4.17.21",
  "integrity": "sha512-..."
}
```

**Python**: Use hashes in requirements.txt
```
# requirements.txt
lodash==4.17.21 --hash=sha256:...
```

**Cargo**: Checksums in Cargo.lock

#### 3. Dependency Pinning

**Pin dependencies** to prevent unexpected updates:

**Exact versions**:
```json
{
  "dependencies": {
    "express": "4.18.2"  // Exact version
  }
}
```

**Version ranges** (use carefully):
```json
{
  "dependencies": {
    "express": "^4.18.0"  // Minor/patch updates OK
    "lodash": "~4.17.0"   // Patch updates only
  }
}
```

**Trade-offs**:
- Exact: Most secure, but miss patches
- Range: Get patches, but risk unexpected changes

**Our preference**: Exact versions + automated updates

#### 4. Package Signing

**Verify package authenticity**:

**npm**: Uses package signing (cosign)
**Python**: Some packages support GPG signatures
**Rust**: crates.io verifies ownership

**Where available, verify signatures.**

#### 5. Private Package Registry

**For internal packages**:

Use private registry to prevent dependency confusion:
- **npm**: npm Enterprise, Verdaccio, GitHub Packages
- **Python**: PyPI private index, Artifactory
- **Rust**: Custom crate registry

**Scoped packages** (npm):
```json
{
  "dependencies": {
    "@luminous-dynamics/internal-lib": "1.0.0"
  }
}
```

#### 6. Minimal Privileges

**Restrict publish access**:
- Two-factor authentication (2FA) required
- Minimal team members with publish rights
- Automation via CI with scoped tokens
- Regular access audits

---

## 📊 Dependency Health Metrics

**Track dependency health**:

### Metrics to Monitor

**Update frequency**:
- How often do we update dependencies?
- Target: Patch weekly, minor monthly, major quarterly

**Vulnerability count**:
- Current open vulnerabilities
- Target: 0 critical, <5 high

**Outdated packages**:
- Packages >6 months behind latest
- Target: <10% of dependencies

**Abandoned dependencies**:
- Dependencies not updated in >1 year
- Target: 0 (replace or vendor)

**License compliance**:
- All dependencies have compatible licenses
- Target: 100% compliance

### Dependency Dashboard

**Example Grafana dashboard**:
- Total dependencies (gauge)
- Dependencies by license (pie chart)
- Outdated dependencies (table)
- Vulnerabilities by severity (bar chart)
- Update latency (histogram)

**Review quarterly** in tech debt meetings.

---

## 🗂️ Monorepo vs Multirepo

### Monorepo (Single Repository)

**All packages in one repo**.

**Pros**:
- Easy to coordinate changes across packages
- Shared tooling and configuration
- Atomic commits across projects
- Simplified dependency management

**Cons**:
- Large repository
- Longer CI times
- Requires good tooling (Nx, Turborepo, Bazel)

**When to use**:
- Tightly coupled packages
- Shared infrastructure
- Coordinated releases

**Tools**:
- **Lerna**: JavaScript monorepo tool
- **Nx**: Build system for monorepos
- **Turborepo**: Fast build system
- **Bazel**: Google's build tool

### Multirepo (Multiple Repositories)

**Each package in separate repo**.

**Pros**:
- Clear ownership boundaries
- Smaller, focused repositories
- Independent releases
- Easier to open source individual packages

**Cons**:
- Cross-repo changes are hard
- Dependency management complexity
- Duplicate tooling/configuration

**When to use**:
- Loosely coupled packages
- Different teams/owners
- Independent release cycles

---

## 🚫 Dependency Anti-Patterns

### What NOT to Do

**❌ Left-pad syndrome**:
Installing a dependency for a trivial function you could write yourself.

```javascript
// Don't do this
import leftPad from 'left-pad';
leftPad('foo', 5);

// Do this
'foo'.padStart(5);  // Built-in!
```

**❌ Kitchen sink dependencies**:
Importing massive library for one small feature.

```javascript
// Don't do this (pulls in 100+ KB for one function)
import _ from 'lodash';
_.debounce(fn, 100);

// Do this (pulls in just what you need)
import debounce from 'lodash.debounce';
debounce(fn, 100);

// Or even better, write it yourself (it's ~10 lines)
```

**❌ Ignoring security warnings**:
"It's probably fine..." ← Famous last words

**Always investigate and fix security warnings.**

**❌ Never updating**:
"If it ain't broke, don't fix it" doesn't apply to dependencies.

**Outdated dependencies accumulate security debt.**

**❌ Updating everything blindly**:
Auto-merging major versions without testing.

**Major versions can (and do) break things.**

**❌ Dependency on unmaintained packages**:
Using packages abandoned years ago.

**Either fork and maintain, or replace.**

**❌ Circular dependencies**:
Package A depends on B, which depends on A.

**Indicates design problem. Refactor.**

**❌ Committing node_modules** (or equivalent):
Vendoring dependencies in version control (usually).

**Use lock files instead. Exceptions: vendoring for supply chain security.**

---

## 🔧 Vendoring Dependencies

### What is Vendoring?

**Vendoring**: Copying dependency source code into your repository.

**Example**: `vendor/` directory with all dependencies.

### When to Vendor

**Consider vendoring when**:
- High security requirements (prevent supply chain attacks)
- Dependency is abandoned (but you need it)
- Air-gapped environments (no internet access)
- Regulatory compliance requires code audit

**Don't vendor when**:
- Dependencies are actively maintained
- You can use lock files and integrity checks
- Repository size is a concern

### How to Vendor

**Go** (built-in):
```bash
go mod vendor
```

**Python**:
```bash
pip install -r requirements.txt -t vendor/
```

**JavaScript** (less common):
```bash
# Use npm-shrinkwrap or manually copy node_modules
```

**Rust**:
```bash
cargo vendor
```

**Pros**:
- ✅ Full control over dependencies
- ✅ Protection from supply chain attacks
- ✅ Works offline
- ✅ Can patch dependencies locally

**Cons**:
- ❌ Larger repository
- ❌ Must manually update
- ❌ Diff noise in code reviews
- ❌ Maintenance burden

---

## 📜 License Management

### License Inventory

**Know what licenses you're using**:

```bash
# npm
npm install -g license-checker
license-checker --summary

# Python
pip install pip-licenses
pip-licenses

# Rust
cargo install cargo-license
cargo license
```

**Output**:
```
MIT: 42 packages
Apache-2.0: 18 packages
BSD-3-Clause: 7 packages
ISC: 3 packages
```

### AGPL-3.0 Compliance

**Our license**: AGPL-3.0 (strong copyleft)

**Requirements**:
- Source code must be available
- Network use = distribution (must share source)
- Derivative works must be AGPL-3.0

**Compatible licenses** (we can use):
- MIT, Apache 2.0, BSD
- GPL, LGPL (with proper linking)
- AGPL

**Potentially problematic**:
- SSPL (not OSI-approved, similar to AGPL but stricter)
- Custom licenses (review carefully)

**See** [LEGAL.md](LEGAL.md) for full license guidance.

### License Compliance Automation

**Tools**:
- **FOSSA**: License compliance platform
- **WhiteSource/Mend**: License and security scanning
- **Black Duck**: License compliance
- **ClearlyDefined**: License clarity

**GitHub Actions** for license checking:
```yaml
name: License Check
on: [pull_request]
jobs:
  license-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check licenses
        run: |
          npm install -g license-checker
          license-checker --failOn 'GPL-3.0;AGPL-3.0' # Fail on incompatible
```

---

## 🎯 Dependency Best Practices

### Do's ✅

**Regularly update dependencies**:
- Patch: Weekly
- Minor: Monthly
- Major: Quarterly (with testing)

**Pin dependencies**:
- Use exact versions
- Commit lock files
- Automate updates (Dependabot, Renovate)

**Audit dependencies**:
- Run `npm audit` / `cargo audit` / etc. weekly
- Fix critical/high severity immediately

**Review before adding**:
- Complete dependency checklist
- Consider alternatives
- Evaluate maintenance and security

**Document dependency decisions**:
- Why we chose this dependency
- What alternatives we considered
- Any known issues or caveats

**Use security tools**:
- Snyk, Dependabot, GitHub Security
- Integrate into CI/CD

**Test dependency updates**:
- Automated tests must pass
- Manual testing for major updates

### Don'ts ❌

**Don't ignore security warnings**:
- Every warning should be triaged
- Fix or document why it's not a risk

**Don't add dependencies lightly**:
- Every dependency has a cost
- "Just install this package" isn't enough justification

**Don't use unmaintained packages**:
- Replace or fork and maintain
- Don't ignore "last updated 3 years ago"

**Don't skip license review**:
- License violations can be legal issues
- Check every dependency's license

**Don't commit secrets in dependencies**:
- Audit dependencies for leaked secrets
- Use tools like TruffleHog, GitGuardian

---

## 💚 Conscious Dependency Management

**Dependencies are relationships, not just code.**

**Consciousness-first dependency management**:
- **Respect maintainers**: We depend on their work
- **Contribute back**: Report bugs, submit fixes, sponsor
- **Share knowledge**: Document what you learn
- **Be grateful**: Thank maintainers for their work
- **Build community**: Support healthy open source ecosystem

**Each dependency is maintained by humans**:
- Often volunteers
- Often unpaid
- Often overworked

**Support the ecosystem**:
- Sponsor projects you depend on
- Contribute fixes and improvements
- Be kind in issues and PRs
- Share your success stories

**Sustainable dependency management benefits everyone.** 💚✨

---

## 📚 Related Resources

- [LEGAL.md](LEGAL.md) - License compliance
- [SECURITY.md](SECURITY.md) - Security practices
- [DEVELOPER_EXPERIENCE.md](DEVELOPER_EXPERIENCE.md) - Developer tooling
- [SUSTAINABILITY.md](SUSTAINABILITY.md) - Funding and support

---

*This dependency management guide is maintained with care and consciousness by the Luminous Dynamics community.*
