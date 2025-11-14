# 📖 Documentation Style Guide

> "Clarity is kindness. Precision is respect. Consistency is care."

Welcome to the Luminous Dynamics documentation style guide. This guide ensures consistency, clarity, and consciousness-first principles across all 15 projects.

---

## 🎯 Purpose and Scope

### Why This Guide Exists

- **Consistency**: Users navigate 15+ projects—consistent docs reduce cognitive load
- **Quality**: High standards reflect our technical excellence and values
- **Inclusivity**: Clear writing serves diverse audiences and accessibility needs
- **Efficiency**: Templates and standards accelerate documentation creation
- **Consciousness**: Language shapes thought—thoughtful language shapes conscious technology

### Scope

This guide applies to:
- All Markdown documentation (README, guides, tutorials)
- Code comments and docstrings
- Issue and PR templates
- Website content
- API documentation
- Community communications

---

## 🎨 Tone and Voice

### Core Principles

1. **Welcoming but Technical**
   - Approachable to newcomers, detailed for experts
   - Explain concepts clearly without dumbing down
   - Balance warmth with precision

2. **Consciousness-First**
   - Honor ERC principles in language choices
   - Avoid extractive, violent, or mechanistic metaphors
   - Use collaborative, organic, empowering language

3. **Direct and Honest**
   - Say what you mean clearly
   - Acknowledge complexity and limitations
   - No hype, no marketing speak, no exaggeration

