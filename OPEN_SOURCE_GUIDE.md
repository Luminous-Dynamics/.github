# 🌍 Open Source Guide

> "Given enough eyeballs, all bugs are shallow." — Linus's Law

*Last updated: January 2025*

This document outlines our **open source philosophy and practices**—why we build in the open, how we contribute to the commons, how we choose licenses, build sustainable communities, and create value for everyone through collaborative development.

---

## 💚 Open Source Philosophy

### What is Open Source?

**Open Source Software (OSS)** is software with source code that anyone can inspect, modify, and enhance. But it's more than that—it's a philosophy of collaboration, transparency, and community.

### The Four Freedoms (Free Software)

1. **Freedom to run** the program for any purpose
2. **Freedom to study** how the program works and adapt it
3. **Freedom to redistribute** copies to help others
4. **Freedom to improve** and share improvements with the community

### Why We Build in the Open

**Transparency**:
- Code is visible to all
- Decisions are documented
- No hidden agendas
- Trust through openness

**Collaboration**:
- Collective problem-solving
- Diverse perspectives
- Shared maintenance burden
- Faster innovation

**Quality**:
- Many eyes catch more bugs
- Peer review improves code
- Best ideas win
- Community holds maintainers accountable

**Sustainability**:
- Projects outlive individual companies
- Shared infrastructure benefits everyone
- Reduced duplication of effort
- Common solutions to common problems

**Learning**:
- Real-world code to study
- Mentorship opportunities
- Portfolio building
- Skill development

---

## 📜 Choosing a License

### License Categories

**Permissive** (MIT, Apache, BSD):
- ✅ Maximum freedom for users
- ✅ Easy adoption by companies
- ✅ Can be included in proprietary software
- ❌ Derivative works can be closed source
- **Use when**: You want maximum adoption and don't care about derivatives staying open

**Copyleft** (GPL, AGPL):
- ✅ Ensures derivatives stay open source
- ✅ Prevents proprietary forks
- ✅ Grows the commons
- ❌ Can deter commercial adoption
- **Use when**: You want to ensure all improvements benefit the community

**Weak Copyleft** (LGPL, MPL):
- ✅ Libraries can be used in proprietary software
- ✅ Modifications to the library must be shared
- ✅ Balance between permissive and copyleft
- **Use when**: Building libraries for wide use while protecting the core

### Common Licenses

| License | Type | Used By | Best For |
|---------|------|---------|----------|
| **MIT** | Permissive | React, Rails, Node.js | Maximum adoption |
| **Apache 2.0** | Permissive | Kubernetes, Android, Swift | Patent protection |
| **GPL v3** | Copyleft | Linux, Git, Bash | Ensuring freedom |
| **AGPL v3** | Strong Copyleft | MongoDB (old), Grafana | Network services |
| **MPL 2.0** | Weak Copyleft | Firefox, Terraform | File-level copyleft |

### How to Choose

```
┌─────────────────────────────────────┐
│ Do you want derivatives to stay     │
│ open source?                         │
└─────────┬───────────────────┬───────┘
          │                   │
         YES                 NO
          │                   │
          ▼                   ▼
    ┌──────────┐        ┌──────────┐
    │ Copyleft │        │Permissive│
    │ GPL/AGPL │        │ MIT/Apache│
    └──────────┘        └──────────┘
```

### Applying a License

**1. Add LICENSE file**:
```
your-repo/
├── LICENSE          ← Full license text
├── README.md
└── ...
```

**2. Add header to source files**:
```javascript
/**
 * Copyright 2025 Luminous Dynamics
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 */
```

**3. Mention in README**:
```markdown
## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
```

---

## 🏗️ Building Open Source Projects

### Starting an Open Source Project

