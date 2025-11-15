# 🔐 Data Privacy

> "Privacy is not something that I'm merely entitled to, it's an absolute prerequisite." — Marlon Brando

*Last updated: January 2025*

This document outlines our **data privacy philosophy and practices**—how we respect user privacy, comply with global privacy laws (GDPR, CCPA, etc.), implement privacy by design, and handle personal data responsibly across our projects and services.

---

## 🎯 Privacy Philosophy

### Why Privacy Matters

**Privacy is a fundamental human right**:
- Users deserve control over their data
- Data breaches have real consequences
- Trust is hard to earn, easy to lose
- Privacy and security go hand-in-hand
- Ethical obligation beyond legal compliance

### Privacy Principles

1. **Data minimization**: Collect only what you need
2. **Purpose limitation**: Use data only for stated purposes
3. **Transparency**: Be clear about what you collect and why
4. **User control**: Let users access, modify, and delete their data
5. **Security**: Protect data from unauthorized access
6. **Privacy by design**: Build privacy in from the start, not as an afterthought
7. **Accountability**: Take responsibility for data handling

---

## 📜 Privacy Regulations

### GDPR (General Data Protection Regulation)

**Applies to**: EU residents, regardless of where your company is located

**Key requirements**:
- **Lawful basis**: Have legal justification for processing (consent, contract, legitimate interest)
- **Consent**: Must be freely given, specific, informed, and unambiguous
- **Right to access**: Users can request their data
- **Right to erasure**: "Right to be forgotten"
- **Data portability**: Users can export their data
- **Breach notification**: Report breaches within 72 hours
- **Privacy by design**: Build privacy into systems
- **Data Protection Officer (DPO)**: Required for large-scale processing

**Penalties**: Up to €20M or 4% of global revenue (whichever is higher)

### CCPA (California Consumer Privacy Act)

**Applies to**: California residents, businesses with >$25M revenue or >50K users

**Key rights**:
- **Right to know**: What data is collected and how it's used
- **Right to delete**: Request deletion of personal information
- **Right to opt-out**: Opt out of data sales
- **Right to non-discrimination**: Equal service even if you opt out

**Penalties**: Up to $7,500 per intentional violation

### Other Regulations

| Law | Region | Key Focus |
|-----|--------|-----------|
| **PIPEDA** | Canada | Consent and accountability |
| **LGPD** | Brazil | Similar to GDPR |
| **PDPA** | Singapore | Consent and notification |
| **Privacy Act** | Australia | Government data handling |

---

## 🏗️ Privacy by Design

### Seven Foundational Principles

1. **Proactive not reactive**: Prevent privacy issues before they happen
2. **Privacy as default**: Maximum privacy out of the box
3. **Privacy embedded**: Built into design, not bolted on
4. **Full functionality**: Privacy doesn't compromise features (win-win)
5. **End-to-end security**: Protect throughout entire lifecycle
6. **Visibility and transparency**: Keep it open
7. **Respect for user privacy**: User-centric approach

### Implementation Checklist

**Before you build**:
- [ ] Privacy Impact Assessment (PIA)
- [ ] Identify what personal data you'll collect
- [ ] Document legal basis for processing
- [ ] Plan data retention and deletion
- [ ] Design consent mechanisms
- [ ] Plan security measures

**During development**:
- [ ] Minimize data collection
- [ ] Encrypt sensitive data
- [ ] Implement access controls
- [ ] Add audit logging
- [ ] Build user data export/delete features
- [ ] Create privacy policy

**After launch**:
- [ ] Regular privacy audits
- [ ] Update privacy policy as needed
- [ ] Monitor for breaches
- [ ] Handle data subject requests
- [ ] Train team on privacy

---

## 🛡️ Technical Implementation

### Data Classification

**Public**: Anyone can see (blog posts, public profiles)
**Internal**: Employees only (analytics, logs)
**Confidential**: Specific authorized users (user emails, purchase history)
**Restricted**: Highly sensitive (passwords, payment info, health data)

### Encryption

**At rest**:
```javascript
// Encrypt sensitive fields in database
const crypto = require('crypto');

function encrypt(text, key) {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);

  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  const authTag = cipher.getAuthTag();

  return {
    encrypted,
    iv: iv.toString('hex'),
    authTag: authTag.toString('hex')
  };
}

// Database schema
{
  email: encrypt(user.email, ENCRYPTION_KEY),  // Encrypted
  name: user.name,                              // Plain (for display)
  created_at: new Date()
}
```

**In transit**:
```yaml
# Force HTTPS everywhere
server {
  listen 80;
  return 301 https://$host$request_uri;
}

server {
  listen 443 ssl http2;

  ssl_certificate /path/to/cert.pem;
  ssl_certificate_key /path/to/key.pem;
  ssl_protocols TLSv1.2 TLSv1.3;
  ssl_ciphers HIGH:!aNULL:!MD5;
}
```

### Data Anonymization

```javascript
// Anonymize user data for analytics
function anonymizeUser(user) {
  return {
    id: hashUserId(user.id),        // Hash, don't use real ID
    country: user.country,           // Geographic data ok
    signupDate: truncateDate(user.created_at),  // Month/year only
    // Remove: email, name, IP, precise location
  };
}

// Hash user IDs consistently
function hashUserId(userId) {
  return crypto
    .createHash('sha256')
    .update(userId + SECRET_SALT)
    .digest('hex');
}
```

### User Data Requests

