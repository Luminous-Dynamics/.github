# 📚 Tactical Playbooks

> "Knowledge becomes wisdom through practice. Wisdom becomes mastery through repetition."

*Last updated: January 2025*

This document provides **step-by-step tactical playbooks** for common scenarios in the Luminous Dynamics community. Think of these as recipes—clear, actionable guides that reference our comprehensive documentation while giving you a practical path forward.

---

## 🎯 How to Use This Guide

Each playbook:
- Provides a **step-by-step checklist** you can follow
- **Cross-references** relevant documentation for deeper context
- Includes **time estimates** so you can plan accordingly
- Offers **tips from experience** to avoid common pitfalls
- Maintains our **consciousness-first values** throughout

Don't treat these as rigid scripts—adapt them to your context while preserving the underlying principles.

---

## 📖 Available Playbooks

### For Contributors
1. [Your First Contribution](#playbook-1-your-first-contribution) - Complete walkthrough (30-60 min)
2. [Proposing a Major Change](#playbook-2-proposing-a-major-change) - RFCs and discussion (1-2 hours)
3. [Responding to Code Review](#playbook-3-responding-to-code-review) - Grace under feedback (15-30 min)

### For Maintainers
4. [Reviewing Your First PR](#playbook-4-reviewing-your-first-pr) - Kind, thorough reviews (20-40 min)
5. [Becoming a Maintainer](#playbook-5-becoming-a-maintainer) - Growth path (6-12 months)
6. [Onboarding a New Team Member](#playbook-6-onboarding-a-new-team-member) - First 90 days

### For Community Builders
7. [Running Your First Event](#playbook-7-running-your-first-event) - Event execution (12 weeks)
8. [Starting a Working Group](#playbook-8-starting-a-working-group) - Focus area leadership (ongoing)

### For Crisis Response
9. [Handling a Security Issue](#playbook-9-handling-a-security-issue) - Security incident response (ASAP)
10. [Managing Conflict](#playbook-10-managing-conflict) - De-escalation and resolution (varies)

### For Releases
11. [Releasing a New Version](#playbook-11-releasing-a-new-version) - Release day checklist (2-4 hours)
12. [Deprecating a Feature](#playbook-12-deprecating-a-feature) - Graceful sunsets (3-6 months)

---

## Playbook 1: Your First Contribution

**Goal**: Make your first meaningful contribution to a Luminous Dynamics project
**Time**: 30-60 minutes (excluding development time)
**Prerequisites**: GitHub account, basic git knowledge
**Related docs**: [GETTING_STARTED.md](GETTING_STARTED.md), [CONTRIBUTING.md](CONTRIBUTING.md)

### Step-by-Step

#### Before You Code (10-15 min)

- [ ] **Read the project README** to understand its purpose and philosophy
- [ ] **Review [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** - understand community values
- [ ] **Check [GETTING_STARTED.md](GETTING_STARTED.md)** for setup instructions
- [ ] **Browse existing issues** labeled `good-first-issue` or `help-wanted`
- [ ] **Comment on the issue** you want to work on:
  ```
  Hi! I'd love to work on this issue. I'm thinking of [brief approach].
  Does this sound reasonable? This is my first contribution, so I'd
  appreciate any guidance! 💚
  ```
- [ ] **Wait for acknowledgment** from a maintainer (usually within 24-48 hours)

**💡 Tip**: If no response after 48 hours, it's okay to gently ping or choose a different issue.

#### Setting Up (15-20 min)

- [ ] **Fork the repository** to your GitHub account
- [ ] **Clone your fork** locally:
  ```bash
  git clone https://github.com/YOUR-USERNAME/repo-name.git
  cd repo-name
  ```
- [ ] **Add upstream remote**:
  ```bash
  git remote add upstream https://github.com/Luminous-Dynamics/repo-name.git
  ```
- [ ] **Create a feature branch** with a descriptive name:
  ```bash
  git checkout -b fix/issue-123-clear-description
  ```
- [ ] **Install dependencies** and verify tests pass:
  ```bash
  npm install  # or appropriate package manager
  npm test     # make sure everything works before you start
  ```

**💡 Tip**: If setup fails, check [GETTING_STARTED.md](GETTING_STARTED.md) troubleshooting section or ask in Discussions.

#### Making Changes (varies)

- [ ] **Write your code** with consciousness and care
- [ ] **Follow [STYLE_GUIDE.md](STYLE_GUIDE.md)** conventions
- [ ] **Add tests** for your changes (see [TESTING.md](TESTING.md))
- [ ] **Update documentation** if you changed behavior
- [ ] **Run tests locally** and ensure they pass:
  ```bash
  npm test
  npm run lint
  ```
- [ ] **Commit with meaningful messages** (see [CONTRIBUTING.md](CONTRIBUTING.md)):
  ```bash
  git add .
  git commit -m "Fix: Resolve issue #123 by improving error handling

  - Add validation for null inputs
  - Include helpful error messages
  - Add test coverage for edge cases

  Fixes #123"
  ```

**💡 Tip**: Reference the issue number with "Fixes #123" to auto-close it when merged.

#### Submitting (10-15 min)

- [ ] **Push your branch**:
  ```bash
  git push origin fix/issue-123-clear-description
  ```
- [ ] **Create a Pull Request** on GitHub
- [ ] **Fill out the PR template** completely and thoughtfully
- [ ] **Request review** from maintainers listed in [CODEOWNERS](CODEOWNERS)
- [ ] **Link the issue** if not auto-linked (use "Fixes #123" in PR description)
- [ ] **Be patient and kind** while waiting for review

**💡 Tip**: PRs typically get initial feedback within 48-72 hours. Use the wait time to start another contribution!

#### After Submission (ongoing)

- [ ] **Respond to review comments** promptly and graciously
- [ ] **Ask questions** if feedback is unclear - reviewers want to help!
- [ ] **Make requested changes** in new commits (don't force-push during review)
- [ ] **Request re-review** after addressing feedback
- [ ] **Celebrate** when merged! 🎉
- [ ] **Update your [CONTRIBUTORS.md](CONTRIBUTORS.md)** entry if needed

**💡 Tip**: See [Playbook 3](#playbook-3-responding-to-code-review) for handling code review feedback.

### Common Pitfalls

❌ **Not reading existing documentation** → Read at least README, CONTRIBUTING, and CODE_OF_CONDUCT
❌ **Starting to code before getting issue acknowledgment** → Always comment first
❌ **Making huge first PRs** → Start small, build trust, then tackle bigger things
❌ **Taking feedback personally** → Remember: reviews critique code, not you
❌ **Radio silence after submitting** → Stay engaged and responsive

### Celebration Checklist

After your first PR merges:
- [ ] **Thank your reviewers** publicly in the PR
- [ ] **Share your achievement** (Twitter, LinkedIn, personal blog)
- [ ] **Reflect**: What did you learn? What surprised you?
- [ ] **Pay it forward**: Welcome the next first-time contributor

---

## Playbook 2: Proposing a Major Change

**Goal**: Successfully propose and get buy-in for a significant change
**Time**: 1-2 hours for initial proposal, ongoing for discussion
**Prerequisites**: Understanding of the project, identified problem
**Related docs**: [CONTRIBUTING.md](CONTRIBUTING.md), [ADR.md](ADR.md), [GOVERNANCE.md](GOVERNANCE.md)

### When to Use This Playbook

Use this for:
- New features that affect many users
- Breaking changes to APIs
- Significant refactoring (>500 lines)
- Changes to architecture or design patterns
- New dependencies or tooling

**Don't use for**: Bug fixes, documentation updates, small improvements (just submit a PR).

### Step-by-Step

#### Research Phase (30-45 min)

- [ ] **Search existing issues/discussions** to avoid duplicates
- [ ] **Review [ADR.md](ADR.md)** for past architectural decisions
- [ ] **Check [VISION_AND_ROADMAP.md](VISION_AND_ROADMAP.md)** for alignment
- [ ] **Gather evidence**: metrics, user complaints, benchmark data
- [ ] **Explore alternatives** - consider at least 3 approaches
- [ ] **Identify stakeholders** who should be involved

#### Proposal Writing (30-60 min)

- [ ] **Create a Discussion** (not an Issue) in the appropriate category
- [ ] **Use the proposal template** (see [TEMPLATES.md](TEMPLATES.md)):

```markdown
# [Concise Title]: [Brief description]

## Problem Statement
[What problem are we solving? Why is it important? Include data/evidence.]

## Proposed Solution
[Your recommended approach with enough detail to evaluate feasibility.]

## Alternative Approaches Considered
1. **[Alternative 1]**: [Why not this?]
2. **[Alternative 2]**: [Why not this?]
3. **[Do nothing]**: [Why status quo isn't acceptable?]

## Impact Assessment
- **Users affected**: [Who and how?]
- **Breaking changes**: [Any?]
- **Performance**: [Expected impact]
- **Maintenance burden**: [Ongoing costs?]
- **Dependencies**: [New ones needed?]

## Implementation Plan
1. [Phase 1 with time estimate]
2. [Phase 2 with time estimate]
3. [Phase 3 with time estimate]

## Open Questions
1. [What are you uncertain about?]
2. [What needs community input?]

## ERC Alignment
[How does this align with our consciousness-first values?]
```

- [ ] **Tag relevant stakeholders** for input
- [ ] **Set clear expectations** for feedback timeline

#### Discussion Phase (1-4 weeks)

- [ ] **Respond to questions** thoughtfully and promptly
- [ ] **Synthesize feedback** periodically (e.g., weekly updates)
- [ ] **Be open to pivoting** if better ideas emerge
- [ ] **Document consensus** as it forms
- [ ] **Update the proposal** based on discussion (track revisions)
- [ ] **Know when to call for decision** - don't let discussion become endless

**💡 Tip**: After ~2 weeks of discussion, post a summary: "Here's what I'm hearing... [consensus points]. Here's what's still unclear... [open questions]. I propose we decide by [date]."

#### Decision Point (1-2 days)

- [ ] **Request formal decision** from maintainers per [GOVERNANCE.md](GOVERNANCE.md)
- [ ] **Document the decision** in the Discussion
- [ ] **If approved**: Create an Architecture Decision Record ([ADR.md](ADR.md))
- [ ] **If rejected**: Document reasoning and thank everyone for their time
- [ ] **If needs more info**: Identify specific gaps and timeline to revisit

#### Implementation (varies)

- [ ] **Break into smaller PRs** that can be reviewed independently
- [ ] **Reference the discussion** in PR descriptions
- [ ] **Update documentation** as you go, not at the end
- [ ] **Communicate progress** weekly in the Discussion thread
- [ ] **Celebrate milestones** along the way

### Common Pitfalls

❌ **Proposing solution instead of problem** → Start with "why," not "how"
❌ **Not considering alternatives** → Always show you explored options
❌ **Getting defensive** → Stay curious and open to better ideas
❌ **Proposal too vague** → Include enough detail for informed decision
❌ **Proposal too detailed** → Don't write full implementation before buy-in

---

## Playbook 3: Responding to Code Review

**Goal**: Gracefully receive and act on code review feedback
**Time**: 15-30 minutes per review round
**Prerequisites**: Submitted PR
**Related docs**: [CODE_REVIEW.md](CODE_REVIEW.md), [COMMUNICATION.md](COMMUNICATION.md)

### Mindset Preparation

Before reading review comments:
- [ ] **Take a breath** - you are not your code
- [ ] **Assume positive intent** - reviewers want to help you succeed
- [ ] **Remember**: Feedback is a gift, even when it stings
- [ ] **Growth mindset**: Every review makes you a better engineer

### Step-by-Step

#### Initial Reading (5 min)

- [ ] **Read all comments** before responding to any
- [ ] **Categorize feedback**:
  - 🔴 Blockers (must fix)
  - 🟡 Suggestions (should consider)
  - 🟢 Questions (need clarification)
  - 💙 Praise (celebrate these!)
- [ ] **Separate technical from personal** - feedback is about code, not you

#### Responding to Comments (10-20 min)

For each comment:

**If you agree** (most common):
- [ ] ✅ React with thumbs up or heart
- [ ] Reply: "Good catch! I'll fix this."
- [ ] Make the change
- [ ] Mark as "Resolved" after pushing fix

**If you're unsure**:
- [ ] 🤔 Ask clarifying questions:
  ```
  I want to make sure I understand - are you suggesting [interpretation]?
  Could you provide an example of what you're envisioning?
  ```
- [ ] Wait for clarification before implementing

**If you disagree**:
- [ ] 🤝 Respond respectfully with reasoning:
  ```
  I see your point about [concern]. I chose [approach] because [reasoning].
  However, I might be missing something - what are the downsides you see
  with this approach?
  ```
- [ ] **Be open to being wrong** - reviewers might have context you lack
- [ ] If discussion extends beyond 2-3 exchanges, **suggest a synchronous call**

**If feedback feels harsh**:
- [ ] 😌 Take a break before responding (5-60 minutes)
- [ ] **Assume positive intent** - tone is hard in text
- [ ] **Focus on technical content**, ignore perceived tone
- [ ] If truly inappropriate, **escalate** per [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

#### Making Changes (varies)

- [ ] **Create new commits** for review changes (don't squash during review):
  ```bash
  git commit -m "Address review feedback: improve error handling"
  ```
- [ ] **Don't force-push** until final approval (preserves review context)
- [ ] **Test thoroughly** - don't introduce new bugs while fixing feedback
- [ ] **Update tests and docs** if behavior changed

#### Requesting Re-Review (2 min)

- [ ] **Summarize changes** in a comment:
  ```
  Thank you for the thoughtful review! I've addressed all feedback:

  - ✅ Improved error handling (commit abc123)
  - ✅ Added null checks (commit def456)
  - ❓ Still discussing the caching approach in thread above

  Ready for another look when you have time! 🙏
  ```
- [ ] **Request re-review** explicitly (tag reviewers if needed)
- [ ] **Be patient** - reviewers are volunteers/busy colleagues

### Common Pitfalls

❌ **Responding defensively** → Take a breath, assume positive intent
❌ **Making changes without discussing** → Sometimes discussion > quick fix
❌ **Ignoring "minor" feedback** → Small things matter for code quality
❌ **Force-pushing during review** → Makes it hard for reviewers to track changes
❌ **Not thanking reviewers** → Reviews are gifts of time and expertise

### Celebration

After approval:
- [ ] **Thank reviewers** genuinely and specifically:
  ```
  Thank you @reviewer for the excellent feedback! I especially appreciated
  your suggestion about [specific thing] - I learned [what you learned]. 💚
  ```
- [ ] **Reflect**: What did you learn? What will you do differently next time?

---

## Playbook 4: Reviewing Your First PR

**Goal**: Provide a kind, thorough, and helpful code review
**Time**: 20-40 minutes
**Prerequisites**: Maintainer/reviewer permissions, empathy
**Related docs**: [CODE_REVIEW.md](CODE_REVIEW.md), [COMMUNICATION.md](COMMUNICATION.md)

### Before You Start

- [ ] **Allocate uninterrupted time** - rushing leads to poor reviews
- [ ] **Check your mindset** - Are you in a kind, curious state?
- [ ] **Remember**: Your goal is to help the author succeed, not to show how smart you are

### Step-by-Step

#### Context Gathering (5-10 min)

- [ ] **Read the PR description** completely
- [ ] **Understand the linked issue** or motivation
- [ ] **Check CI status** - all tests passing?
- [ ] **Review PR size** - if >400 lines, consider asking to split
- [ ] **Note if first-time contributor** - extra kindness and patience

#### Code Review (15-25 min)

Review in this order:

**1. Architecture & Design** (5 min)
- [ ] Does this solve the right problem?
- [ ] Is the approach sound?
- [ ] Does it fit with existing patterns?
- [ ] Any security concerns?

**2. Implementation** (10-15 min)
- [ ] **Code quality**: Readable? Maintainable?
- [ ] **Edge cases**: What could go wrong?
- [ ] **Performance**: Any obvious issues?
- [ ] **Tests**: Adequate coverage? Test the right things?
- [ ] **Documentation**: Updated? Sufficient?

**3. Style & Nitpicks** (5 min)
- [ ] Follows [STYLE_GUIDE.md](STYLE_GUIDE.md)?
- [ ] Consistent with codebase conventions?
- [ ] **Use automation for this** when possible (linters, formatters)

#### Writing Comments

**Use the "Ask, Don't Tell" approach**:
- [ ] ❌ "This is wrong. Do X instead."
- [ ] ✅ "Have you considered X? It might help with Y concern."

**Be specific and actionable**:
- [ ] ❌ "This could be better."
- [ ] ✅ "Consider extracting this 20-line block into a helper function `validateUserInput()` for reusability."

**Explain the "why"**:
- [ ] ❌ "Don't use `var` here."
- [ ] ✅ "Using `const` instead of `var` prevents accidental reassignment and makes scope clearer."

**Balance criticism with praise**:
- [ ] **Start with something positive**: "Nice test coverage!"
- [ ] **Sandwich**: Praise → Critique → Encouragement
- [ ] **End encouragingly**: "This is really close! Just a few small things."

**Label your feedback**:
- [ ] 🔴 **Blocker**: "We need to fix the SQL injection vulnerability here before merging."
- [ ] 🟡 **Suggestion**: "Consider adding a timeout here, but not required for this PR."
- [ ] 🤔 **Question**: "I'm curious why we chose approach X over Y?"
- [ ] 💭 **Thought**: "Just thinking out loud - might this impact performance with large datasets?"

#### Decision Making (5 min)

Choose your review status:

**✅ Approve** when:
- [ ] Code is solid (doesn't need to be perfect!)
- [ ] Any remaining nitpicks are truly minor
- [ ] You trust the author to address small comments before/after merge

**💬 Comment** when:
- [ ] You have questions or suggestions
- [ ] You're not the primary reviewer but want to contribute
- [ ] It's informational, not blocking

**🔄 Request Changes** when:
- [ ] There are bugs or security issues
- [ ] Significant design concerns
- [ ] Missing critical tests or documentation
- [ ] **Be clear**: What specifically needs to change?

**💡 Tip**: Use "Request Changes" sparingly, especially for first-time contributors.

#### Follow-Up (ongoing)

- [ ] **Respond promptly** to author questions
- [ ] **Re-review quickly** after changes (ideally within 24 hours)
- [ ] **Don't nitpick forever** - know when good enough is good enough
- [ ] **Approve and thank** when ready:
  ```
  Excellent work! Thank you for the thorough tests and clear documentation.
  Welcome to the contributor community! 🎉
  ```

### Common Pitfalls

❌ **Reviewing only for style** → Focus on correctness, design, then style
❌ **Being vague** → "This seems off" is not helpful
❌ **Perfectionism** → Don't let perfect be enemy of good
❌ **Forgetting to praise** → Positive feedback motivates and teaches
❌ **Ghosting** → If you can't finish review, say so and reassign

### For First-Time Contributors

Extra care:
- [ ] **Welcome them warmly** in your first comment
- [ ] **Over-explain** - don't assume they know project conventions
- [ ] **Teach, don't just correct**: "Here's why we do X..."
- [ ] **Be encouraging** - they're nervous!
- [ ] **Offer to pair** if struggling: "Happy to hop on a call if helpful"
- [ ] **Celebrate loudly** when merged - make them want to come back!

---

## Playbook 5: Becoming a Maintainer

**Goal**: Grow from contributor to trusted maintainer
**Time**: 6-12 months of sustained contribution
**Prerequisites**: Several merged contributions, deep project knowledge
**Related docs**: [CONTRIBUTOR_LADDER.md](CONTRIBUTOR_LADDER.md), [GOVERNANCE.md](GOVERNANCE.md)

### The Journey (6-12 months)

This isn't a checklist you rush through—it's a natural growth path.

#### Phase 1: Build Foundation (Months 1-3)

- [ ] **Make regular contributions** (aim for 1-2 PRs/month)
- [ ] **Participate in discussions** with thoughtful input
- [ ] **Help other contributors** in Issues/Discussions
- [ ] **Learn the codebase** deeply, not just your corner
- [ ] **Attend community events** if available
- [ ] **Build relationships** with existing maintainers

**Milestone**: You're a recognized regular contributor.

#### Phase 2: Take Ownership (Months 4-6)

- [ ] **Own a feature area** - become the go-to expert
- [ ] **Triage issues** - label, prioritize, ask clarifying questions
- [ ] **Review PRs** (as commenter, not approver yet)
- [ ] **Write documentation** to help future contributors
- [ ] **Mentor newer contributors** - answer questions, guide first PRs
- [ ] **Participate in planning** - roadmap discussions, architecture decisions

**Milestone**: Maintainers rely on your expertise in your area.

#### Phase 3: Demonstrate Leadership (Months 7-9)

- [ ] **Lead initiatives** - drive features from idea to completion
- [ ] **Make architectural decisions** in your area
- [ ] **Resolve conflicts** gracefully when they arise
- [ ] **Improve processes** - identify and fix friction points
- [ ] **Represent the project** - speak at meetups, write blog posts
- [ ] **Show judgment** - knowing when to say no, when to escalate

**Milestone**: You're acting like a maintainer already.

#### Phase 4: Formalize Role (Months 10-12)

- [ ] **Express interest** to existing maintainers:
  ```
  I've been thinking about my growth in this community, and I'd love
  to take on more responsibility as a maintainer. I'm particularly
  passionate about [area]. Would that be helpful? What would the path
  look like?
  ```
- [ ] **Understand expectations** - time commitment, responsibilities, on-call?
- [ ] **Complete any required training** - security, incident response, etc.
- [ ] **Get nominated** by existing maintainer per [GOVERNANCE.md](GOVERNANCE.md)
- [ ] **Demonstrate readiness** during trial period if applicable
- [ ] **Receive maintainer access** and celebrate! 🎉

### What Maintainers Look For

✅ **Technical skills**:
- Write quality code consistently
- Understand architecture and design patterns
- Can review code thoughtfully

✅ **Communication**:
- Kind and clear in all interactions
- Can explain complex topics simply
- Handles conflict gracefully

✅ **Judgment**:
- Knows when to ask for help
- Balances user needs with technical constraints
- Says no when appropriate

✅ **Values alignment**:
- Embodies consciousness-first principles
- Treats all contributors with respect
- Prioritizes community health

✅ **Sustainability**:
- Contributes consistently, not in bursts
- Maintains work-life balance
- Asks for help when overwhelmed

### Common Pitfalls

❌ **Rushing the process** → Trust takes time to build
❌ **Only coding** → Maintainership is about people, not just code
❌ **Being a hero** → Maintainers build systems that work without them
❌ **Burning out** → Sustainable pace always beats sprints
❌ **Not asking** → Existing maintainers may not realize you're interested

### Your First Month as Maintainer

After you're officially a maintainer:

**Week 1**:
- [ ] Get added to maintainer team and permissions
- [ ] Announcement in community channels
- [ ] Read all maintainer-only docs
- [ ] Set up any required tooling/access

**Week 2-4**:
- [ ] **Pair with experienced maintainer** on reviews
- [ ] **Take on easy reviews** solo - build confidence
- [ ] **Join maintainer meetings** and listen more than you speak
- [ ] **Ask questions** - there's no stupid questions

**Month 2-3**:
- [ ] **Find your rhythm** - what aspects do you enjoy most?
- [ ] **Own something** - an area, a process, a working group
- [ ] **Remember**: You're still learning. That never stops.

### Celebration

When you become a maintainer:
- [ ] **Update [CONTRIBUTORS.md](CONTRIBUTORS.md)** with new role
- [ ] **Thank those who supported you** publicly
- [ ] **Reflect**: How will you use this power to lift others?
- [ ] **Pay it forward**: Start mentoring the next generation

---

## Playbook 6: Onboarding a New Team Member

**Goal**: Help a new maintainer/team member succeed in their first 90 days
**Time**: Ongoing investment over 90 days
**Prerequisites**: You're an established team member
**Related docs**: [MENTORSHIP.md](MENTORSHIP.md), [ONBOARDING_AUTOMATION.md](ONBOARDING_AUTOMATION.md)

### Pre-Start (1 week before)

- [ ] **Send welcome email** with excitement and logistics
- [ ] **Grant appropriate access** - GitHub, comms channels, docs
- [ ] **Assign an onboarding buddy** (you or someone else)
- [ ] **Prepare first tasks** - meaningful but achievable
- [ ] **Schedule first 1-on-1** for Day 1 or 2
- [ ] **Add to team calendar** for meetings, events

### Day 1

- [ ] **Welcome warmly** in team channel:
  ```
  🎉 Everyone please welcome @newperson to the team! They'll be focusing
  on [area] and bring experience in [background]. We're so glad you're
  here! Feel free to ask us anything. 💚
  ```
- [ ] **1-on-1 meeting** (30-60 min):
  - Get to know them personally
  - Understand their goals and fears
  - Tour the project landscape
  - Review first week plan
  - Answer all questions
- [ ] **Introduce to key people** they'll work with
- [ ] **Share essential resources**: [GETTING_STARTED.md](GETTING_STARTED.md), team norms, communication channels

### Week 1: Foundation

Daily check-ins (15 min):
- [ ] How are you feeling?
- [ ] What questions came up?
- [ ] Any blockers?
- [ ] What's your focus today?

Tasks for their first week:
- [ ] **Set up development environment** (have them update [GETTING_STARTED.md](GETTING_STARTED.md) if anything is unclear!)
- [ ] **Read core documentation** - README, CONTRIBUTING, CODE_OF_CONDUCT, VISION
- [ ] **Make a small contribution** - fix docs, add test, small bug fix
- [ ] **Attend team meeting** as observer
- [ ] **End of week retro** (30 min):
  - What went well?
  - What was confusing?
  - What would have helped?
  - What's exciting about next week?

### Weeks 2-4: Building Confidence

Weekly 1-on-1s (30 min):
- [ ] Review progress on assigned tasks
- [ ] Remove blockers
- [ ] Answer accumulated questions
- [ ] Gradually increase responsibility

Expanding scope:
- [ ] **Assign meaty first project** - something they can own
- [ ] **Include in code reviews** - first as observer, then participant
- [ ] **Introduce to adjacent teams** they'll collaborate with
- [ ] **Pair program** on something complex
- [ ] **Invite to design discussions** - start building that context

### Weeks 5-8: Finding Flow

Bi-weekly 1-on-1s (30 min):
- [ ] Shift from "how to" to "why" conversations
- [ ] Discuss career growth and interests
- [ ] Get their input on processes and decisions
- [ ] Start thinking about areas they could own

Growing responsibility:
- [ ] **First independent feature** from design to deployment
- [ ] **Lead a small initiative** - could be technical or process
- [ ] **Start mentoring newer contributors** - great way to solidify knowledge
- [ ] **Present something** in team meeting - build visibility

### Weeks 9-12: Independence

Monthly 1-on-1s (shifting to regular cadence):
- [ ] Career development focus
- [ ] Feedback (both ways!)
- [ ] Long-term vision and growth

Full team member:
- [ ] **Owns significant area** with minimal oversight
- [ ] **Participates fully** in planning and decisions
- [ ] **Comfortable asking for help** when needed
- [ ] **Helping onboard the next person** - the cycle continues

### 90-Day Retrospective

Schedule a longer 1-on-1 (60 min):
- [ ] **Celebrate growth** - look how far they've come!
- [ ] **Review goals** - did we achieve what we hoped?
- [ ] **Gather feedback** - what could we improve in onboarding?
- [ ] **Set next 90-day goals** together
- [ ] **Discuss** potential areas of ownership going forward
- [ ] **Formalize** any role changes or new responsibilities

### Common Pitfalls

❌ **Information overload** → Drip-feed info as needed
❌ **Sink or swim** → Check in frequently, especially early
❌ **Only assigning grunt work** → Give meaningful projects
❌ **Not getting their feedback** → They see our blind spots!
❌ **Forgetting to celebrate** → Recognize milestones!

### Celebration

After 90 days:
- [ ] **Public recognition** in team channel of their accomplishments
- [ ] **Update team directory** if roles/areas changed
- [ ] **Thank them** for their contributions
- [ ] **Get their input** on improving onboarding for next person

---

## Playbook 7: Running Your First Event

**Goal**: Successfully plan and execute a community event
**Time**: 12 weeks from planning to post-event
**Prerequisites**: Event idea, basic organizational skills
**Related docs**: [EVENTS.md](EVENTS.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

See [EVENTS.md](EVENTS.md) for comprehensive event planning guidance. This playbook provides a condensed timeline.

### Weeks 1-4: Planning

- [ ] **Define event purpose** - why this event, why now?
- [ ] **Choose format** - meetup, hackathon, workshop, conference?
- [ ] **Set date and time** - check for conflicts, consider timezones
- [ ] **Create budget** - venue, food, materials, speaker travel?
- [ ] **Secure venue** (if in-person) or virtual platform
- [ ] **Recruit co-organizers** - don't do this alone!
- [ ] **Draft agenda** - what will actually happen?

### Weeks 5-8: Promotion

- [ ] **Create event page** - GitHub Discussion, Eventbrite, Meetup.com
- [ ] **Announce widely** - social media, newsletters, community channels
- [ ] **Invite speakers** if applicable
- [ ] **Set up registration** with accessibility questions
- [ ] **Plan for accessibility** - dietary needs, mobility, virtual option?
- [ ] **Prepare materials** - slides, handouts, swag

### Weeks 9-11: Logistics

- [ ] **Confirm final headcount** and adjust plans
- [ ] **Order food** (if in-person) with dietary accommodations
- [ ] **Test technology** - A/V equipment, video platform, screen sharing
- [ ] **Prepare Code of Conduct enforcement plan** (see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md))
- [ ] **Assign day-of roles** - greeter, tech support, facilitator, photographer
- [ ] **Send reminder** to registrants with logistics
- [ ] **Create shared notes doc** for collaborative note-taking

### Event Day

**Before**:
- [ ] Arrive early to set up
- [ ] Test all technology
- [ ] Set up signage and directions
- [ ] Prep food and beverages
- [ ] Final team briefing

**During**:
- [ ] **Welcome attendees warmly** - make everyone feel included
- [ ] **Share Code of Conduct** and how to report issues
- [ ] **Facilitate inclusively** - create space for all voices
- [ ] **Take photos** (with permission)
- [ ] **Capture key insights** in shared notes
- [ ] **Be flexible** - plans change, roll with it gracefully

**After**:
- [ ] **Thank attendees** as they leave
- [ ] **Clean up thoroughly**
- [ ] **Debrief with co-organizers** - what worked, what didn't?

### Week 12: Follow-Up

- [ ] **Share event notes** and photos with attendees
- [ ] **Send thank you** to speakers, sponsors, venues
- [ ] **Publish retrospective** (see [RETROSPECTIVES.md](RETROSPECTIVES.md))
- [ ] **Update [EVENTS.md](EVENTS.md)** with lessons learned
- [ ] **Celebrate** your accomplishment! 🎉
- [ ] **Plan next event** if there's energy and interest

---

## Playbook 8: Starting a Working Group

**Goal**: Launch a focused working group to advance a specific area
**Time**: Ongoing
**Prerequisites**: Identified need, initial interested members
**Related docs**: [GOVERNANCE.md](GOVERNANCE.md), [COMMUNICATION.md](COMMUNICATION.md)

See [GOVERNANCE.md](GOVERNANCE.md) Section on Working Groups for details. Quick start:

### Formation (Week 1-2)

- [ ] **Identify clear charter** - what problem does this group solve?
- [ ] **Recruit founding members** (3-5 people to start)
- [ ] **Propose to maintainers** for approval
- [ ] **Set up communication** - dedicated channel, mailing list
- [ ] **Schedule kickoff meeting**

### Kickoff Meeting

- [ ] Introductions - why is everyone here?
- [ ] Review and refine charter
- [ ] Define success metrics - how will we know we're succeeding?
- [ ] Set meeting cadence - weekly? bi-weekly?
- [ ] Assign roles - facilitator, note-taker, timekeeper
- [ ] Identify first deliverables

### Ongoing Operations

- [ ] **Regular meetings** with published agendas
- [ ] **Public notes** - transparency builds trust
- [ ] **Quarterly updates** to broader community
- [ ] **Welcome new members** who want to contribute
- [ ] **Sunset gracefully** when mission accomplished

---

## Playbook 9: Handling a Security Issue

**Goal**: Respond quickly and responsibly to security vulnerabilities
**Time**: ASAP - hours to days
**Prerequisites**: Security issue reported
**Related docs**: [SECURITY.md](SECURITY.md), [INCIDENT_RESPONSE.md](INCIDENT_RESPONSE.md)

### 🚨 IMPORTANT: Confidentiality

Security issues are **NEVER** discussed in public channels until fixed and disclosed responsibly.

### Step-by-Step

#### Immediate Response (Within 1 hour)

- [ ] **Acknowledge receipt** to reporter privately (security@... email)
- [ ] **Assess severity** using CVSS or similar framework:
  - 🔴 Critical: Remote code execution, data breach (ACT NOW)
  - 🟠 High: Authentication bypass, privilege escalation (24-48 hours)
  - 🟡 Medium: Information disclosure, DoS (1-2 weeks)
  - 🟢 Low: Minor issues (regular release cycle)
- [ ] **Alert security team** (private channel)
- [ ] **DO NOT** commit fixes to public repo yet

#### Investigation (Hours to days, depending on severity)

- [ ] **Reproduce the issue** in isolated environment
- [ ] **Understand scope** - what versions affected? How many users?
- [ ] **Assess impact** - what data is at risk? What actions are possible?
- [ ] **Identify root cause**
- [ ] **Keep reporter updated** - at least every 48 hours

#### Fix Development (In private)

- [ ] **Develop patch** in private repository or branch
- [ ] **Test thoroughly** - don't introduce new issues!
- [ ] **Prepare backports** for supported versions
- [ ] **Draft security advisory** - describe issue and fix
- [ ] **Coordinate disclosure date** with reporter (typically 90 days)

#### Coordinated Disclosure

- [ ] **Prepare release** with security fix
- [ ] **Write public advisory** with:
  - Description of vulnerability
  - Affected versions
  - Fixed versions
  - Workarounds if any
  - Credits to reporter
  - CVE number if applicable
- [ ] **Notify affected users** before public announcement if possible
- [ ] **Publish fix and advisory** simultaneously
- [ ] **Update security page** and [SECURITY.md](SECURITY.md)

#### Post-Incident

- [ ] **Thank the reporter** publicly (with permission) and privately
- [ ] **Run retrospective** - how could we prevent this class of issue?
- [ ] **Update security practices** based on learnings
- [ ] **Consider security audit** if pattern of issues

### Common Pitfalls

❌ **Discussing publicly** → Always private until coordinated disclosure
❌ **Rushing incomplete fix** → Take time to fix it right
❌ **Blaming the reporter** → Thank them for responsible disclosure!
❌ **No communication** → Keep reporter and users updated
❌ **Forgetting backports** → Users on old versions need fixes too

---

## Playbook 10: Managing Conflict

**Goal**: De-escalate and resolve interpersonal conflict constructively
**Time**: Varies greatly
**Prerequisites**: Conflict situation, willingness to engage
**Related docs**: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [COMMUNICATION.md](COMMUNICATION.md)

### When to Use This Playbook

- Disagreements have become personal
- Communication has broken down
- People are talking past each other
- Emotions are running high
- Team dynamics are suffering

### Early Intervention (When tensions rise)

#### For Participants

- [ ] **Take a break** - step away from the keyboard for 30+ minutes
- [ ] **Assume positive intent** - they probably don't intend harm
- [ ] **Separate person from problem** - critique ideas, not people
- [ ] **Use "I" statements**: "I feel..." not "You always..."
- [ ] **Ask questions**: "Help me understand your perspective..."
- [ ] **Find common ground** - what do we agree on?

#### For Observers

- [ ] **Don't pile on** - adding more voices can inflame
- [ ] **DM privately** offering to mediate if helpful
- [ ] **Report to moderators** if violating [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [ ] **Model good behavior** - show how to disagree respectfully

### Escalation (If early intervention doesn't work)

#### Request Mediation

- [ ] **Identify neutral mediator** - someone both parties trust
- [ ] **Move to private channel** - public arguments help no one
- [ ] **Set ground rules**:
  - One person speaks at a time
  - No personal attacks
  - Goal is mutual understanding, not "winning"
  - Commit to good-faith effort

#### Mediation Session (60-90 min)

- [ ] **Each person shares their perspective** (10-15 min each)
  - Mediator listens and paraphrases back
  - Other person listens without interrupting
- [ ] **Identify underlying needs** (not positions)
  - What does each person really need?
  - What are they afraid of?
- [ ] **Find creative solutions** that address both needs
- [ ] **Agree on path forward** - specific, concrete actions
- [ ] **Schedule follow-up** - check if agreement is working

### If Mediation Fails

- [ ] **Escalate to Code of Conduct committee** per [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [ ] **Implement boundaries** - work in different areas, limited interaction
- [ ] **Consider consequences** - warnings, temporary bans, removal if severe

### Post-Resolution

- [ ] **Follow through** on commitments
- [ ] **Rebuild trust** gradually through consistent actions
- [ ] **Learn from it** - what could prevent this next time?
- [ ] **Forgive** - holding grudges poisons communities

### Prevention

Better to prevent conflict than resolve it:
- [ ] **Clear expectations** - [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), contribution guidelines
- [ ] **Overcommunicate** - especially in text-based communication
- [ ] **Address small issues early** - don't let them fester
- [ ] **Build relationships** - easier to resolve conflict with people you know
- [ ] **Model vulnerability** - admitting mistakes creates safety

---

## Playbook 11: Releasing a New Version

**Goal**: Ship a new release smoothly and safely
**Time**: 2-4 hours
**Prerequisites**: Releasable code, release permissions
**Related docs**: [RELEASES.md](RELEASES.md), [TESTING.md](TESTING.md)

See [RELEASES.md](RELEASES.md) for comprehensive release process. Quick checklist:

### Pre-Release (Days before)

- [ ] **Code freeze** - no new features, only bug fixes
- [ ] **Test thoroughly** - run full test suite, manual testing
- [ ] **Update dependencies** and check for security issues
- [ ] **Review breaking changes** and update [DEPRECATION.md](DEPRECATION.md)
- [ ] **Draft release notes** highlighting key changes
- [ ] **Prepare documentation** updates for new features

### Release Day

**Morning**:
- [ ] **Final test run** - all CI green
- [ ] **Update CHANGELOG.md** with version and date
- [ ] **Bump version number** following semantic versioning
- [ ] **Create release branch** if needed
- [ ] **Tag release** (e.g., `v1.2.0`)

**Afternoon**:
- [ ] **Build release artifacts** and verify
- [ ] **Publish to package registries** (npm, PyPI, etc.)
- [ ] **Deploy documentation** updates
- [ ] **Create GitHub Release** with notes
- [ ] **Announce** in community channels, blog, social media
- [ ] **Update website** if applicable

**Evening**:
- [ ] **Monitor** for issues - support channels, error tracking
- [ ] **Be available** for critical issues
- [ ] **Celebrate** with the team! 🎉

### Post-Release (Next day)

- [ ] **Check metrics** - downloads, errors, user feedback
- [ ] **Address critical issues** quickly (hotfix if needed)
- [ ] **Thank contributors** whose work is in this release
- [ ] **Retrospective** - what went well, what to improve?
- [ ] **Update roadmap** - mark completed items, plan next release

### If Something Goes Wrong

- [ ] **Assess severity** - is it critical?
- [ ] **Communicate transparently** - acknowledge the issue
- [ ] **Hotfix or rollback** - depending on severity
- [ ] **Post-incident review** - learn from it

---

## Playbook 12: Deprecating a Feature

**Goal**: Sunset a feature gracefully with minimal user pain
**Time**: 3-6 months
**Prerequisites**: Decision to deprecate, migration path
**Related docs**: [DEPRECATION.md](DEPRECATION.md), [RELEASES.md](RELEASES.md)

### Month 1: Planning & Announcement

- [ ] **Document reason** - why are we deprecating?
- [ ] **Create migration path** - how should users transition?
- [ ] **Set timeline** - when will it be removed? (Ideally 3-6 months notice)
- [ ] **Write migration guide** - step-by-step instructions
- [ ] **Announce deprecation**:
  ```markdown
  ## 🚨 Deprecation Notice: [Feature Name]

  **Timeline**: Deprecated in v1.5 (Jan 2025), will be removed in v2.0 (June 2025)

  **Reason**: [Why we're doing this]

  **Migration Path**: [How to transition]

  **Questions?**: [Where to get help]
  ```

### Months 2-4: Migration Support

- [ ] **Add deprecation warnings** in code that trigger when feature is used
- [ ] **Update documentation** to show new approach
- [ ] **Write blog post** with migration examples
- [ ] **Offer office hours** for questions
- [ ] **Monitor usage** - how many users still using deprecated feature?
- [ ] **Proactively reach out** to high-impact users

### Month 5: Final Warning

- [ ] **Louder deprecation warnings** - make it clear removal is soon
- [ ] **Final migration deadline** announcement
- [ ] **Offer to help** stragglers migrate
- [ ] **Document breaking change** in upcoming release notes

### Month 6: Removal

- [ ] **Remove deprecated code** in major version bump
- [ ] **Release notes** prominently feature removal
- [ ] **Keep migration guide** available indefinitely
- [ ] **Be responsive** to any users caught off-guard

### Common Pitfalls

❌ **Surprise removal** → Always give ample notice
❌ **No migration path** → Make transition easy
❌ **Removing in minor version** → Breaking changes require major version bump
❌ **Deprecating too much at once** → Pace changes to avoid migration fatigue

---

## 🌟 Continuous Improvement

These playbooks are living documents. As you use them:

- **Adapt** to your context - they're guides, not rigid rules
- **Share learnings** - what worked? What didn't?
- **Propose updates** - submit PRs to improve these playbooks
- **Create new playbooks** - what scenarios are we missing?

Remember: Playbooks capture wisdom from experience. Every time you navigate a scenario, you're adding to our collective knowledge. 💚

---

## 📚 Related Resources

- [GETTING_STARTED.md](GETTING_STARTED.md) - Your first steps
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [CODE_REVIEW.md](CODE_REVIEW.md) - Code review guidelines
- [MENTORSHIP.md](MENTORSHIP.md) - Mentorship programs
- [EVENTS.md](EVENTS.md) - Event planning
- [GOVERNANCE.md](GOVERNANCE.md) - How we make decisions
- [TEMPLATES.md](TEMPLATES.md) - Templates for common tasks

---

*These playbooks are maintained with consciousness and care by the Luminous Dynamics community. Questions? Open a Discussion! 💚✨*
