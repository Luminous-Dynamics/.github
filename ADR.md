# Architecture Decision Records (ADR)

*"In unity we code, in love we debug, in consciousness we deploy"* ✨

## What are ADRs?

Architecture Decision Records document significant technical and architectural decisions made in Luminous Dynamics projects. They provide context for why decisions were made, helping current and future contributors understand the reasoning.

## Why ADRs?

- **Preserve context**: Understand decisions years later
- **Onboard efficiently**: New contributors learn reasoning quickly
- **Avoid revisiting**: Don't rehash settled decisions
- **Track evolution**: See how thinking has changed
- **Transparency**: Community understands technical direction

## ADR Process

### When to Create an ADR

Create an ADR when making decisions about:
- **Architecture**: System design, component boundaries
- **Technology choices**: Languages, frameworks, platforms
- **Patterns**: Design patterns, coding conventions
- **Infrastructure**: Hosting, deployment, CI/CD
- **Security**: Authentication, encryption, data protection
- **Philosophy integration**: How ERC principles apply technically

### When NOT to Create an ADR

Skip ADRs for:
- Trivial decisions easily reversed
- Implementation details (not architecture)
- Temporary solutions
- Obvious choices with clear consensus

## ADR Format

Use this template for all ADRs:

```markdown
# ADR-[NUMBER]: [TITLE]

**Status**: [Proposed | Accepted | Deprecated | Superseded by ADR-XXX]
**Date**: YYYY-MM-DD
**Deciders**: [Names or roles]
**ERC Alignment**: [How this aligns with consciousness-first principles]

## Context

What is the issue we're addressing? What factors are we considering?

## Decision

What decision did we make? Be specific and concrete.

## Consequences

What becomes easier or harder as a result?

### Positive Consequences
- Benefit 1
- Benefit 2

### Negative Consequences
- Drawback 1
- Drawback 2

### Neutral Consequences
- Impact 1
- Impact 2

## Alternatives Considered

What other options did we evaluate?

### Alternative 1: [Name]
**Pros**: ...
**Cons**: ...
**Why not chosen**: ...

### Alternative 2: [Name]
**Pros**: ...
**Cons**: ...
**Why not chosen**: ...

## ERC Consciousness-First Analysis

How does this decision:
- **Preserve awareness**: Does it respect user agency?
- **Serve all beings**: Is it radically accessible?
- **Enable regeneration**: Does it support community ownership?
- **Embody sacred development**: Was it made with wisdom and intention?
- **Honor gift economy**: Does it avoid extraction?

## References

- Links to relevant discussions
- Related documentation
- External resources
- Similar decisions in other projects

## Notes

Additional context, concerns, or follow-up needed.
```

## Example ADR

### ADR-001: Use Holochain for Mycelix Ecosystem

**Status**: Accepted
**Date**: 2025-11-14
**Deciders**: Core team, Mycelix contributors
**ERC Alignment**: Agent-centric architecture aligns with consciousness-first principles

#### Context

Mycelix ecosystem (Mail, Music, Marketplace) needs a distributed platform that:
- Enables true data sovereignty
- Scales without centralized servers
- Resists censorship and single points of failure
- Aligns with consciousness-first values
- Supports trust and reputation systems

Options considered: Blockchain, IPFS, traditional P2P, Holochain.

#### Decision

Build Mycelix ecosystem on **Holochain** as the primary distributed platform.

#### Consequences

**Positive**:
- User data sovereignty (agent-centric design)
- Scalability without blockchain bloat
- Energy efficient (no mining)
- Built-in DHT for data distribution
- Cryptographic verification (Ed25519)
- Aligns with consciousness-first values

**Negative**:
- Smaller ecosystem than blockchain
- Steeper learning curve for contributors
- Less mature tooling than established platforms
- Network effects take time to build

**Neutral**:
- Different mental model than client-server
- Requires WSL2 on Windows (NSFW helps here)

#### Alternatives Considered

**Alternative 1: Ethereum/Blockchain**
- **Pros**: Large ecosystem, proven, financial integration
- **Cons**: Energy intensive, high costs, surveillance-like transparency, not truly distributed
- **Why not**: Violates consciousness-first and regenerative economics principles

**Alternative 2: IPFS**
- **Pros**: Proven distributed storage, good tooling
- **Cons**: Storage-focused, no built-in compute or trust layer
- **Why not**: Would need significant additional infrastructure

**Alternative 3: Traditional P2P**
- **Pros**: Maximum control, proven patterns
- **Cons**: Massive development effort, no ecosystem
- **Why not**: Reinventing the wheel

#### ERC Consciousness-First Analysis

- **Preserve awareness**: Agent-centric design puts users in control
- **Serve all beings**: Lower barriers than blockchain (no tokens required)
- **Enable regeneration**: No extractive mining or token economics
- **Embody sacred development**: Thoughtful platform choice with long-term vision
- **Honor gift economy**: Platform design supports mutual benefit over extraction