**Right to access** (GDPR Article 15):
```javascript
// Export user data
app.get('/api/user/data-export', authenticateUser, async (req, res) => {
  const userId = req.user.id;

  const data = {
    profile: await db.users.findOne({ id: userId }),
    posts: await db.posts.find({ authorId: userId }),
    comments: await db.comments.find({ authorId: userId }),
    settings: await db.settings.find({ userId }),
    // Include ALL data you have on the user
  };

  res.json({
    requestDate: new Date(),
    userData: data
  });
});
```

**Right to erasure** (GDPR Article 17):
```javascript
// Delete user and all associated data
app.delete('/api/user/delete-account', authenticateUser, async (req, res) => {
  const userId = req.user.id;

  // Delete or anonymize all user data
  await db.transaction(async (trx) => {
    await trx('users').where({ id: userId }).del();
    await trx('posts').where({ authorId: userId }).update({
      authorId: null,
      authorName: 'Deleted User'
    });
    await trx('comments').where({ authorId: userId }).del();
    await trx('sessions').where({ userId }).del();
    // Continue for all tables with user data
  });

  res.json({ message: 'Account deleted successfully' });
});
```

---

## 🍪 Cookie Consent

### Cookie Categories

**Strictly necessary**: Required for site to function (session cookies)
- ✅ No consent needed

**Functional**: Remember preferences (language, theme)
- ⚠️ Consent recommended

**Analytics**: Understand usage (Google Analytics)
- ⚠️ Consent required

**Marketing**: Advertising and tracking
- ⚠️ Consent required

### Cookie Banner Example

```html
<!-- Cookie consent banner -->
<div id="cookie-banner" class="cookie-banner">
  <p>We use cookies to improve your experience. You can choose which cookies to allow.</p>

  <div class="cookie-options">
    <label>
      <input type="checkbox" checked disabled> Necessary (required)
    </label>
    <label>
      <input type="checkbox" id="analytics-cookies"> Analytics
    </label>
    <label>
      <input type="checkbox" id="marketing-cookies"> Marketing
    </label>
  </div>

  <button onclick="acceptCookies()">Accept Selected</button>
  <button onclick="acceptAllCookies()">Accept All</button>
  <button onclick="rejectOptionalCookies()">Reject Optional</button>
</div>

<script>
function acceptCookies() {
  const analytics = document.getElementById('analytics-cookies').checked;
  const marketing = document.getElementById('marketing-cookies').checked;

  if (analytics) enableAnalytics();
  if (marketing) enableMarketing();

  localStorage.setItem('cookieConsent', JSON.stringify({
    necessary: true,
    analytics,
    marketing,
    timestamp: new Date()
  }));

  hideBanner();
}
</script>
```

---

## 📋 Privacy Policy

### What to Include

**Required sections**:
1. **What data we collect**: Be specific (emails, IP addresses, usage data)
2. **Why we collect it**: Legitimate purposes
3. **How we use it**: Be transparent
4. **Who we share with**: Third parties, processors
5. **How long we keep it**: Retention periods
6. **Your rights**: Access, deletion, portability, opt-out
7. **How to contact us**: Email, address
8. **Updates**: When policy was last updated

**Example snippet**:
```markdown
## What Data We Collect

**Account information**: When you create an account, we collect:
- Email address (for login and notifications)
- Username (for public display)
- Password (encrypted, never stored in plain text)

**Usage data**: We automatically collect:
- IP address (for security and analytics)
- Browser type and version (for compatibility)
- Pages visited and time spent (to improve our service)
- Approximate location (country level, from IP)

**We do NOT collect**: Precise geolocation, browsing history outside our site,
data from other apps or websites.

## How We Use Your Data

- **Provide the service**: Your email and username let you log in and use features
- **Communication**: Send important updates (we'll never spam you)
- **Improve our product**: Understand what features are used most
- **Security**: Detect and prevent fraud

## Your Rights

You can:
- **Access your data**: Request a copy of all data we have on you
- **Correct your data**: Update your profile information
- **Delete your data**: Request complete account deletion
- **Export your data**: Download your data in JSON format
- **Opt out of emails**: Unsubscribe from marketing emails

Email privacy@example.com to exercise these rights.
```

---

## 🚨 Data Breach Response

### Breach Response Plan

**Within 1 hour**:
- [ ] Contain the breach (stop ongoing access)
- [ ] Assess scope (what data, how many users)
- [ ] Notify incident response team

**Within 24 hours**:
- [ ] Document everything
- [ ] Begin forensic investigation
- [ ] Prepare user communication
- [ ] Determine legal obligations

**Within 72 hours** (GDPR requirement):
- [ ] Notify supervisory authority if high risk
- [ ] Notify affected users if high risk
- [ ] Coordinate with legal team
- [ ] Implement immediate fixes

### User Notification Template

```
Subject: Important Security Notice

Dear [User],

We are writing to inform you of a data security incident that may have affected your account.

What happened: On [date], we discovered that [brief description].

What data was affected: [Specific data types: emails, usernames, etc.]

What was NOT affected: [Passwords, payment info if applicable]

What we're doing:
- Immediately secured the vulnerability
- Notified relevant authorities
- Implementing additional security measures

What you should do:
- Change your password immediately
- Enable two-factor authentication
- Watch for suspicious activity

We sincerely apologize for this incident. Your privacy and security are our top priorities.

For questions: security@example.com

[Company Name]
```

---

## 📊 Privacy Metrics

**Track privacy health**:
- Time to respond to data subject requests (target: <30 days)
- Percentage of data encrypted at rest (target: 100% of sensitive data)
- Number of privacy incidents (target: 0)
- Cookie consent rate
- Privacy policy acceptance rate

See [LEGAL.md](LEGAL.md), [SECURITY.md](SECURITY.md) for complete privacy and legal compliance guidance.

---

*This data privacy guide is maintained with care and consciousness by the Luminous Dynamics community.*
