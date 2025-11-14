# ⏳ Deprecation Policy

> "How we end things matters as much as how we begin them. Every feature deserves a graceful sunset, every user deserves clear transition guidance."

This document defines how Luminous Dynamics deprecates features, APIs, and projects with care for users and downstream dependents.

---

## 🎯 Deprecation Philosophy

### Core Principles

1. **User-First Communication**
   - Give ample warning (minimum 6 months for major features)
   - Provide clear migration paths
   - Offer migration tooling when possible
   - Be available to help users transition

2. **Minimize Disruption**
   - Maintain backward compatibility during deprecation period
   - Stagger breaking changes across releases
   - Coordinate with major downstream users
   - Consider impact on entire ecosystem

3. **Conscious Sunsetting**
   - Honor what a feature contributed
   - Document lessons learned
   - Celebrate what it enabled
   - Thank those who built and used it

4. **Transparent Reasoning**
   - Explain *why* we're deprecating
   - Share decision-making process
   - Admit when we made mistakes
   - Consider alternatives when users push back

---

## 📊 What to Deprecate (and When)

### When to Deprecate

✅ **Good Reasons:**
- Feature is superseded by better approach
- Maintenance burden outweighs user value
- Security issues can't be fixed without breaking changes
- Conflicts with consciousness-first principles
- Resource constraints (honest about capacity)

⚠️ **Reconsider:**
- Few users but high value for them (maybe just maintain, not deprecate)
- Recent feature that hasn't found users yet (give it more time)
- Personal preference ("I don't like this") without user feedback

