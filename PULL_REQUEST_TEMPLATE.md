# Pull Request

## Description

<!--
Provide a clear and concise description of what this PR does.
Explain the motivation and context for these changes.
-->



## Related Issues

<!--
Link any related issues using GitHub's closing keywords.
Examples: Closes #123, Fixes #456, Relates to #789
-->

- Closes #
- Related to #

## Type of Change

<!-- Check all that apply -->

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Performance improvement
- [ ] Code refactoring (no functional changes)
- [ ] Documentation update
- [ ] Test coverage improvement
- [ ] CI/CD or build changes
- [ ] Security fix
- [ ] Dependency update

## Component(s) Affected

<!-- Check all that apply -->

- [ ] Core
- [ ] Identity
- [ ] Marketplace
- [ ] Mail
- [ ] Governance
- [ ] CLI
- [ ] Tests
- [ ] Documentation
- [ ] CI/CD
- [ ] Other: <!-- specify -->

## Testing

### Test Coverage

<!-- Describe the tests you've added or modified -->

- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] End-to-end tests added/updated
- [ ] Manual testing performed

### Testing Checklist

<!-- Complete this checklist to confirm testing -->

- [ ] All existing tests pass (`cargo test`)
- [ ] New tests pass for added functionality
- [ ] Code compiles without warnings (`cargo build`)
- [ ] Linting passes (`cargo clippy`)
- [ ] Code is formatted (`cargo fmt --check`)

### Test Instructions

<!--
Provide specific instructions for reviewers to test your changes.
Include any setup steps, test commands, or scenarios to verify.
-->

```bash
# Example test commands
cargo test --package mycelix-core
cargo run -- <specific command to test>
```

## Documentation

- [ ] Documentation has been updated (if applicable)
- [ ] Code comments have been added/updated
- [ ] CHANGELOG.md has been updated (if applicable)
- [ ] API documentation is up to date

## Breaking Changes

<!--
If this PR includes breaking changes, describe them here.
Include migration instructions for users.
-->

### Breaking Changes Description

<!-- Delete this section if there are no breaking changes -->

N/A

### Migration Guide

<!--
If applicable, provide step-by-step migration instructions.
Delete this section if there are no breaking changes.
-->

N/A

## Security Considerations

<!--
Describe any security implications of these changes.
Has this been reviewed for common vulnerabilities?
-->

- [ ] No security implications
- [ ] Security review requested
- [ ] Security considerations documented below:

<!-- Add security notes here if applicable -->

## Performance Impact

<!--
Describe any performance implications of these changes.
Include benchmark results if available.
-->

- [ ] No performance impact expected
- [ ] Performance improved (include benchmarks)
- [ ] Performance may be affected (explain below)

<!-- Add performance notes here if applicable -->

## Screenshots / Recordings

<!--
If applicable, add screenshots or recordings to demonstrate the changes.
Especially useful for UI changes or complex behaviors.
-->

## Checklist

<!-- Final checklist before requesting review -->

- [ ] My code follows the project's coding style and guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published
- [ ] I have updated the documentation accordingly
- [ ] I have read the [CONTRIBUTING.md](../CONTRIBUTING.md) guidelines

## Additional Notes

<!--
Any additional information that reviewers should know.
Context, design decisions, trade-offs, future improvements, etc.
-->

---

<!--
Thank you for contributing to Mycelix!
A maintainer will review your PR as soon as possible.
-->
