# Release Process & Versioning

*"In unity we code, in love we debug, in consciousness we deploy"* ✨

## Overview

This document outlines how Luminous Dynamics projects handle releases, versioning, and deployment with consciousness-first principles.

## Semantic Versioning

We use **Semantic Versioning 2.0.0** (SemVer) for all projects.

### Version Format: MAJOR.MINOR.PATCH

**MAJOR** (1.0.0 → 2.0.0):
- Breaking changes
- API incompatibilities
- Major architectural shifts
- Requires user action to upgrade

**MINOR** (1.0.0 → 1.1.0):
- New features (backward compatible)
- Significant enhancements
- New capabilities added
- Safe to upgrade

**PATCH** (1.0.0 → 1.0.1):
- Bug fixes
- Security patches
- Performance improvements
- Documentation updates

### Pre-Release Versions

**Alpha** (1.0.0-alpha.1):
- Very early, experimental
- APIs may change dramatically
- Not feature complete
- Internal testing

**Beta** (1.0.0-beta.1):
- Feature complete
- APIs mostly stable
- External testing welcome
- Known bugs may exist

**Release Candidate** (1.0.0-rc.1):
- Production-ready candidate
- No new features
- Only critical bug fixes
- Final testing before release

## Release Philosophy

### Consciousness-First Releases

Our release process honors:

- **Sacred Time**: No rushed releases for artificial deadlines
- **Quality**: Thoroughly tested before release
- **Transparency**: Clear communication about changes
- **Accessibility**: Migration guides for breaking changes
- **Community**: User feedback shapes release timing

### When Ready, Not When Scheduled

We release when software is **truly ready**, not on arbitrary schedules. This aligns with sacred development principles.

**However**, we aim for:
- **Security patches**: Within 24-72 hours of discovery
- **Critical bugs**: Within 1 week
- **Minor releases**: Every 4-8 weeks (when features ready)
- **Major releases**: Every 6-12 months (when justified)

## Release Process

### 1. Pre-Release Planning

**Identify Changes**:
- Review merged PRs since last release
- Categorize: breaking, features, fixes
- Determine version number (SemVer)

**Check Readiness**:
- [ ] All planned features merged
- [ ] Tests passing
- [ ] Documentation updated
- [ ] CHANGELOG drafted
- [ ] Breaking changes have migration guides
- [ ] Security audit completed (if applicable)

**ERC Alignment Check**:
- [ ] Does this serve consciousness-first principles?
- [ ] Have we honored sacred development pace?
- [ ] Is the quality worthy of release?
- [ ] Have we communicated transparently?

### 2. Prepare Release

**Update CHANGELOG**:
```markdown
## [1.2.0] - 2025-11-14

### Added
- Natural language pattern matching for 20 new commands
- Voice control integration (experimental)
- Web dashboard for command history

### Changed
- Improved fuzzy matching accuracy by 15%
- Updated Python requirement to 3.11+

### Fixed
- Bug #42: Crash on invalid Nix syntax
- Memory leak in cache system
- Typos in help documentation

### Security
- Updated dependencies to patch CVE-2025-XXXX

### Breaking Changes
None

### Migration Guide
Python 3.10 users must upgrade to 3.11+:
\`\`\`bash
# Update Python
sudo apt install python3.11
# Reinstall luminous-nix
pip install --upgrade luminous-nix
\`\`\`
```

**Update Version Numbers**:
- `pyproject.toml` or `package.json` or `Cargo.toml`
- Any hardcoded version references
- Documentation version badges

**Tag Release**:
```bash
git tag -a v1.2.0 -m "Release v1.2.0: Natural language improvements"
git push origin v1.2.0
```

### 3. Create GitHub Release

**Release Notes Template**:
```markdown
# 🌟 Luminous [Project] v1.2.0

> *Building consciousness-first technology that serves all beings*

## ✨ Highlights

[2-3 sentence summary of this release]

## 🚀 What's New

### Natural Language Pattern Expansion
We've added support for 20 new command patterns, making it even easier to interact with NixOS naturally.

### Voice Control (Experimental)
Try controlling your system with voice commands! This is an early experiment - feedback welcome.

### Web Dashboard
View your command history and patterns through a new web interface.

## 📝 Full Changelog

[Link to CHANGELOG.md section]

## 🐛 Bug Fixes

- Fixed crash on invalid Nix syntax (#42)
- Resolved memory leak in cache system
- Corrected help documentation typos

## 🔐 Security Updates

Updated dependencies to address CVE-2025-XXXX. All users should upgrade.

## 📚 Documentation

- [Installation Guide](link)
- [Upgrade Guide](link)
- [Full Documentation](link)

## 💖 Thank You

Special thanks to our contributors:
@contributor1, @contributor2, @contributor3

This release includes contributions from X contributors with Y commits.

## 🙏 Support Our Work

If this release serves you, consider supporting via:
- [Ko-fi](https://ko-fi.com/luminousdynamics)
- [Terra Lumina Investment](https://terra-lumina.com/invest)
- Contributing code, docs, or feedback!

---

*"In unity we code, in love we debug, in consciousness we deploy"* ✨

**Full Changelog**: v1.1.0...v1.2.0
```