4. **Respectful and Inclusive**
   - Use gender-neutral language (they/them as singular)
   - Avoid ableist language (see [Language Guidelines](#language-guidelines))
   - Consider global English speakers (avoid idioms)

### Voice Examples

✅ **Good:**
```markdown
The Mycelix Protocol achieves Byzantine fault tolerance through the MATL/0TML
trust layer. This allows the network to maintain integrity even when 30% of
nodes behave maliciously.
```

❌ **Avoid:**
```markdown
Mycelix CRUSHES Byzantine faults with our REVOLUTIONARY trust layer that
DESTROYS malicious nodes!
```

✅ **Good:**
```markdown
If you're new to distributed systems, we recommend starting with our
[Introduction to Federated Learning](./LEARNING.md#federated-learning) guide.
```

❌ **Avoid:**
```markdown
Even a beginner can understand this simple concept.
```

---

## 📝 Document Structure

### Standard Template

Every major documentation file should follow this structure:

```markdown
# [Emoji] Title

> "[Relevant quote or one-line description]"

[Brief 1-2 paragraph introduction]

---

## Table of Contents (for docs >200 lines)

## Main Sections

### Subsections

---

## 📚 Related Resources

## 🤝 Contributing

## 💬 Questions?

---

**Last Updated**: [Date]
**Maintained by**: [Team/Person]
```

### File Naming Conventions

- **ALL_CAPS.md** for organization-wide docs (README.md, CONTRIBUTING.md)
- **kebab-case.md** for guides and tutorials (getting-started.md)
- **PascalCase.md** for documentation within projects (UserGuide.md)
- Use descriptive names: `federation-setup.md` not `setup.md`

### Header Hierarchy

- **H1 (`#`)**: Document title only (one per file)
- **H2 (`##`)**: Major sections
- **H3 (`###`)**: Subsections
- **H4 (`####`)**: Rare—only when necessary for clarity
- Never skip levels (don't go H2 → H4)

---

## 🎯 Formatting Conventions

### Emphasis

- **Bold** for UI elements, important terms, emphasis: `**bold**`
- *Italic* for gentle emphasis, book/paper titles: `*italic*`
- `Code` for code, commands, file names, variables: `` `code` ``
- ***Bold italic*** sparingly for critical warnings: `***bold italic***`

### Lists

**Unordered Lists:**
```markdown
- First level
  - Second level (2 spaces)
    - Third level (4 spaces)
- Use `-` consistently (not `*` or `+`)
```

**Ordered Lists:**
```markdown
1. Use `1.` for all items (auto-numbering)
2. Not `1)` or `1:`
3. Maintain consistent formatting
```

**Task Lists:**
```markdown
- [ ] Incomplete task
- [x] Completed task
```

### Code Blocks

Always specify language for syntax highlighting:

````markdown
```python
def consciousness_first():
    return "Technology serving awareness"
```

```bash
npm install @luminous/core
```

```javascript
// For multi-language examples, use separate blocks
const api = new LuminousAPI();
```
````

For terminal commands, use `bash` and include `$` prefix:

```bash
$ git clone https://github.com/Luminous-Dynamics/luminous-dynamics.git
$ cd luminous-dynamics
```

### Links

**Internal Links:**
```markdown
See [Getting Started](./GETTING_STARTED.md) for details.
See the [API Reference](../api/reference.md#endpoints).
```

**External Links:**
```markdown
Learn more about [Holochain](https://holochain.org/).
```

**Reference-Style Links** (for repeated URLs):
```markdown
The [Mycelix Protocol][mycelix] uses [federated learning][fed-learning].

[mycelix]: https://github.com/Luminous-Dynamics/Mycelix-Core
[fed-learning]: ./GLOSSARY.md#federated-learning
```

### Tables

Use tables for structured comparisons:

```markdown
| Feature | Mycelix | Traditional ML |
|---------|---------|----------------|
| Data Privacy | ✅ Local | ❌ Centralized |
| Byzantine Resistance | ✅ 100% | ⚠️ Limited |
| Latency | ✅ 0.7ms | ❌ 15ms |
```

Align for readability in source:
- Left-align text columns
- Center-align icon/emoji columns
- Right-align number columns

---

## 🌟 Emoji Guidelines

### Philosophy

Emojis enhance scannability and add warmth **when used purposefully**. They are visual anchors, not decoration.

### Standard Usage

**Section Headers:**
- 🎯 Purpose, Goals, Objectives
- 📖 Documentation, Learning, Resources
- 🚀 Quick Start, Getting Started, Launch
- 🏗️ Architecture, Structure, Design
- 🔧 Configuration, Setup, Tools
- 🤝 Contributing, Community, Collaboration
- 💬 Questions, Discussion, Support
- 🔒 Security, Privacy, Safety
- ⚡ Performance, Speed, Optimization
- 🧬 Core Concepts, Fundamentals
- 🌍 Ecosystem, Projects, Landscape
- 💚 Values, Principles, Philosophy
- 📊 Metrics, Analytics, Data
- 🎨 Design, UI/UX, Aesthetics
- ⚠️ Warnings, Cautions, Important Notes

**Inline Usage:**
- ✅ Success, Good, Recommended
- ❌ Failure, Bad, Avoid
- ⚠️ Warning, Caution, Deprecated
- 💡 Tip, Idea, Suggestion
- 🎓 Learning, Educational
- 🔍 Search, Investigate, Research

**Project Identifiers:**
- 🧬 Luminous Dynamics (main ecosystem)
- ⚡ Mycelix Protocol
- 🌍 Terra Atlas
- 🎭 Simulacra
- 💎 Sacred Economy projects

### When NOT to Use Emojis

❌ **Avoid:**
- In code comments (breaks some IDEs)
- In technical specifications (unless standard symbols)
- Excessively (more than one per paragraph)
- As bullet points (use `-` instead)
- In formal API documentation

---

## 📚 Terminology and Language

### Use the Glossary

Always link to [GLOSSARY.md](./GLOSSARY.md) when introducing technical terms:

```markdown
The [Mycelix Protocol](./GLOSSARY.md#mycelix-protocol) uses [federated
learning](./GLOSSARY.md#federated-learning) to enable privacy-preserving AI.
```

After first link, use the term normally.

### Preferred Terminology

| ✅ Use | ❌ Avoid | Why |
|--------|----------|-----|
| consciousness-first | AI-powered | Centers awareness over automation |
| participant, contributor | user | More collaborative, less extractive |
| sacred reciprocity | transaction | Honors gift economy values |
| collective intelligence | crowdsourcing | More respectful of human agency |
| they/them (singular) | he/she | Gender-inclusive |
| accessible | handicap-accessible | Person-first language |

### Language Guidelines

**Avoid Violent/Militaristic Metaphors:**
- ❌ "kill the process" → ✅ "stop the process"
- ❌ "nuke the database" → ✅ "reset the database"
- ❌ "target users" → ✅ "serve participants"
- ❌ "capture attention" → ✅ "invite engagement"

**Avoid Ableist Language:**
- ❌ "sanity check" → ✅ "validation check"
- ❌ "dummy variable" → ✅ "placeholder variable"
- ❌ "crippled performance" → ✅ "degraded performance"
- ❌ "blind copy" → ✅ "hidden copy"

**Avoid Master/Slave Terminology:**
- ✅ "primary/replica" or "leader/follower"
- ✅ "main branch" (not "master branch")

---

## 💻 Code Examples

### Example Quality Standards

1. **Complete**: Examples should run without modification
2. **Realistic**: Show real-world usage, not toy examples
3. **Explained**: Add comments for non-obvious code
4. **Safe**: No hardcoded credentials, realistic but safe data
5. **ERC-Aligned**: Variable names and logic reflect our values

### Example Format

````markdown
### Example: Setting Up Mycelix Federation

This example demonstrates how to initialize a Mycelix federation with Byzantine
fault tolerance:

```python
from mycelix import Federation, TrustLayer

# Initialize federation with consciousness-first principles
federation = Federation(
    name="community-health-research",
    trust_layer=TrustLayer.MATL,  # Byzantine resistance
    privacy_mode="local-only",     # Data never leaves devices
)

# Configure learning parameters
federation.configure(
    learning_rate=0.01,
    batch_size=32,
    byzantine_threshold=0.3,  # Tolerate up to 30% malicious nodes
)

# Start federated training
federation.train(
    model=health_model,
    epochs=10,
    participants_required=100,
)
```

**Expected Output:**
```
✓ Federation initialized: community-health-research
✓ Trust layer active: MATL/0TML
✓ 127 participants joined
✓ Training complete: 99.2% accuracy, 0 Byzantine attacks detected
```

**Key Points:**
- The `trust_layer` parameter enables Byzantine fault tolerance
- `privacy_mode="local-only"` ensures data never leaves participant devices
- The federation automatically detects and excludes malicious nodes
````

### Anti-Patterns

❌ **Avoid Unexplained Magic:**
```python
# What does this do? Why these values?
f = Fed("x", TL.M, "l")
f.c(0.01, 32, 0.3)
```

❌ **Avoid Incomplete Examples:**
```python
# Where does `model` come from?
federation.train(model)
```

❌ **Avoid Dangerous Examples:**
```python
# Never show actual credentials
api_key = "sk_live_abc123xyz789"  # ❌ BAD
```

---

## 🔗 Cross-Linking Best Practices

### Link Generously

Documentation is a web, not a tree. Link to related concepts:

```markdown
The [Mycelix Protocol](https://github.com/Luminous-Dynamics/Mycelix-Core)
builds on principles from [federated learning](./GLOSSARY.md#federated-learning)
while adding [Byzantine fault tolerance](./GLOSSARY.md#byzantine-fault-tolerance).

For implementation details, see:
- [Architecture Overview](../docs/architecture.md)
- [API Reference](../docs/api.md)
- [Tutorial: Your First Federation](../tutorials/first-federation.md)
```

### Link Types

1. **Navigational Links**: Help users find what they need next
2. **Conceptual Links**: Explain related ideas (use GLOSSARY)
3. **Reference Links**: Point to detailed specifications
4. **External Links**: Connect to broader ecosystem

### Related Resources Section

End major docs with related links:

```markdown
---

## 📚 Related Resources

**Getting Started:**
- [Installation Guide](./INSTALL.md)
- [Quick Start Tutorial](./QUICKSTART.md)

**Deep Dives:**
- [Architecture Decision Records](./ADR.md)
- [Security Model](./SECURITY.md)

**Community:**
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
```

---

## ⚠️ Warnings and Notices

### Callout Boxes

Use blockquotes with emoji for important notices:

**General Information:**
```markdown
> 💡 **Tip:** The Mycelix Protocol works best with at least 100 participants.
```

**Warnings:**
```markdown
> ⚠️ **Warning:** Changing the `byzantine_threshold` affects security guarantees.
```

**Critical:**
```markdown
> 🚨 **Critical:** Never commit API keys to public repositories.
```

**Deprecation:**
```markdown
> ⚠️ **Deprecated:** This API will be removed in v3.0. Use `newMethod()` instead.
```

---

## ✍️ Writing Process

### Before You Write

1. **Define Audience**: Who is this for? (newcomers, experts, contributors?)
2. **Define Purpose**: What should they be able to do after reading?
3. **Check Existing Docs**: Are you duplicating? Should you link instead?
4. **Outline First**: Structure before details

### While You Write

1. **One Idea Per Paragraph**: If you use "also" or "additionally", consider splitting
2. **Active Voice**: "The protocol detects attacks" not "Attacks are detected"
3. **Show, Don't Tell**: Use examples liberally
4. **Link Generously**: Connect concepts

### After You Write

1. **Read Aloud**: Awkward? Revise.
2. **Check Links**: Do they work? Are they necessary?
3. **Run Spell Check**: Typos reduce trust
4. **Test Examples**: Do code examples actually run?
5. **Ask for Feedback**: Fresh eyes catch issues

---

## 📊 Before and After Examples

### Example 1: Technical Explanation

❌ **Before:**
```markdown
Mycelix is really good at detecting bad nodes. It's super fast.
```

✅ **After:**
```markdown
The Mycelix Protocol achieves 100% Byzantine fault detection with 0.7ms
latency—21.4× faster than traditional federated learning systems. This is
enabled by the MATL/0TML trust layer, which maintains cryptographic proofs
of participant behavior.

See [METRICS.md](./METRICS.md#mycelix-performance) for benchmark details.
```

**Why Better:** Specific numbers, technical explanation, links to evidence.

### Example 2: Getting Started Section

❌ **Before:**
```markdown
## Installation

Just install it:
npm install @luminous/core
```

✅ **After:**
```markdown
## 🚀 Installation

### Prerequisites

- Node.js 18+ or Python 3.9+
- 4GB RAM minimum
- Git for version control

### Install via npm

```bash
$ npm install @luminous/core
```

### Install via pip

```bash
$ pip install luminous-core
```

### Verify Installation

```bash
$ luminous --version
luminous-core v2.1.0
```

**Next Steps:** See [Quick Start Tutorial](./QUICKSTART.md) to build your
first consciousness-first application.
```

**Why Better:** Clear prerequisites, multiple install methods, verification step, clear next action.

### Example 3: API Documentation

❌ **Before:**
```markdown
`createFederation(opts)` - Creates a federation
```

✅ **After:**
```markdown
### `createFederation(options)`

Creates a new federated learning network with Byzantine fault tolerance.

**Parameters:**
- `options` (Object)
  - `name` (string, required): Human-readable federation identifier
  - `trustLayer` (TrustLayer, optional): Defense mechanism. Default: `TrustLayer.MATL`
  - `privacyMode` (string, optional): Data handling policy. Options: `"local-only"`, `"encrypted-shared"`. Default: `"local-only"`

**Returns:** `Federation` instance

**Throws:**
- `ValidationError` if `name` is empty
- `NetworkError` if unable to initialize trust layer

**Example:**
```javascript
const federation = createFederation({
  name: "healthcare-research",
  trustLayer: TrustLayer.MATL,
  privacyMode: "local-only"
});
```

**See Also:**
- [Federation API Reference](./api/federation.md)
- [Trust Layer Options](./security/trust-layers.md)
```

**Why Better:** Complete parameter documentation, error cases, working example, related links.

---

## 🎓 Documentation Types

### README Files

**Purpose:** First impression, orientation, quick start

**Must Have:**
- Project description (what, why, for whom)
- Quick start example (<5 minutes to first success)
- Link to full documentation
- Installation instructions
- Basic usage example
- Links to contributing, license, support

**Length:** 100-300 lines for project READMEs

### Tutorials

**Purpose:** Learning by doing

**Structure:**
1. Clear learning objective
2. Prerequisites listed
3. Step-by-step instructions (numbered)
4. Expected output at each step
5. Troubleshooting section
6. Next steps

**Tone:** Patient, encouraging, detailed

### Reference Documentation

**Purpose:** Complete technical specification

**Must Have:**
- Every parameter documented
- Return values specified
- Error conditions listed
- Examples for each method
- Cross-references to related APIs

**Tone:** Precise, exhaustive, neutral

### Guides

**Purpose:** Explain concepts and best practices

**Structure:**
- Conceptual explanation
- Why it matters
- When to use (and when not to)
- Examples showing principles
- Anti-patterns and gotchas

**Tone:** Explanatory, practical, opinionated

---

## 🤝 Contributing to Documentation

### Small Fixes

Typos, broken links, small clarifications:
1. Click "Edit" on GitHub
2. Make change
3. Submit PR with description

### Major Additions

New pages, restructuring, new sections:
1. Open issue first to discuss approach
2. Reference this style guide
3. Request review from docs maintainers
4. Update navigation/index pages

### Documentation Review Checklist

When reviewing documentation PRs, check:

- [ ] Follows tone and voice guidelines
- [ ] Uses consistent formatting (headers, lists, code blocks)
- [ ] Includes working code examples
- [ ] Links to related resources
- [ ] Free of typos and grammatical errors
- [ ] Accessible language (defined terms, clear structure)
- [ ] Appropriate emoji usage
- [ ] Follows file naming conventions
- [ ] Includes "Last Updated" date

---

## 🔧 Tools and Resources

### Recommended Tools

- **Linters**: [markdownlint](https://github.com/DavidAnson/markdownlint) for consistent formatting
- **Link Checkers**: [markdown-link-check](https://github.com/tcort/markdown-link-check)
- **Spell Check**: [cspell](https://cspell.org/) with custom dictionary
- **Preview**: GitHub's preview, [Marked](https://marked2app.com/), or VS Code

### Custom Dictionary

Common terms to add to spell checkers:
- Mycelix, MATL, 0TML
- Holochain, hApp
- ERC (Evolving Resonant Co-creationism)
- consciousness-first
- Terra Atlas, Simulacra, Luminos
- Byzantine, federated
- Luminous Dynamics

### Writing Resources

- [GLOSSARY.md](./GLOSSARY.md) - Luminous Dynamics terminology
- [Divio Documentation System](https://documentation.divio.com/) - Tutorials vs. guides vs. reference
- [Google Developer Documentation Style Guide](https://developers.google.com/style)
- [Write the Docs](https://www.writethedocs.org/) - Community and resources

---

## 📚 Related Resources

- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - How to contribute to projects
- **[GLOSSARY.md](./GLOSSARY.md)** - Terminology definitions
- **[GETTING_STARTED.md](./GETTING_STARTED.md)** - Newcomer onboarding
- **[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)** - Community standards

---

## 💬 Questions About This Guide?

- Open an issue: [.github repository](https://github.com/Luminous-Dynamics/.github/issues)
- Ask in discussions: [Community Discussions](https://github.com/orgs/Luminous-Dynamics/discussions)
- Suggest improvements via PR

---

**Last Updated**: 2025-01-14
**Maintained by**: Documentation Working Group

---

> "The quality of our documentation reflects the care we have for those who will use our technology. Every word is an act of service." 💚
