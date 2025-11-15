# 🤖 Onboarding Automation

> "Good automation scales kindness. Bad automation scales bureaucracy. Let us automate the tedious while preserving the human."

This document provides guidance for automating contributor onboarding and project setup while maintaining consciousness-first values.

---

## 🎯 Automation Philosophy

### What to Automate (and What Not To)

**✅ Automate:**
- Repetitive tasks
- Consistency checks
- Information delivery
- Environment setup
- Routine responses
- Status updates

**❌ Don't Automate:**
- Empathy and emotional support
- Complex decision-making
- Nuanced feedback
- Relationship building
- Values judgment
- Creative problem-solving

### Core Principles

1. **Reduce Friction, Not Humanity**
   - Automation serves people, not replaces them
   - Makes contributing easier, not impersonal
   - Frees humans for high-value interactions

2. **Transparent Automation**
   - Clear when bot vs. human
   - Explain what automation does
   - Easy to opt-out or override

3. **Fail Gracefully**
   - Automation failures shouldn't block humans
   - Always provide manual alternative
   - Monitor and fix broken automation

4. **Evolve With Feedback**
   - Measure impact (does it help?)
   - Iterate based on user feedback
   - Remove automation that annoys

---

## 🤗 Welcoming Contributors

### GitHub Actions: First Interaction

**Auto-welcome new contributors:**

```yaml
# .github/workflows/greetings.yml
name: Greetings

on:
  issues:
    types: [opened]
  pull_requests:
    types: [opened]

jobs:
  greeting:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write
    
    steps:
      - uses: actions/first-interaction@v1
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          issue-message: |
            👋 Welcome to Luminous Dynamics, @${{ github.actor }}!
            
            Thank you for opening your first issue. We're excited to have you in our
            consciousness-first technology community!
            
            A maintainer will review this soon. In the meantime:
            - Check out our [Getting Started Guide](./GETTING_STARTED.md)
            - Join us on [Discord](https://discord.gg/luminous-dynamics)
            - Review our [Code of Conduct](./CODE_OF_CONDUCT.md)
            
            Looking forward to collaborating with you! 💚
          
          pr-message: |
            🎉 Thank you for your first pull request, @${{ github.actor }}!
            
            We appreciate your contribution! Here's what happens next:
            
            1. **Automated checks** will run (linting, tests, etc.)
            2. **Review** from a maintainer (usually within 2-3 days)
            3. **Iteration** based on feedback
            4. **Merge** when everything looks good!
            
            While you wait:
            - Make sure tests pass
            - Read our [Code Review Guide](./CODE_REVIEW.md)
            - Feel free to ask questions here
            
            Thank you for contributing to consciousness-first technology! 💚
```

### Issue Templates with Auto-Labels

**Automatically label and assign issues:**

```yaml
# .github/ISSUE_TEMPLATE/bug_report.yml
name: Bug Report
description: Report a bug
labels: ["bug", "triage"]
assignees:
  - maintainer-on-call

body:
  - type: markdown
    attributes:
      value: |
        Thank you for reporting a bug! This helps improve the project.
  
  - type: dropdown
    id: project
    attributes:
      label: Which project?
      options:
        - Mycelix Core
        - Terra Atlas
        - Luminous Dynamics Main
    validations:
      required: true
  
  - type: textarea
    id: description
    attributes:
      label: Bug Description
      description: What happened?
    validations:
      required: true
```

**Auto-label based on content:**

```yaml
# .github/workflows/label-issues.yml
name: Label Issues

on:
  issues:
    types: [opened, edited]

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v4
        with:
          configuration-path: .github/labeler.yml

# .github/labeler.yml
documentation:
  - '**/*.md'
  - 'docs/**/*'

performance:
  - '**/performance*'
  - body: '/performance|slow|latency/'

security:
  - body: '/security|vulnerability|exploit/'
```

---

## 🚀 Project Setup Automation

### Development Environment

**Automated Setup Script:**