### 4. Publish Release

**For Python Projects**:
```bash
# Build distribution
python -m build

# Upload to PyPI
python -m twine upload dist/*
```

**For Rust Projects**:
```bash
# Publish to crates.io
cargo publish
```

**For TypeScript/JavaScript**:
```bash
# Publish to npm
npm publish
```

**For NixOS**:
```bash
# Update nixpkgs PR
# Follow NixOS contribution guidelines
```

### 5. Announce Release

**Communication Channels**:
- [ ] GitHub Discussions post
- [ ] Update project README
- [ ] Social media (if applicable)
- [ ] Email newsletter (if exists)
- [ ] Community Discord/Slack (if exists)

**Announcement Template**:
```markdown
🎉 **[Project] v1.2.0 Released!**

We're excited to announce [Project] v1.2.0 with natural language improvements, voice control experiments, and important security updates.

**Highlights**:
✨ 20 new command patterns
🎤 Experimental voice control
📊 Web dashboard for command history
🔐 Security updates

[Read full release notes](link)
[Upgrade guide](link)

Thank you to all contributors! 💚
```

### 6. Post-Release

**Monitor**:
- Issue reports
- User feedback
- Crash reports
- Performance metrics

**Support**:
- Respond to questions quickly
- Fix critical bugs immediately
- Plan patch releases if needed

**Reflect**:
- What went well?
- What could improve?
- Update this process based on learning

## Project-Specific Guidelines

### Mycelix-Core (Rust)

**Versioning**:
- Conservative major version bumps (security/trust is critical)
- Extensive testing before each release
- Security audit for all releases

**Release Cadence**:
- Patch: As needed for bugs/security
- Minor: Every 2-3 months
- Major: Every 12-18 months

**Special Considerations**:
- Byzantine resistance benchmarks must maintain
- Reproducibility via STARK proofs
- Holochain compatibility verified

### Terra Atlas (TypeScript/Next.js)

**Versioning**:
- Rapid iteration for UX improvements
- Breaking changes rare (platform stability matters)

**Release Cadence**:
- Patch: Weekly (bug fixes, UX tweaks)
- Minor: Every 2-4 weeks (new features)
- Major: Every 6-12 months

**Special Considerations**:
- Database migrations tested thoroughly
- Swiss foundation governance compatibility
- Investment data accuracy verified

### Luminous Nix (Python)

**Versioning**:
- Minor bumps for new patterns
- Major only for fundamental changes

**Release Cadence**:
- Patch: As needed
- Minor: Monthly (pattern additions)
- Major: Yearly (architectural shifts)

**Special Considerations**:
- NixOS version compatibility maintained
- Pattern accuracy benchmarks tracked
- Safety checks always working

### Kosmic Lab (Python)

**Versioning**:
- Research tool, more lenient
- Clear API stability commitments

**Release Cadence**:
- As features complete
- Research timeline driven

**Special Considerations**:
- Reproducibility guaranteed
- K-Codex compatibility maintained
- Bayesian optimization validated

## Breaking Changes

### Minimizing Breaking Changes

**Before Making Breaking Change**:
1. Can we maintain backward compatibility?
2. Can we deprecate gracefully?
3. Is the benefit worth the disruption?
4. Have we communicated plans early?

### When Breaking Changes Necessary

**Deprecation Process**:
1. **Warning phase** (1-2 releases):
   - Add deprecation warnings
   - Document migration path
   - Provide both old and new APIs

2. **Transition phase** (1 release):
   - Old API deprecated but functional
   - New API recommended
   - Clear migration guide

3. **Removal phase** (major version):
   - Old API removed
   - Only new API available
   - Comprehensive upgrade guide