#### References

- [Holochain documentation](https://developer.holochain.org/)
- [Agent-Centric vs Data-Centric](https://developer.holochain.org/concepts/2_application_architecture/)
- Mycelix-Core implementation proving viability
- Community discussions on platform choice

#### Notes

This decision enables a unified ecosystem across Mail, Music, and Marketplace while maintaining consciousness-first principles. Future projects should evaluate Holochain as first option for distributed applications.

---

## ADR Storage

### Location

ADRs are stored in project repositories:

```
repository-name/
└── docs/
    └── adr/
        ├── README.md
        ├── 001-use-holochain.md
        ├── 002-implement-matl.md
        └── 003-swiss-foundation-governance.md
```

### Organization-Wide ADRs

For decisions affecting multiple projects, store in `.github` repository:

```
.github/
└── ADR/
    ├── README.md
    └── 001-example.md
```

## ADR Lifecycle

### 1. Propose

- Create ADR with **Status: Proposed**
- Open PR for discussion
- Community provides feedback
- Iterate based on input

### 2. Accept

- Achieve consensus
- Update **Status: Accepted**
- Merge PR
- Communicate decision
- Implement

### 3. Deprecate (if needed)

- When decision becomes obsolete
- Update **Status: Deprecated**
- Explain why in Notes section
- Keep for historical context

### 4. Supersede (if needed)

- When new ADR replaces old one
- Update **Status: Superseded by ADR-XXX**
- Link to new ADR
- Explain what changed

## ADR Numbering

- **Sequential**: ADR-001, ADR-002, ADR-003...
- **Per-project**: Each project starts at 001
- **Organization-wide**: Separate sequence for org-level decisions
- **Never reuse numbers**: Even for deprecated ADRs

## ADR Review Process

### For Individual Projects

1. Draft ADR in PR
2. Label PR with `adr`
3. Maintainers review
4. Community discussion (minimum 7 days)
5. Consensus or maintainer decision
6. Merge and implement

### For Organization-Wide

1. Draft ADR in PR to `.github`
2. Post in Discussions
3. Extended review (minimum 14 days)
4. Core team + community consensus
5. Merge and communicate
6. Projects adopt as appropriate

## ERC Integration

Every ADR must include **ERC Consciousness-First Analysis** section showing how the decision aligns with our five core principles. This ensures technical decisions stay grounded in our values.

## Best Practices

### Writing ADRs

- **Be concise**: One page ideally, two max
- **Be specific**: "We will use PostgreSQL" not "We will use a database"
- **Include dates**: Context changes over time
- **List alternatives**: Show you considered options
- **Explain reasoning**: Not just what, but why
- **Accept tradeoffs**: Acknowledge downsides honestly

### Reviewing ADRs

- **Question assumptions**: Challenge if needed
- **Suggest alternatives**: If important option missed
- **Consider long-term**: Think beyond immediate needs
- **Evaluate ERC alignment**: Does it serve consciousness-first values?
- **Be constructive**: Help improve, don't just criticize

### Using ADRs

- **Reference in PRs**: Link to relevant ADRs
- **Update when learning**: Add notes about implementation experience
- **Don't fear reversal**: It's okay to supersede if context changes
- **Teach newcomers**: Point to ADRs during onboarding

## Common ADR Topics

### Technology Choices
- Programming languages
- Frameworks and libraries
- Databases and storage
- Hosting and infrastructure
- Development tools

### Architecture Patterns
- System boundaries
- Communication protocols
- Data flow patterns
- Error handling strategies
- Security architectures

### Process Decisions
- Git workflows
- Release processes
- Testing strategies
- Code review standards
- Documentation approaches

### ERC Applications
- How consciousness-first manifests in code
- Gift economy platform features
- Community ownership transitions
- Regenerative design patterns
- Sacred development practices

## ADR Templates

### Quick Decision Template

For less complex decisions:

```markdown
# ADR-[NUMBER]: [TITLE]

**Status**: Accepted
**Date**: YYYY-MM-DD

## Decision
[One paragraph: what we decided]

## Why
[One paragraph: key reasoning]

## ERC Alignment
[How this serves consciousness-first principles]
```

### Full Template

Use the comprehensive format shown above for significant architectural decisions.

## Questions About ADRs?

- Review examples in project repositories
- Ask in Discussions with `[ADR]` tag
- Check our [FAQ](./FAQ.md)
- Email: invest@luminousdynamics.org

---

**Last Updated**: November 2025
**Next Review**: Quarterly

*Documenting decisions with consciousness and care* 💚✨

## Related Documents

- [GOVERNANCE.md](./GOVERNANCE.md) - Decision-making process
- [CONTRIBUTING.md](./CONTRIBUTING.md) - How to propose ADRs
- [VISION_AND_ROADMAP.md](./VISION_AND_ROADMAP.md) - Strategic direction
- [RESEARCH.md](./RESEARCH.md) - Research decisions