❌ **Bad Reasons:**
- Shinier technology exists (new ≠ better)
- Original author left project (find new maintainer first)
- Code is ugly (refactor, don't deprecate)

### What Can Be Deprecated

**API Changes:**
- Function signatures
- Endpoint URLs
- Configuration formats
- Data structures

**Features:**
- Entire modules or services
- Configuration options
- CLI commands

**Projects:**
- Entire repositories
- Support for platforms/versions

---

## 🗓️ Deprecation Timeline

### Semantic Versioning Context

See [RELEASES.md](./RELEASES.md) for full SemVer details.

**Version Format:** MAJOR.MINOR.PATCH

- **PATCH** (1.0.x): No deprecations (bug fixes only)
- **MINOR** (1.x.0): Deprecate with warnings, maintain backward compatibility
- **MAJOR** (x.0.0): Remove deprecated features, breaking changes allowed

### Standard Timeline

**For Public APIs and Major Features:**

| Phase | Duration | Version | Actions |
|-------|----------|---------|---------|
| Announcement | Pre-deprecation | Current | Announce plan, gather feedback |
| Deprecation | 6-12 months | Next MINOR | Add warnings, provide migration guide |
| Removal | After deprecation period | Next MAJOR | Remove deprecated code |

**Example Timeline:**
```
v2.0.0 (Jan 2025)  - Feature X is current, no warnings
v2.1.0 (Mar 2025)  - Deprecate Feature X, add warnings, introduce Feature Y
v2.2.0 (Jun 2025)  - Feature X still works, warnings continue
v2.3.0 (Sep 2025)  - Feature X still works, warnings continue
v3.0.0 (Jan 2026)  - Remove Feature X, only Feature Y available
```

**For Minor Features:**

Minimum 3 months deprecation period, removed in next MAJOR version.

**For Critical Security Issues:**

Expedited timeline possible, but with maximum communication and migration support.

---

## 📢 Deprecation Communication

### 1. Announcement (Pre-Deprecation)

**Before** adding deprecation warnings, announce the plan:

**Where:**
- GitHub Discussion (proposal for feedback)
- Release notes (current version)
- Blog post or documentation
- Discord/community channels
- Email to known major users

**Template:**

```markdown
# Proposal: Deprecate [Feature/API Name]

## Summary

We're proposing to deprecate [feature] in favor of [alternative approach].

## Rationale

[Explain why this is being deprecated]

## Impact

**Affected Users:**
- [Describe who uses this feature]
- Estimated usage: [X% of users, or "minimal" if unknown]

**Alternatives:**
- [Recommended migration path]

## Proposed Timeline

- **Now**: Gather feedback on this proposal
- **v2.1.0 (Est. Mar 2025)**: Add deprecation warnings
- **v3.0.0 (Est. Jan 2026)**: Remove deprecated feature

## Migration Path

[Detailed steps to migrate to alternative]

## We Need Your Feedback

- Does this timeline work for you?
- Are there use cases we're not considering?
- Do you need help migrating?

**Comment on this discussion by [date] with your feedback.**
```

**Process:**
1. Post proposal
2. Gather feedback for 2-4 weeks
3. Adjust plan based on feedback
4. Finalize decision (see [ADR.md](./ADR.md))
5. Proceed with deprecation

### 2. Deprecation Warnings (Implementation)

**In Code:**

```python
import warnings

def old_function(param):
    """
    .. deprecated:: 2.1.0
        `old_function` is deprecated and will be removed in v3.0.0.
        Use `new_function` instead. See migration guide:
        https://docs.luminous-dynamics.org/migration/old-to-new
    """
    warnings.warn(
        "old_function is deprecated. Use new_function instead. "
        "See https://docs.luminous-dynamics.org/migration/old-to-new",
        DeprecationWarning,
        stacklevel=2
    )
    return new_function(param)
```

**In Documentation:**

```markdown
## `old_function(param)`

> ⚠️ **Deprecated since v2.1.0. Will be removed in v3.0.0.**
> Use [`new_function`](#new_function) instead.
> See [Migration Guide](./migration/old-to-new.md).

[Rest of documentation, but marked deprecated]
```

**In Release Notes:**

```markdown
## v2.1.0 - 2025-03-15

### Deprecated

- **`old_function`** - Deprecated in favor of `new_function`. Will be removed
  in v3.0.0. See [Migration Guide](./migration/old-to-new.md) for upgrade instructions.
```

**In CLI/Logs:**

```bash
$ mycelix old-command

⚠️  WARNING: 'old-command' is deprecated and will be removed in v3.0.0.
Use 'new-command' instead.
See: https://docs.mycelix.org/migration/commands

[command still executes normally]
```

### 3. Migration Guide

**Create Comprehensive Guide:**

```markdown
# Migration Guide: OldFunction → NewFunction

## Quick Summary

Replace:
```python
result = old_function(data)
```

With:
```python
result = new_function(data)
```

## Why This Change?

[Brief explanation of improvements in new approach]

## Detailed Migration

### Step 1: Update Function Calls

**Before:**
```python
from mycelix import old_function

result = old_function(
    data=my_data,
    option=True
)
```

**After:**
```python
from mycelix import new_function

result = new_function(
    data=my_data,
    enhanced_mode=True  # 'option' renamed to 'enhanced_mode'
)
```

### Step 2: Update Error Handling

[Any changes to exceptions or error handling]

### Step 3: Test Your Changes

```python
# Add this test to verify migration
def test_migrated_to_new_function():
    result = new_function(test_data)
    assert result.success
```

## Breaking Changes

- `option` parameter renamed to `enhanced_mode`
- Return type changed from `dict` to `Result` object
- Exception changed from `ValueError` to `ValidationError`

## Compatibility Shim (Temporary)

If you need time to migrate, use this shim:

```python
def old_function(data, option=False):
    """Temporary shim - remove before v3.0.0"""
    return new_function(data, enhanced_mode=option)
```

## Help Available

- Questions? [GitHub Discussions](link)
- Found a bug in migration guide? [Open an issue](link)
- Need assistance? [Office hours](link)

## Timeline

- v2.1.0+ : Deprecated, warnings shown
- v3.0.0 (Jan 2026): Removed

Migrate before v3.0.0 to avoid breaking changes.
```

### 4. Ongoing Communication

**Every Release in Deprecation Period:**

Include in release notes:
```markdown
## Deprecation Reminders

- **`old_function`** will be removed in v3.0.0 (4 releases away).
  See [Migration Guide](link).
```

**Escalating Warnings:**

```python
# v2.1.0 - Initial deprecation
warnings.warn("old_function is deprecated", DeprecationWarning)

# v2.5.0 - Emphasize upcoming removal (6 months out)
warnings.warn(
    "old_function is deprecated and will be REMOVED in v3.0.0 (Jan 2026). "
    "Please migrate to new_function soon.",
    DeprecationWarning
)

# v2.9.0 - Final warning (1 release before removal)
warnings.warn(
    "FINAL WARNING: old_function will be REMOVED in the next release (v3.0.0). "
    "Migrate to new_function now: https://docs/migration",
    FutureWarning  # Shows by default, not just for developers
)

# v3.0.0 - Removed
# Function no longer exists
```

### 5. Removal Announcement

**In v3.0.0 Release Notes:**

```markdown
## v3.0.0 - 2026-01-15

### Breaking Changes

- **REMOVED: `old_function`** - Deprecated since v2.1.0 (Mar 2025).
  Use `new_function` instead. If you haven't migrated yet, see:
  https://docs.luminous-dynamics.org/migration/v2-to-v3

[Include migration guide link prominently]
```

---

## 🛠️ Migration Support Tools

### Automated Migration Scripts

When possible, provide migration tooling:

```bash
# Example: Automated code updater
$ mycelix migrate --from=2.9 --to=3.0 ./my_project/

Scanning for deprecated API usage...
Found 15 instances of old_function

Migrating:
✓ src/main.py:45 - Replaced old_function with new_function
✓ src/utils.py:23 - Replaced old_function with new_function
...

Migration complete! Review changes and test thoroughly.
```

### Compatibility Layers (Temporary)

For complex migrations, consider temporary compatibility:

```python
# v2.1-2.9: Provide backward compatibility
def old_function(*args, **kwargs):
    """Compatibility shim - will be removed in v3.0."""
    warnings.warn("old_function is deprecated", DeprecationWarning)
    # Translate old API to new API
    return new_function(*transform_args(args, kwargs))
```

**Important:** Compatibility layers are temporary and will be removed!

---

## 📦 Project Archival vs Deprecation

### When to Archive Entire Projects

**Archive When:**
- No active maintenance for >1 year
- Fundamental approach superseded (e.g., new protocol replaces old)
- Security issues can't be addressed
- Incompatible with ecosystem evolution

**Don't Archive If:**
- Still has active users (find new maintainer instead)
- Just needs maintenance (find contributors)
- Personal bandwidth issue (recruit help)

### Archival Process

**1. Announcement (3+ months before archival)**

```markdown
# Proposal: Archive [Project Name]

## Context

[Explain why archival is being considered]

## Current State

- Last active development: [Date]
- Current users: [Known usage]
- Alternatives: [Other projects that serve this use case]

## We Need Your Input

- Do you use this project? How?
- Would you be interested in maintaining it?
- What would you need to migrate?

**Feedback period: Next 30 days**
```

**2. Seek New Maintainer**

Before archiving, actively look for someone to take it over:
- Post in GitHub Discussions
- Reach out to active contributors
- Ask in community channels
- Consider transferring to interested party

**3. Archive Repository (After feedback period)**

- Update README with archive notice
- Add banner to documentation
- Set repository to archived mode (read-only)
- Keep available (don't delete)

**Archived Repository README:**

```markdown
# ⚠️ This Repository is Archived

This project is no longer actively maintained as of [Date].

## Why Archived?

[Brief explanation]

## Alternatives

We recommend:
- [Alternative Project 1](link) - [Why it's a good alternative]
- [Alternative Project 2](link) - [Why it's a good alternative]

## Forking

This code remains available under [LICENSE]. You're welcome to fork and
continue development.

If you'd like to become the official maintainer, please reach out:
[contact info]

## Historical Context

[Brief description of what this project accomplished]

---

**Thank you to all contributors and users who made this project possible.** 💚
```

---

## 🤝 Handling User Pushback

### Listen First

When users object to deprecation:
1. **Understand their use case** - Why do they need this feature?
2. **Look for alternatives** - Can new approach serve their needs?
3. **Assess impact** - How many users are affected?
4. **Consider extension** - Can we extend timeline if many affected?

### Possible Outcomes

**1. Proceed with Deprecation (Most Common)**
```markdown
Thank you for the feedback. We understand this change impacts your workflow.

After considering the concerns raised, we're proceeding with deprecation because
[reasons]. However, we're extending the timeline to 12 months (instead of 6)
to give more time for migration.

We're also:
- Creating additional migration examples for your use case
- Offering office hours for migration help
- Documenting the workaround you suggested

We're committed to supporting you through this transition.
```

**2. Postpone or Cancel Deprecation**
```markdown
Thank you for the detailed feedback. You've highlighted use cases we hadn't
fully considered.

Given the impact on [X many] users and lack of clear migration path for
[specific use case], we're **canceling** this deprecation for now.

Instead, we'll:
- Maintain current API alongside new one
- Revisit deprecation in v4.0 after improving alternatives
- Document both approaches and when to use each

We'll update the proposal accordingly.
```

**3. Offer Alternative Solution**
```markdown
Thanks for raising this concern. We understand you rely on [feature] for
[use case].

Rather than maintaining the deprecated API, we can offer:
- Plugin/extension mechanism for your use case
- Fork the code into a separate package you maintain
- Consulting help to build custom solution

Would any of these work for you? Let's discuss the best path forward.
```

---

## 📝 Deprecation Checklist

### For Feature/API Deprecation

- [ ] Discuss with team (is this the right decision?)
- [ ] Document reasoning in ADR
- [ ] Create proposal in GitHub Discussions
- [ ] Gather user feedback (2-4 weeks)
- [ ] Create migration guide
- [ ] Add deprecation warnings to code
- [ ] Update documentation (mark as deprecated)
- [ ] Include in release notes
- [ ] Announce in community channels (Discord, email, blog)
- [ ] Maintain throughout deprecation period (6-12 months)
- [ ] Escalate warnings as removal approaches
- [ ] Remove in next MAJOR version
- [ ] Update documentation (remove deprecated content)
- [ ] Include removal in release notes with migration link

### For Project Archival

- [ ] Announce intention (3+ months before)
- [ ] Seek new maintainer
- [ ] Gather community feedback
- [ ] Make final decision (document in ADR)
- [ ] Update README with archive notice
- [ ] Add documentation banner
- [ ] Archive repository on GitHub
- [ ] Announce archival
- [ ] Remain available for questions (6 months)

---

## 💚 Conscious Deprecation

### Honor What Was

Every deprecated feature once served users:
- Acknowledge the value it provided
- Thank contributors who built it
- Celebrate what it enabled
- Document its legacy

**In Announcement:**
```markdown
## Honoring OldFeature

OldFeature served our community well for 3 years:
- Used by 1,000+ users
- Enabled 50+ research projects
- Taught us valuable lessons about [X]

While we're moving forward with NewFeature, we're grateful for what
OldFeature contributed to the ecosystem.

Thank you to @original_author and the 15 contributors who built and
maintained it. 💚
```

### Support Users Through Transition

Deprecation is disruptive for users:
- Provide clear, kind communication
- Offer help and support (office hours, consulting)
- Be available to answer questions
- Acknowledge the burden on users

### Learn and Document

Every deprecation teaches us:
- What to do differently next time
- Patterns to avoid
- Patterns to embrace
- User needs we missed

**In Post-Deprecation ADR:**
```markdown
## Lessons from Deprecating OldFeature

### What Went Well
- Migration guide was comprehensive
- 12-month timeline gave users enough time
- Early communication prevented surprises

### What We'd Improve
- Could have provided automated migration script
- Should have involved major users earlier
- Could have been clearer about "why" upfront

### Applying These Lessons
- Future deprecations will include migration tooling budget
- We'll consult with top 10 users before finalizing deprecation
- We'll lead announcements with reasoning, not just mechanics
```

---

## 📚 Related Resources

- **[RELEASES.md](./RELEASES.md)** - Release process and SemVer
- **[ADR.md](./ADR.md)** - Document deprecation decisions
- **[COMMUNICATION.md](./COMMUNICATION.md)** - How to communicate changes
- **[GOVERNANCE.md](./GOVERNANCE.md)** - Decision-making process

---

## 💬 Questions?

- **Proposing a deprecation**: [GitHub Discussions](https://github.com/orgs/Luminous-Dynamics/discussions)
- **Migration help**: Office hours (see [COMMUNICATION.md](./COMMUNICATION.md))
- **Suggest policy improvements**: Open PR on this document

---

**Last Updated**: 2025-01-14
**Maintained by**: Engineering Working Group

---

> "Endings are as sacred as beginnings. May we sunset features with the same care and consciousness we brought to creating them." 💚
