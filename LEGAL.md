# ⚖️ Legal Guide

> "Legal compliance is not bureaucracy—it's care. We protect our users, our contributors, and our mission through thoughtful legal practices."

This document provides guidance on legal compliance, licensing, intellectual property, and data privacy for Luminous Dynamics projects.

---

## 🎯 Legal Philosophy

### Core Principles

1. **Transparency First**
   - Clear licensing on every project
   - Public documentation of legal decisions
   - No hidden terms or surprise restrictions

2. **User Protection**
   - Privacy by design
   - Data minimization
   - User rights respected
   - Clear terms of service

3. **Contributor Protection**
   - Clear IP assignment
   - No copyright surprises
   - Recognition of contributions
   - Fair and equitable treatment

4. **Compliance as Care**
   - GDPR, CCPA, and privacy laws protect users
   - Licensing protects open source commons
   - Legal clarity prevents disputes

5. **When In Doubt, Consult**
   - Not legal advice (we're engineers, not lawyers)
   - Complex issues → professional legal counsel
   - Better safe than sorry

---

## 📜 Licensing Framework

### Our Primary License: AGPL-3.0

**All Luminous Dynamics code is licensed under:**
```
GNU Affero General Public License v3.0 (AGPL-3.0)
```

**Why AGPL-3.0?**
- **Strong Copyleft**: Modifications must be shared
- **Network Provision**: SaaS deployments must share source
- **Consciousness-First Aligned**: Prevents proprietary capture
- **Community Protection**: Ensures code remains open

**AGPL-3.0 Requirements:**
- Source code must include LICENSE file
- All modifications must be released under AGPL-3.0
- Network services using the code must provide source
- Copyright and license notices must be preserved

### License Compatibility

**✅ Compatible Licenses (Can Include in AGPL Projects):**
- MIT
- BSD (2-clause, 3-clause)
- Apache 2.0
- GPL-2.0, GPL-3.0
- LGPL-2.1, LGPL-3.0
- Public Domain / CC0

**❌ Incompatible Licenses (Cannot Include):**
- Proprietary/closed source
- Commons Clause
- SSPL (Server Side Public License)
- Most "source available" licenses

**⚠️ Check Carefully:**
- Creative Commons licenses (depends on variant)
- Custom open source licenses
- Dual-licensed code (check terms)

### License Notices

**Every Source File:**
```python
# Copyright (C) 2025 Luminous Dynamics
#
# This file is part of [Project Name].
#
# [Project Name] is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# [Project Name] is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with [Project Name]. If not, see <https://www.gnu.org/licenses/>.
```

**README.md:**
```markdown
## License

This project is licensed under the GNU Affero General Public License v3.0.
See [LICENSE](./LICENSE) for full text.

**Summary**: You're free to use, modify, and distribute this software,
but any modifications (including SaaS deployments) must be shared under
the same license.
```

### Dual Licensing (If Needed)

**For Library Code** (not main projects):
Consider dual licensing under AGPL-3.0 + permissive (MIT/Apache):
- AGPL-3.0 by default
- Commercial license available for proprietary use (generates revenue)
- Requires legal counsel to set up properly

---

## 🏛️ Intellectual Property

### Copyright

**Who Owns the Code?**
- **Contributors retain copyright** to their contributions
- **No copyright assignment required**
- All code licensed under AGPL-3.0 to Luminous Dynamics

**Copyright Notices:**
```
Copyright (C) 2025 Luminous Dynamics and contributors
```

**Significant Contributors:**
Can add themselves to copyright:
```
Copyright (C) 2025 Luminous Dynamics and contributors
Copyright (C) 2025 Alice Smith <alice@example.com>
```

### Contributor License Agreement (CLA)

**We do NOT require a CLA**, but we do require:

**Developer Certificate of Origin (DCO):**
- Sign commits with `git commit -s`
- Certifies you have right to contribute
- Simpler and more contributor-friendly than CLA

**DCO Text:**
```
Developer Certificate of Origin
Version 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

**Enforcing DCO:**
```yaml
# .github/workflows/dco.yml
name: DCO Check
on: [pull_request]

jobs:
  dco:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: DCO Check
        uses: tim-actions/dco@v1.1.0
```

### Trademarks

**"Luminous Dynamics" and Project Names:**
- Trademarks belong to organization
- Use in good faith allowed (open source projects, discussions)
- Commercial use requires permission
- Preventing confusion and brand dilution

**Trademark Policy:**
```markdown
You may use our trademarks to:
✅ Refer to our projects accurately
✅ Link to our projects
✅ Describe compatibility ("works with Mycelix")

You may NOT:
❌ Imply official endorsement without permission
❌ Create confusingly similar names
❌ Use in domain names without permission
❌ Modify our logos
```

### Patents

**Patent Grant:**
AGPL-3.0 includes implicit patent grant:
- Contributors grant patent licenses for their contributions
- Protects users from patent claims
- Terminated if user sues over patents

**Defensive Patent Strategy:**
- We will not sue over patents except defensively
- If sued, we terminate patent license to aggressor
- Protects open source commons

---

## 🔒 Privacy & Data Protection

### GDPR Compliance (EU)

**If you collect user data, you MUST:**

**1. Legal Basis:**
- Consent (explicit opt-in)
- Contract (necessary for service)
- Legitimate interest (documented)

**2. User Rights:**
- **Right to Access**: Provide data upon request
- **Right to Rectification**: Allow data corrections
- **Right to Erasure**: Delete data upon request ("right to be forgotten")
- **Right to Portability**: Export data in machine-readable format
- **Right to Object**: Stop processing for specific purposes

**3. Data Processing Requirements:**
- **Data Minimization**: Collect only what's needed
- **Purpose Limitation**: Use data only for stated purposes
- **Storage Limitation**: Delete when no longer needed
- **Security**: Appropriate technical and organizational measures

**4. Notifications:**
- **Privacy Policy**: Clear explanation of data practices
- **Data Breach**: Notify within 72 hours
- **DPO**: Appoint if processing at scale

### CCPA Compliance (California)

**California Consumer Privacy Act requirements:**
- Disclose data collection and use
- Allow users to opt-out of data sales
- Don't discriminate against users who opt-out
- Provide data deletion upon request

### Privacy-First Design

**Best Practices:**

**1. Collect Minimal Data:**
```python
# ❌ Bad: Collect everything
user_data = {
    'email': email,
    'name': name,
    'age': age,
    'location': location,
    'ip_address': ip,
    'device_fingerprint': fingerprint,
    # ... etc
}

# ✅ Good: Collect only what's needed
user_data = {
    'email': email,  # Required for account
    'username': username,  # Required for display
}
```

**2. Anonymous by Default:**
```python
# Allow anonymous usage where possible
federation = create_federation(
    name="research-project",
    anonymous=True,  # No user accounts required
)
```

**3. Local Processing:**
```python
# Mycelix: Data never leaves user devices
federation.train(
    model=model,
    privacy_mode="local-only",  # All computation local
)
```

**4. Encryption:**
```python
# Encrypt sensitive data at rest
encrypted_data = encrypt(
    data=user_data,
    key=user_key,  # Only user has key
)
```

**5. Retention Limits:**
```python
# Auto-delete old data
def cleanup_old_sessions():
    cutoff = datetime.now() - timedelta(days=90)
    Session.query.filter(Session.last_accessed < cutoff).delete()
```

### Privacy Policy Template

```markdown
# Privacy Policy for [Project Name]

**Last Updated**: [Date]

## What Data We Collect

We collect minimal data to provide our service:
- **Account Data**: Email address and username (if you create account)
- **Usage Data**: Anonymous analytics (page views, feature usage)
- **Technical Data**: IP address (for security, not stored long-term)

## How We Use Data

- Provide and improve our service
- Communicate about your account (if you opt-in)
- Prevent abuse and ensure security

## Data Sharing

We do NOT:
- Sell your data (ever)
- Share with advertisers
- Use for purposes beyond stated above

We MAY share with:
- Service providers (hosting, email) under strict privacy agreements
- Law enforcement (if legally required)

## Your Rights

You can:
- Access your data: [email/process]
- Correct your data: [email/process]
- Delete your data: [email/process]
- Export your data: [email/process]

## Data Retention

- Account data: Until you delete account
- Usage data: 90 days
- Logs: 30 days

## Security

We use industry-standard security practices:
- Encryption in transit (HTTPS)
- Encryption at rest
- Regular security audits
- Minimal data collection

## Changes

We'll notify you of privacy policy changes via [email/notification].

## Contact

Privacy questions: privacy@luminous-dynamics.org
```

---

## 📋 Terms of Service

**For Services (Terra Atlas, etc.):**

```markdown
# Terms of Service for [Service Name]

**Last Updated**: [Date]

## Acceptance

By using [Service], you agree to these terms.

## Use of Service

You may:
✅ Use for lawful purposes
✅ Use for research and education
✅ Share and collaborate

You may NOT:
❌ Violate laws or others' rights
❌ Abuse or attack the service
❌ Impersonate others
❌ Scrape without permission

## User Content

- You retain ownership of your content
- You grant us license to host/display your content
- You're responsible for your content

## Our Content

- All code is open source (AGPL-3.0)
- Documentation is CC-BY-SA 4.0
- Trademarks remain our property

## Privacy

See our [Privacy Policy](link).

## Termination

We may terminate accounts that violate these terms.
You may delete your account anytime.

## Disclaimer

Service provided "as is" without warranties.
We're not liable for data loss or service interruptions.

(See AGPL-3.0 license for full disclaimer)

## Disputes

- Governed by [jurisdiction] law
- Informal resolution first
- Arbitration if needed

## Changes

We'll notify you 30 days before changes.
Continued use = acceptance.

## Contact

Legal questions: legal@luminous-dynamics.org
```

---

## ⚠️ Legal Risk Management

### Common Legal Risks

**1. Copyright Infringement**
- **Risk**: Including code you don't have rights to
- **Prevention**:
  - Only use open source or original code
  - Check license compatibility
  - Require DCO on all contributions

**2. Patent Infringement**
- **Risk**: Implementing patented algorithms
- **Prevention**:
  - Research patents before implementing
  - Use defensive patent clauses (AGPL includes this)
  - Avoid submarine patents

**3. Trademark Issues**
- **Risk**: Using others' trademarks
- **Prevention**:
  - Search before naming projects
  - Don't use company names without permission
  - Respect nominative fair use

**4. Data Privacy Violations**
- **Risk**: Mishandling user data
- **Prevention**:
  - Privacy by design
  - GDPR/CCPA compliance
  - Regular privacy audits

**5. Terms of Service Violations**
- **Risk**: Violating third-party ToS (APIs, platforms)
- **Prevention**:
  - Read ToS before integrating
  - Monitor for ToS changes
  - Have alternatives ready

### When to Consult a Lawyer

**Definitely consult legal counsel for:**
- ✅ Significant partnership agreements
- ✅ Dual licensing strategies
- ✅ Patent concerns
- ✅ Trademark registration
- ✅ Legal threats or disputes
- ✅ Regulatory compliance questions
- ✅ Fundraising or investment terms

**Probably fine to handle yourself:**
- Standard AGPL-3.0 licensing
- Basic privacy policy (use templates)
- Standard contributor agreements (DCO)
- Routine open source activities

### Legal Resources

**Free/Low-Cost Legal Help:**
- **Software Freedom Law Center**: https://softwarefreedom.org/
- **EFF (Electronic Frontier Foundation)**: https://www.eff.org/
- **Open Source Initiative**: https://opensource.org/
- **SFLC Legal Guides**: Free resources for open source projects

**Pro Bono Programs:**
- Many law firms offer pro bono for open source
- Tech law clinics at law schools
- Bar association referrals

---

## 📚 Related Resources

- **[GOVERNANCE.md](./GOVERNANCE.md)** - Decision-making and authority
- **[SECURITY.md](./SECURITY.md)** - Security vulnerability handling
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - Contributor agreements (DCO)
- **[SUSTAINABILITY.md](./SUSTAINABILITY.md)** - Funding and revenue models

---

## 💬 Legal Questions?

- **General legal questions**: legal@luminous-dynamics.org
- **Privacy concerns**: privacy@luminous-dynamics.org
- **License compatibility**: Ask in [GitHub Discussions](link)

---

## ⚠️ Disclaimer

**This document is informational, not legal advice.**

For legal advice specific to your situation, consult a qualified attorney licensed in your jurisdiction.

Luminous Dynamics provides this information to help navigate common legal issues in open source, but we are not lawyers and this is not a substitute for professional legal counsel.

---

**Last Updated**: 2025-01-14
**Maintained by**: Legal Working Group (with attorney consultation)

---

> "Legal protection serves our mission. Clear, fair legal practices let us focus on building consciousness-first technology that serves all." 💚
