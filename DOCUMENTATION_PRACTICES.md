# 📖 Documentation Practices

> "Code is read more than it is written. Documentation is read even more than code."

*Last updated: January 2025*

This document outlines our **documentation philosophy and practices**—how we create, maintain, and evolve documentation that serves users, developers, and operators. Good documentation is essential for project success, onboarding, and long-term sustainability.

---

## 🎯 Documentation Philosophy

### Why Documentation Matters

**Without documentation**:
- ❌ Tribal knowledge (information lost when people leave)
- ❌ Repeated questions ("how do I...")
- ❌ Slow onboarding (weeks to get started)
- ❌ Fear of change (no one knows how it works)
- ❌ Poor adoption (people can't figure out how to use it)

**With good documentation**:
- ✅ Self-service learning
- ✅ Fast onboarding (hours, not weeks)
- ✅ Confident changes (documented behavior)
- ✅ Higher adoption (clear value proposition)
- ✅ Reduced support burden

### Documentation Principles

1. **Start with why**: Explain the purpose before the how
2. **Show, don't just tell**: Include examples and code snippets
3. **Keep it current**: Outdated docs are worse than no docs
4. **Write for humans**: Clear, friendly language
5. **Make it findable**: Good structure and search
6. **Progressive disclosure**: Simple → advanced
7. **Docs as code**: Version controlled, reviewed, tested

---

## 📚 Types of Documentation

### 1. README

**Purpose**: First impression and quick start

**Must include**:
- What the project does (one sentence)
- Why it exists (the problem it solves)
- Quick start (get running in <5 minutes)
- Links to deeper docs
- Installation instructions
- Basic usage example
- License and contribution info

**Example structure**:
```markdown
# Project Name

One-sentence description of what this does.

## Why This Exists

Brief paragraph on the problem this solves.

## Quick Start

\`\`\`bash
npm install project-name
npm start
\`\`\`

## Documentation

- [User Guide](docs/user-guide.md)
- [API Reference](docs/api.md)
- [Contributing](CONTRIBUTING.md)

## License

MIT - see [LICENSE](LICENSE)
```

### 2. Getting Started Guide

**Purpose**: Get new users productive quickly

**Structure**:
1. Prerequisites (what you need installed)
2. Installation (step-by-step)
3. First example (working code)
4. Next steps (where to go from here)

**Example**:
```markdown
# Getting Started

## Prerequisites

- Node.js 18+
- PostgreSQL 15+
- 30 minutes

## Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/org/project.git
   cd project
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   npm install
   \`\`\`

3. Configure environment:
   \`\`\`bash
   cp .env.example .env
   # Edit .env with your database credentials
   \`\`\`

4. Run migrations:
   \`\`\`bash
   npm run migrate
   \`\`\`

5. Start the server:
   \`\`\`bash
   npm start
   \`\`\`

## Your First API Call

\`\`\`javascript
const response = await fetch('http://localhost:3000/api/users');
const users = await response.json();
console.log(users);
\`\`\`

## Next Steps

- [User Guide](user-guide.md) - Learn core concepts
- [API Reference](api-reference.md) - Complete API docs
- [Examples](examples/) - More code examples
```

### 3. User Guide / Tutorials

**Purpose**: Teach concepts and workflows

**Best practices**:
- Task-oriented ("How to deploy an app")
- Step-by-step instructions
- Screenshots/diagrams where helpful
- Real-world examples
- Link to reference docs

### 4. API Reference

**Purpose**: Complete technical specification

**What to include**:
- All public APIs, functions, classes
- Parameters and return values
- Type information
- Code examples
- Error cases

**Example**:
```markdown
## createUser(data)

Creates a new user in the database.

**Parameters:**
- `data` (object): User data
  - `email` (string, required): User email
  - `name` (string, required): Full name
  - `role` (string, optional): User role. Default: "user"

**Returns:**
- `Promise<User>`: Created user object

**Throws:**
- `ValidationError`: If email is invalid or already exists
- `DatabaseError`: If database operation fails

**Example:**
\`\`\`javascript
const user = await createUser({
  email: 'alice@example.com',
  name: 'Alice Smith',
  role: 'admin'
});

console.log(user.id);  // "usr_abc123"
\`\`\`
```

### 5. Architecture Documentation

**Purpose**: Explain system design and decisions

**Include**:
- System overview (high-level diagram)
- Component interactions
- Data flow
- Technology choices (and why)
- Trade-offs made

**Use ADRs** (Architecture Decision Records) for important decisions.

### 6. Operations / Runbooks

**Purpose**: Guide operators through common tasks

**Examples**:
- How to deploy
- How to rollback
- How to investigate incidents
- How to scale
- Database migrations
- Backup and recovery

### 7. Code Comments

**What to comment**:
- ✅ Why (not what): Explain reasoning, not obvious code
- ✅ Edge cases and gotchas
- ✅ Complex algorithms
- ✅ Business logic

**What NOT to comment**:
- ❌ Obvious code: `i++; // increment i`
- ❌ Outdated comments
- ❌ Commented-out code (delete it!)

**Good example**:
```javascript
// Hash user IDs for analytics to preserve privacy (GDPR requirement)
// We use SHA-256 with a secret salt to ensure consistent hashing
function anonymizeUserId(userId) {
  return crypto
    .createHash('sha256')
    .update(userId + SECRET_SALT)
    .digest('hex');
}
```

**Bad example**:
```javascript
// This function adds two numbers
function add(a, b) {
  return a + b;  // return the sum
}
```

---

## 🛠️ Documentation Tools

### Static Site Generators

| Tool | Best For | Language |
|------|----------|----------|
| **Docusaurus** | React projects | React/MDX |
| **MkDocs** | Python projects | Markdown |
| **Sphinx** | Python API docs | reStructuredText |
| **VitePress** | Vue projects | Markdown |
| **GitBook** | General docs | Markdown |
| **Nextra** | Next.js projects | MDX |

### API Documentation

| Tool | Best For | Features |
|------|----------|----------|
| **OpenAPI/Swagger** | REST APIs | Interactive playground |
| **GraphQL Playground** | GraphQL | Schema explorer |
| **JSDoc** | JavaScript | Generated from comments |
| **TypeDoc** | TypeScript | Type-aware docs |
| **Redoc** | REST APIs | Beautiful OpenAPI renderer |

### Diagrams

| Tool | Type | Use Case |
|------|------|----------|
| **Mermaid** | Text-based | Sequence, flowcharts, class diagrams |
| **PlantUML** | Text-based | UML diagrams |
| **Excalidraw** | Hand-drawn style | Architecture diagrams |
| **draw.io** | Visual editor | Flowcharts, network diagrams |
| **D2** | Text-based | Modern architecture diagrams |

**Mermaid example**:
```markdown
\`\`\`mermaid
sequenceDiagram
    User->>API: POST /auth/login
    API->>Database: Check credentials
    Database-->>API: User found
    API-->>User: JWT token
\`\`\`
```

---

## ✍️ Writing Great Documentation

### Structure

**Use headings** (H1, H2, H3) for hierarchy:
```markdown
# Main Topic (H1)

## Major Section (H2)

### Subsection (H3)
```

**Use lists** for steps or items:
```markdown
1. First step
2. Second step
3. Third step

- Bullet point
- Another point
```

**Use code blocks** with language tags:
````markdown
```javascript
console.log('Hello, world!');
```
````

**Use callouts** for important info:
```markdown
> ⚠️ **Warning**: This will delete all data!

> 💡 **Tip**: You can use shortcuts to speed this up.
```

### Voice and Tone

**Do**:
- ✅ Use active voice: "Run the command" (not "The command should be run")
- ✅ Use "you": "You can configure..." (not "One can configure...")
- ✅ Be concise: Short sentences and paragraphs
- ✅ Be helpful: Anticipate questions

**Don't**:
- ❌ Use jargon without explanation
- ❌ Assume knowledge
- ❌ Be condescending
- ❌ Use humor that doesn't translate (cultural sensitivity)

### Examples

**Always include working examples**:

```markdown
## Bad (no example)
The `createUser` function creates a user.

## Good (with example)
The `createUser` function creates a user in the database:

\`\`\`javascript
const user = await createUser({
  email: 'alice@example.com',
  name: 'Alice Smith'
});
\`\`\`
```

---

## 🔄 Maintaining Documentation

### Keeping Docs Current

**Strategies**:
- Update docs in the same PR as code changes
- Automated checks for broken links
- Regular documentation reviews (quarterly)
- Tag docs with version numbers
- Archive old versions

**GitHub Actions example**:
```yaml
# .github/workflows/docs.yml
name: Documentation

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      # Check for broken links
      - name: Link Checker
        uses: lycheeverse/lychee-action@v1

      # Build docs to catch errors
      - name: Build docs
        run: |
          cd docs
          npm install
          npm run build
```

### Documentation Debt

**Signs of documentation debt**:
- Outdated screenshots
- Dead links
- References to deprecated features
- No recent updates
- User confusion in support channels

**How to address**:
- Quarterly documentation sprints
- "Adopt-a-doc" program
- Documentation as part of definition of done
- Reward doc contributions

---

## 📊 Documentation Metrics

### Quality Metrics

**Measure**:
- **Freshness**: When was it last updated?
- **Completeness**: Are all features documented?
- **Accuracy**: Does it match current behavior?
- **Findability**: Can users find what they need?
- **User satisfaction**: Doc feedback surveys

**Track**:
- Documentation coverage (% of code with docs)
- Time to first contribution (with vs without docs)
- Support ticket volume (should decrease with better docs)
- Doc page views (what's popular?)
- Search queries (what are people looking for?)

### Documentation Reviews

**Checklist**:
- [ ] Technically accurate
- [ ] Examples work (copy-paste and run them!)
- [ ] No broken links
- [ ] Clear and concise
- [ ] Follows style guide
- [ ] Appropriate detail level
- [ ] Cross-referenced to related docs

---

## 🎨 Documentation Templates

### Feature Documentation Template

```markdown
# Feature Name

## Overview

One paragraph explaining what this feature does and why it exists.

## When to Use

Describe the use cases where this feature is appropriate.

## Prerequisites

- Requirement 1
- Requirement 2

## Usage

### Basic Example

\`\`\`language
// Minimal working example
\`\`\`

### Advanced Example

\`\`\`language
// More complex real-world example
\`\`\`

## Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `option1` | string | "default" | What it does |

## Limitations

- Known limitation 1
- Known limitation 2

## Related

- [Related Feature A](link)
- [Related Feature B](link)
```

### Troubleshooting Template

```markdown
# Troubleshooting Guide

## Problem: [Symptom]

**Symptoms**:
- What the user sees/experiences

**Cause**:
- Why this happens

**Solution**:
1. Step to fix
2. Another step
3. Verification step

**Prevention**:
- How to avoid this in the future
```

See [STYLE_GUIDE.md](STYLE_GUIDE.md), [PLAYBOOKS.md](PLAYBOOKS.md), [TEMPLATES.md](TEMPLATES.md) for complete documentation standards.

---

*This documentation practices guide is maintained with care and consciousness by the Luminous Dynamics community.*