**Migration Guide Requirements**:
```markdown
## Migration from 1.x to 2.0

### Breaking Changes

#### 1. Function Rename: `old_function()` → `new_function()`

**Old way (1.x)**:
\`\`\`python
result = old_function(param1, param2)
\`\`\`

**New way (2.0)**:
\`\`\`python
result = new_function(param1, param2, new_param)
\`\`\`

**Why changed**: [Reasoning]
**Migration script**: [If available]

#### 2. Configuration Format Change

**Old format**:
\`\`\`yaml
config:
  old_structure: value
\`\`\`

**New format**:
\`\`\`yaml
config:
  new:
    structure: value
\`\`\`

**Migration tool**:
\`\`\`bash
luminous-migrate-config config.yml
\`\`\`
```

## Release Checklist

Use this for every release:

### Pre-Release
- [ ] All tests passing
- [ ] Documentation updated
- [ ] CHANGELOG complete
- [ ] Version numbers bumped
- [ ] Breaking changes have migration guides
- [ ] Security audit (if applicable)
- [ ] ERC alignment verified

### Release
- [ ] Git tag created
- [ ] GitHub release published
- [ ] Package published (PyPI/npm/crates.io)
- [ ] Documentation deployed
- [ ] Release notes comprehensive
- [ ] Contributors thanked

### Post-Release
- [ ] Announcement posted
- [ ] Community notified
- [ ] Monitoring active
- [ ] Quick response to issues
- [ ] Retrospective completed

## Hotfix Process

For critical bugs or security issues in production:

### 1. Assess Severity

**Critical** (Immediate hotfix):
- Security vulnerabilities
- Data loss bugs
- System crashes
- Complete feature breakage

**High** (Fast hotfix):
- Major functionality broken
- Significant performance degradation
- User-impacting bugs

**Medium/Low** (Wait for next release):
- Minor bugs
- Cosmetic issues
- Documentation errors

### 2. Hotfix Branch

```bash
# Create hotfix branch from latest release
git checkout -b hotfix/v1.2.1 v1.2.0

# Fix the bug
git commit -m "fix: critical security vulnerability CVE-2025-XXXX"

# Bump patch version
# Update CHANGELOG

# Tag hotfix
git tag -a v1.2.1 -m "Hotfix: Security patch"

# Merge to main and develop
git checkout main
git merge hotfix/v1.2.1
git checkout develop
git merge hotfix/v1.2.1

# Push
git push origin main develop --tags
```

### 3. Expedited Release

- Skip normal release timeline
- Minimal changelog (focus on fix)
- Clear security advisory if applicable
- Immediate publication
- Urgent communication

## Version Lifecycle

### Support Policy

**Current Release**:
- Full support
- New features
- Bug fixes
- Security patches

**Previous Minor (N-1)**:
- Security patches only
- Critical bug fixes
- For 6 months after new release

**Previous Major (N-1 major)**:
- Security patches only
- For 12 months after new major

**End of Life**:
- No support
- Clear EOL announcement
- Migration path provided

### Example Timeline

```
v1.0.0 (Jan 2025) → v1.1.0 (Mar 2025) → v1.2.0 (May 2025) → v2.0.0 (Jan 2026)
│                    │                   │                   │
└─ EOL Sep 2025     └─ EOL Nov 2025    └─ EOL Nov 2026    └─ Current

Support:
v2.0.x: Full support
v1.2.x: Security only (until Nov 2026)
v1.1.x: EOL
v1.0.x: EOL
```

## Sacred Release Practices

### Consciousness-First Releasing

- **No crunch**: Never rush releases at cost of well-being
- **Quality**: Thorough testing, worthy of users' trust
- **Honesty**: Transparent about limitations and bugs
- **Gratitude**: Thank contributors meaningfully
- **Service**: Releases serve users, not vanity metrics

### Gift Economy Integration

- Releases are gifts to community
- No features locked behind payments
- Voluntary support encouraged but never required
- Community input shapes release priorities
- Recognition over compensation (though both honored)

## Questions About Releases?

- Review project-specific CHANGELOG files
- Check GitHub release pages
- Ask in Discussions with `[Release]` tag
- Email: invest@luminousdynamics.org

---

**Last Updated**: November 2025
**Next Review**: Quarterly

*Releasing with intention, care, and love* 💚✨

## Related Documents

- [CONTRIBUTING.md](./CONTRIBUTING.md) - How to contribute to releases
- [SECURITY.md](./SECURITY.md) - Security patch process
- [GOVERNANCE.md](./GOVERNANCE.md) - Release decision authority
- [ADR.md](./ADR.md) - Architecture decisions affecting releases
