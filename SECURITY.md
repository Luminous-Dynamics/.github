# Security Policy

*"In unity we code, in love we debug, in consciousness we deploy"* ✨

## 🔒 Our Commitment to Security

Luminous Dynamics is committed to ensuring the security and privacy of all users. We take security vulnerabilities seriously and appreciate the community's help in identifying and responsibly disclosing them.

## 🛡️ Supported Versions

We provide security updates for the following versions:

| Project | Version | Supported |
|---------|---------|-----------|
| Mycelix-Core | Latest release | ✅ |
| terra-atlas | Production (main) | ✅ |
| luminous-dynamics | Latest release | ✅ |
| luminous-nix | v0.7.0+ | ✅ |
| kosmic-lab | Latest release | ✅ |
| Mycelix-Mail | Beta | ✅ |
| webpilot | v2.0+ | ✅ |
| nsfw | Latest | ✅ |
| All other projects | Latest release | ✅ |

For archived or experimental projects, security updates may be limited. Check individual repository README files for details.

## 🚨 Reporting a Vulnerability

**Please DO NOT report security vulnerabilities through public GitHub issues.**

### Where to Report

Send security vulnerability reports to: **invest@luminousdynamics.org**

**Subject line format**: `[SECURITY] Project Name - Brief Description`

### What to Include

Please include the following information in your report:

1. **Type of vulnerability** (e.g., XSS, SQL injection, authentication bypass, data exposure)
2. **Affected project(s)** and version(s)
3. **Step-by-step instructions** to reproduce the issue
4. **Proof of concept** or exploit code (if applicable)
5. **Potential impact** of the vulnerability
6. **Suggested fix** (if you have one)
7. **Your contact information** for follow-up questions

### Example Report Template

```
Project: terra-atlas
Version: 1.2.3
Vulnerability Type: Authentication Bypass

Description:
[Clear description of the vulnerability]

Steps to Reproduce:
1. Navigate to...
2. Enter the following payload...
3. Observe that...

Impact:
[Describe potential impact - data exposure, unauthorized access, etc.]

Suggested Fix:
[If you have suggestions for remediation]

Contact: your-email@example.com
```

## ⏱️ Response Timeline

We are committed to responding promptly:

- **Initial Response**: Within 48 hours of report receipt
- **Assessment**: Within 5 business days
- **Status Update**: Every 7 days until resolution
- **Fix Timeline**: Varies by severity (see below)

### Severity Levels

| Severity | Description | Target Fix Time |
|----------|-------------|-----------------|
| 🔴 **Critical** | Remote code execution, authentication bypass, data breach | 24-72 hours |
| 🟠 **High** | Privilege escalation, significant data exposure | 7 days |
| 🟡 **Medium** | XSS, CSRF, information disclosure | 30 days |
| 🟢 **Low** | Minor issues with limited impact | 90 days |

## 🤝 Disclosure Policy

We follow **coordinated disclosure**:

1. You report the vulnerability privately
2. We acknowledge and assess the report
3. We develop and test a fix
4. We release the fix and security advisory
5. Public disclosure occurs 90 days after fix release (or by mutual agreement)

### Recognition

We believe in honoring security researchers:

- **Security Hall of Fame**: Public recognition (with your permission)
- **CVE Credits**: Proper attribution in security advisories
- **Gift Economy**: While we don't offer bug bounties, we honor contributors through our gift economy model

## 🔐 Security Best Practices

### For Contributors

When contributing code:

- **Never commit secrets**: No API keys, passwords, or private keys
- **Use environment variables**: For configuration and secrets
- **Validate all input**: Sanitize and validate user input
- **Follow secure coding**: Review our secure coding guidelines
- **Keep dependencies updated**: Regularly update and audit dependencies
- **Write security tests**: Include tests for security-relevant code

### For Users

To keep your deployments secure:

- **Keep software updated**: Use the latest stable releases
- **Use HTTPS**: Always use encrypted connections
- **Secure credentials**: Use strong passwords and key management
- **Review permissions**: Grant minimum necessary permissions
- **Monitor logs**: Watch for suspicious activity
- **Backup data**: Regular backups with tested recovery