**Before you start**:
- [ ] Check if similar projects exist (don't duplicate unnecessarily)
- [ ] Choose appropriate license
- [ ] Define project scope and goals
- [ ] Plan for maintenance burden
- [ ] Consider if you have time to maintain it

**Essential files**:
- `README.md` - What, why, how to use
- `LICENSE` - Legal terms
- `CONTRIBUTING.md` - How to contribute
- `CODE_OF_CONDUCT.md` - Community standards
- `.github/ISSUE_TEMPLATE/` - Issue templates
- `.github/PULL_REQUEST_TEMPLATE.md` - PR template

### Healthy Project Indicators

✅ **Active maintenance**:
- Issues responded to within 1 week
- PRs reviewed within 2 weeks
- Regular releases
- Updated dependencies

✅ **Good documentation**:
- Clear README with examples
- API documentation
- Contributing guide
- Changelog

✅ **Welcoming community**:
- Friendly responses to newcomers
- Good first issues labeled
- Code of conduct enforced
- Mentorship available

✅ **Sustainable governance**:
- Multiple maintainers
- Clear decision-making process
- Funded or sponsored
- Succession planning

---

## 🤝 Contributing to Open Source

### How to Contribute

**Not just code**:
- 📝 Improve documentation
- 🐛 Report bugs with clear reproduction steps
- 💡 Suggest features
- 🎨 Design assets
- 🌍 Translate to other languages
- 👥 Answer questions
- 📊 Triage issues

### First Contribution Checklist

1. **Find a project**:
   - Look for "good first issue" labels
   - Choose projects you actually use
   - Check if project is actively maintained

2. **Before you code**:
   - Read CONTRIBUTING.md
   - Check existing issues/PRs
   - Discuss approach in issue first
   - Understand the codebase

3. **Make your contribution**:
   - Fork the repository
   - Create a feature branch
   - Follow project style guide
   - Write tests
   - Update documentation

4. **Submit**:
   - Open pull request
   - Describe what and why
   - Link to related issues
   - Be patient and responsive
   - Accept feedback gracefully

### Contribution Example

```bash
# 1. Fork and clone
git clone https://github.com/YOUR-USERNAME/project.git
cd project

# 2. Create branch
git checkout -b fix/improve-error-messages

# 3. Make changes, test, commit
npm test
git add .
git commit -m "Improve error messages for invalid input"

# 4. Push and create PR
git push origin fix/improve-error-messages
# Open PR on GitHub
```

---

## 💰 Sustainability Models

### How to Sustain Open Source Work

**Volunteer-driven**:
- ✅ Truly free and independent
- ❌ Burnout risk, inconsistent maintenance
- **Example**: Most small projects

**Corporate-sponsored**:
- ✅ Dedicated resources, professional development
- ❌ Risk of abandonment if priorities change
- **Example**: React (Meta), Kubernetes (Google/CNCF)

**Foundation-backed**:
- ✅ Independent governance, long-term stability
- ❌ Slower decision-making
- **Example**: Linux (Linux Foundation), Python (PSF)

**Dual-licensing**:
- ✅ Open core, paid enterprise features
- ❌ Community may feel second-class
- **Example**: MySQL, MongoDB

**Donations/Sponsorship**:
- ✅ Community-funded, independent
- ❌ Often insufficient for full-time work
- **Example**: Vue.js (Patreon), many GitHub Sponsors projects

**Open core**:
- ✅ Free basic version, paid premium
- ❌ Tension between open and commercial
- **Example**: GitLab, Sentry

### Funding Platforms

- **GitHub Sponsors**: Integrated with GitHub
- **Open Collective**: Transparent finances
- **Patreon**: Recurring donations
- **Ko-fi**: One-time or monthly donations
- **Tidelift**: Pay for professionally maintained dependencies

---

## 🏢 Inner Source

### Applying Open Source Practices Internally

**Inner source** brings open source practices inside companies:

**Benefits**:
- Break down silos
- Encourage collaboration
- Improve code quality
- Knowledge sharing
- Retain talent (devs love open practices)

**How to implement**:
1. Make internal repos discoverable
2. Accept contributions across teams
3. Document like open source
4. Review transparently
5. Recognize contributors

---

## ⚠️ Common Pitfalls

### What Can Go Wrong

**Burnout**:
- **Problem**: Maintainer overwhelmed by demands
- **Solution**: Set boundaries, share maintenance, say no

**Toxic community**:
- **Problem**: Harassment, negativity
- **Solution**: Strong code of conduct, active moderation

**No succession plan**:
- **Problem**: Project dies when maintainer leaves
- **Solution**: Build co-maintainer team, document everything

**License confusion**:
- **Problem**: Mixing incompatible licenses
- **Solution**: Track all dependencies, use SPDX identifiers

**Feature creep**:
- **Problem**: Project becomes bloated
- **Solution**: Clear scope, say no to out-of-scope features

**Security vulnerabilities**:
- **Problem**: Public code, public vulnerabilities
- **Solution**: Security policy, private disclosure process, quick patches

---

## 📚 Resources

### Learning More

**Guides**:
- [opensource.guide](https://opensource.guide) - Comprehensive guides
- [Choose a License](https://choosealicense.com) - License picker
- [First Timers Only](https://www.firsttimersonly.com) - Beginner-friendly projects

**Books**:
- "Working in Public" by Nadia Eghbal
- "The Cathedral and the Bazaar" by Eric S. Raymond
- "Producing Open Source Software" by Karl Fogel

**Communities**:
- [Open Source Friday](https://opensourcefriday.com)
- [Hacktoberfest](https://hacktoberfest.com)
- [Google Summer of Code](https://summerofcode.withgoogle.com)

See [LEGAL.md](LEGAL.md), [SUSTAINABILITY.md](SUSTAINABILITY.md), [CONTRIBUTING.md](CONTRIBUTING.md) for complete open source governance.

---

*This open source guide is maintained with care and consciousness by the Luminous Dynamics community.*
