# Security Policy

## Reporting a Vulnerability

The Luminous Dynamics team takes security vulnerabilities seriously. We appreciate your efforts to responsibly disclose your findings and will make every effort to acknowledge your contributions.

### How to Report

**Please DO NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to:

**tristan.stoltz@evolvingresonantcocreationism.com**

Include the following information in your report:

- **Type of vulnerability** (e.g., SQL injection, XSS, authentication bypass)
- **Location** - Full paths of affected source files
- **Steps to reproduce** - Step-by-step instructions to reproduce the issue
- **Proof of concept** - Code or commands demonstrating the vulnerability
- **Impact** - What an attacker could achieve by exploiting this vulnerability
- **Suggested fix** (optional) - If you have ideas on how to fix it

### What to Expect

1. **Acknowledgment** - We will acknowledge receipt of your report within 48 hours
2. **Assessment** - We will assess the vulnerability and determine its severity
3. **Communication** - We will keep you informed of our progress
4. **Fix** - We will develop and test a fix
5. **Release** - We will release the fix and publish a security advisory
6. **Credit** - We will credit you in the security advisory (unless you prefer anonymity)

### Response Timeline

- **Initial response**: Within 48 hours
- **Status update**: Within 7 days
- **Fix timeline**: Depends on severity
  - Critical: Within 7 days
  - High: Within 14 days
  - Medium: Within 30 days
  - Low: Within 90 days

## Supported Versions

We provide security updates for the following versions:

| Project | Version | Supported |
|---------|---------|-----------|
| Terra Atlas | Latest | :white_check_mark: |
| Luminous Nix | 0.8.x | :white_check_mark: |
| Luminous Nix | < 0.8.0 | :x: |
| Mycelix-Core | Latest | :white_check_mark: |

**Note**: We recommend always using the latest version of our software.

## Security Update Process

1. **Discovery** - Vulnerability is reported or discovered
2. **Triage** - Team assesses severity and impact
3. **Development** - Fix is developed in a private branch
4. **Testing** - Fix is thoroughly tested
5. **Release** - Fix is released with a new version
6. **Advisory** - Security advisory is published on GitHub
7. **Notification** - Users are notified through release notes

## Security Best Practices

### For Users

- **Keep software updated** - Always use the latest version
- **Use secure connections** - Always use HTTPS
- **Protect credentials** - Never commit secrets to repositories
- **Review dependencies** - Regularly audit third-party dependencies

### For Contributors

- **No hardcoded secrets** - Use environment variables or secret managers
- **Input validation** - Validate and sanitize all user input
- **Dependency scanning** - Check for known vulnerabilities in dependencies
- **Code review** - All changes must be reviewed before merging
- **Least privilege** - Request only necessary permissions

## Scope

This security policy applies to:

- All repositories in the Luminous-Dynamics GitHub organization
- All official releases and distributions
- The main monorepo at `luminous-dynamics/luminous-dynamics`
- All standalone project repositories

### Out of Scope

The following are NOT covered by this policy:

- Third-party services we integrate with
- User-deployed instances with custom modifications
- Vulnerabilities in dependencies (report these to the dependency maintainers)
- Social engineering attacks
- Physical security
- Denial of service attacks

## Bug Bounty

We currently do not have a formal bug bounty program. However, we deeply appreciate security researchers who take the time to report vulnerabilities responsibly. We will:

- Acknowledge your contribution publicly (with your permission)
- Provide a letter of recognition
- Include you in our security hall of fame

## Security Contacts

**Primary Contact**: tristan.stoltz@evolvingresonantcocreationism.com

For general security questions that are not vulnerability reports, you may also open a GitHub Discussion in the relevant repository.

## PGP Key

If you need to encrypt sensitive information, please request our PGP public key via email.

## Acknowledgments

We would like to thank the following security researchers for their responsible disclosures:

*This list will be updated as we receive and resolve security reports.*

---

Thank you for helping keep Luminous Dynamics and our users safe!