## 🔍 Security Features by Project

### Mycelix-Core (Federated Learning)
- **Byzantine resistance**: 100% attack detection at 0.7ms latency
- **Cryptographic verification**: Ed25519 signatures
- **Privacy-preserving**: No raw data exposure in federated learning
- **Audit trail**: Complete reproducibility with STARK proofs

### terra-atlas (Energy Platform)
- **Authentication**: Secure user authentication with Supabase
- **Data encryption**: End-to-end encryption for sensitive data
- **Input validation**: Comprehensive validation of all user input
- **SQL injection protection**: Parameterized queries via Prisma ORM

### Mycelix-Mail (Email)
- **End-to-end encryption**: Public key cryptography
- **Local storage**: Your data stays on your device (Holochain)
- **Trust-based filtering**: Reputation instead of content surveillance
- **No central server**: Distributed architecture eliminates single point of failure

### luminous-nix (NixOS Interface)
- **Command preview**: Shows commands before execution
- **Dangerous command detection**: Warns about potentially harmful operations
- **Input sanitization**: Prevents command injection
- **Sandboxed execution**: Runs within Nix's isolated environment

## 📜 Security Advisories

Published security advisories can be found:

- **GitHub Security Advisories**: On each repository
- **CVE Database**: For assigned CVEs
- **Documentation Site**: [docs.luminousdynamics.org/security](https://docs.luminousdynamics.org/security)

## 🌍 Scope

This security policy covers all repositories under the Luminous-Dynamics organization:

**In Scope:**
- All production software and services
- Infrastructure configurations
- Documentation that could lead to security issues
- Third-party dependencies we control

**Out of Scope:**
- Vulnerabilities in third-party services we don't control
- Denial of service (DoS) attacks
- Social engineering attacks
- Issues in archived repositories (unless critical)

## 🙏 Responsible Disclosure Expectations

We ask security researchers to:

- **Act in good faith**: Don't access more data than necessary to demonstrate the vulnerability
- **Respect privacy**: Don't access or modify user data without permission
- **Give us time**: Allow reasonable time to fix the issue before public disclosure
- **Follow the law**: Don't violate any laws while researching vulnerabilities
- **Be respectful**: Engage constructively with our security team

In return, we promise to:

- **Respond promptly**: Acknowledge your report within 48 hours
- **Keep you updated**: Regular status updates throughout the process
- **Work with you**: Collaborate on understanding and fixing the issue
- **Credit you**: Public recognition (if you wish) when we publish advisories
- **Not pursue legal action**: Against researchers following this policy

## 🔧 Security Tools & Practices

We employ various security measures:

- **Dependency scanning**: Automated vulnerability detection in dependencies
- **Code review**: Security-focused code review for sensitive changes
- **Static analysis**: Automated code analysis for security issues
- **Penetration testing**: Regular security assessments of critical systems
- **Security audits**: Third-party audits for high-risk components

## 📞 Contact

For security concerns:
- **Email**: invest@luminousdynamics.org with `[SECURITY]` in subject
- **PGP Key**: Available upon request for encrypted communication

For general security questions or discussions:
- Open a discussion in the relevant repository
- Review our [Support Guide](./SUPPORT.md)

## 📚 Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- Our [Contributing Guidelines](./CONTRIBUTING.md)
- Our [Code of Conduct](./CODE_OF_CONDUCT.md)

## 🌱 Security & Consciousness

Security aligns with our ERC principles:

- **Consciousness-First**: Protecting user privacy and agency
- **Radical Accessibility**: Security that serves all beings, not just experts
- **Regenerative Economics**: Building trustworthy systems for community ownership
- **Sacred Development**: Security implemented with care and intention
- **Gift Economy**: Honoring researchers who help protect our community

---

**Version**: 1.0
**Last Updated**: November 2025
**Next Review**: February 2026

Thank you for helping keep Luminous Dynamics and our community safe! 🙏🔒