```bash
#!/bin/bash
# scripts/setup.sh

echo "🚀 Setting up Mycelix development environment..."

# Check prerequisites
command -v node >/dev/null 2>&1 || {
  echo "❌ Node.js not found. Please install Node.js 18+"
  exit 1
}

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Setup pre-commit hooks
echo "🪝 Setting up git hooks..."
npx husky install

# Copy environment template
if [ ! -f .env ]; then
  echo "📋 Creating .env from template..."
  cp .env.example .env
  echo "⚠️  Please edit .env with your configuration"
fi

# Run tests to verify setup
echo "🧪 Running tests..."
npm test

echo "✅ Setup complete! Run 'npm start' to begin."
```

**One-Command Setup:**
```bash
$ curl -fsSL https://setup.mycelix.org | bash
```

### Docker for Consistency

**Dockerfile for development:**

```dockerfile
# Dockerfile.dev
FROM node:18

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source
COPY . .

# Expose dev server
EXPOSE 3000

# Start dev server
CMD ["npm", "run", "dev"]
```

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - .:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
  
  database:
    image: postgres:15
    environment:
      POSTGRES_DB: mycelix
      POSTGRES_PASSWORD: dev_password
    ports:
      - "5432:5432"
```

**One command to rule them all:**
```bash
$ docker-compose up
```

### Cookiecutter Templates

**For New Projects:**

```bash
# Install cookiecutter
pip install cookiecutter

# Create new project from template
cookiecutter gh:Luminous-Dynamics/project-template
```

**Template Structure:**
```
project-template/
├── cookiecutter.json
└── {{cookiecutter.project_name}}/
    ├── README.md
    ├── LICENSE
    ├── .gitignore
    ├── pyproject.toml
    ├── src/
    │   └── {{cookiecutter.project_slug}}/
    │       └── __init__.py
    ├── tests/
    └── docs/
```

**cookiecutter.json:**
```json
{
  "project_name": "My Awesome Project",
  "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_') }}",
  "description": "A consciousness-first project",
  "author_name": "Your Name",
  "author_email": "you@example.com",
  "license": "AGPL-3.0",
  "python_version": "3.11"
}
```

---

## ✅ CI/CD Automation

### Continuous Integration

**Run tests on every PR:**

```yaml
# .github/workflows/ci.yml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: Test
        run: npm test
      
      - name: Build
        run: npm run build
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

### Auto-Format Code

**Pre-commit hooks (Husky):**

```json
// package.json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ],
    "*.{json,md,yml}": [
      "prettier --write"
    ],
    "*.py": [
      "black",
      "ruff --fix"
    ]
  }
}
```

**Or use GitHub Actions:**

```yaml
# .github/workflows/auto-format.yml
name: Auto-format

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          ref: ${{ github.head_ref }}
      
      - name: Run Prettier
        run: |
          npm install prettier
          npx prettier --write "**/*.{js,json,md}"
      
      - name: Commit changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git diff --quiet && git diff --staged --quiet || git commit -m "style: auto-format code"
          git push
```

### Automated Releases

**Semantic Release:**

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    branches: [main]

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: 18
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build
        run: npm run build
      
      - name: Semantic Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: npx semantic-release
```

**Configuration (.releaserc.json):**
```json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    "@semantic-release/npm",
    "@semantic-release/github",
    "@semantic-release/git"
  ]
}
```

---

## 🤖 Chatbots and AI Assistants

### GitHub Copilot for Docs

**Help contributors with AI-powered suggestions:**
- Enable GitHub Copilot in repository
- Train on your documentation
- Suggest completions as contributors type

### Discord Bot

**Simple welcome bot:**

```python
# bot.py
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    await channel.send(
        f"👋 Welcome to Luminous Dynamics, {member.mention}!\n\n"
        f"Get started:\n"
        f"• Read our Getting Started guide\n"
        f"• Introduce yourself in #introductions\n"
        f"• Ask questions in #help\n\n"
        f"We're glad you're here! 💚"
    )

@bot.command()
async def docs(ctx, query):
    """Search documentation"""
    results = search_docs(query)
    await ctx.send(f"📚 Found {len(results)} results for '{query}':\n" + 
                   "\n".join(results))

bot.run(DISCORD_TOKEN)
```

### Conscious Use of AI

**Principles:**
- **Transparency**: Label AI-generated content
- **Augmentation**: AI assists humans, doesn't replace
- **Control**: Users can opt-out
- **Privacy**: Don't train on private data
- **Fallback**: Always provide human alternative

---

## 📊 Measuring Success

### Metrics to Track

**Onboarding Effectiveness:**
- Time from first interaction to first PR
- Percentage of newcomers who make second contribution
- Questions asked before first contribution
- Setup time (how long to get dev environment running)

**Automation Health:**
- CI/CD success rate
- Average time from PR to merge
- Bot response time
- Automation error rate

**Community Health:**
- New contributor retention (% still active after 3 months)
- Response time to first-time contributors
- Positive feedback on onboarding experience

### Feedback Loops

**Survey new contributors:**
```markdown
## New Contributor Survey

Help us improve onboarding!

**How easy was it to set up your development environment?**
1 (very hard) - 5 (very easy)

**What was most confusing?**
[Free text]

**What automation was most helpful?**
[Free text]

**What would you improve?**
[Free text]
```

---

## ⚠️ Automation Anti-Patterns

### What NOT to Do

**❌ Over-Automation:**
```
Bot: "Thank you for your contribution!"
Bot: "Tests are running..."
Bot: "Linter passed!"
Bot: "Code coverage looks good!"
Bot: "Build succeeded!"
Bot: "Ready for review!"
Bot: "Reviewer assigned!"
[Contributor is overwhelmed by notifications]
```

**✅ Thoughtful Automation:**
```
Bot: "Thanks for your PR! Tests are running. I'll notify you when ready for review."
[Later] Bot: "✅ All checks passed! @reviewer has been notified."
```

---

**❌ Annoying Automation:**
```
Bot: "This issue will close in 7 days"
Bot: "This issue will close in 5 days"
Bot: "This issue will close in 3 days"
Bot: "This issue will close in 1 day"
Bot: [Closes issue user was actively discussing]
```

**✅ Respectful Automation:**
```
Bot: "This issue has been inactive for 60 days. If still relevant, please comment. 
     Otherwise, it will close in 14 days to keep our backlog manageable."
[If commented] Bot: "Thanks! Keeping open."
```

---

**❌ Impersonal Automation:**
```
Bot: "PR not following template. Rejected."
```

**✅ Helpful Automation:**
```
Bot: "Thanks for your PR! I noticed it doesn't include a description.
     Could you add one? This helps reviewers understand your changes.
     See our PR template: [link]"
```

---

## 💚 Scaling Kindness

### Automation Serves Human Values

**Automation should:**
- Make contributing more welcoming
- Reduce busywork for maintainers
- Speed up routine processes
- Free humans for creative work
- Maintain consistency and quality

**Automation should NOT:**
- Make people feel like numbers
- Replace genuine human interaction
- Enforce rigidity over common sense
- Punish honest mistakes
- Create more bureaucracy

### Human Touch Points

**Keep These Human:**
- First PR review (welcome personally)
- Difficult feedback (empathy required)
- Strategic decisions (judgment calls)
- Conflict resolution (nuance needed)
- Celebrating milestones (genuine appreciation)

---

## 📚 Related Resources

- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - Contribution process
- **[CONTRIBUTOR_LADDER.md](./CONTRIBUTOR_LADDER.md)** - Growth pathways
- **[TESTING.md](./TESTING.md)** - Automated testing
- **[CODE_REVIEW.md](./CODE_REVIEW.md)** - Review automation

---

## 💬 Automation Questions?

- **Setup issues**: #help Discord channel
- **Suggest automation**: GitHub Discussions
- **Report broken automation**: GitHub Issues

---

**Last Updated**: 2025-01-14
**Maintained by**: DevOps & Automation Working Group

---

> "The best automation is invisible. It serves without demanding attention, enables without creating dependency, and scales kindness without losing humanity." 💚
