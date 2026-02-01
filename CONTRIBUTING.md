# Contributing to Luminous Dynamics

Thank you for your interest in contributing to Luminous Dynamics! We're building technology that serves human flourishing, and we welcome contributors who share our commitment to creating accessible, high-quality open-source software.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Communication Channels](#communication-channels)
- [Core Projects](#core-projects)

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## Getting Started

### Repository Structure

Most development happens in the **monorepo** at [luminous-dynamics/luminous-dynamics](https://github.com/Luminous-Dynamics/luminous-dynamics). This contains the core codebase and shared infrastructure.

Individual projects may have their own repositories for standalone releases:

- **[Terra Atlas](https://github.com/Luminous-Dynamics/terra-atlas)** - Energy investment platform
- **[Luminous Nix](https://github.com/Luminous-Dynamics/luminous-nix)** - NixOS natural language interface
- **[Mycelix-Core](https://github.com/Luminous-Dynamics/Mycelix-Core)** - Decentralized ML protocol

## Development Setup

### Prerequisites

- **Git** - Version control
- **Nix** (recommended) - For reproducible development environments
- **Node.js 20+** - For JavaScript/TypeScript projects
- **Python 3.11+** - For Python projects
- **Rust** (latest stable) - For Mycelix-Core

### Quick Start with Nix (Recommended)

We use Nix flakes for reproducible development environments:

```bash
# Clone the monorepo
git clone https://github.com/Luminous-Dynamics/luminous-dynamics.git
cd luminous-dynamics

# Enter the development environment
nix develop

# For specific projects
cd terra-lumina/terra-atlas-app && nix develop
cd 11-meta-consciousness/luminous-nix && nix develop
cd Mycelix-Core && nix develop
```

### Traditional Setup

Each project includes its own setup instructions in its README. Generally:

```bash
# For Node.js projects
npm install

# For Python projects
poetry install

# For Rust projects
cargo build
```

## How to Contribute

### Types of Contributions

1. **Code** - Bug fixes, features, performance improvements
2. **Documentation** - Improve guides, fix typos, add examples
3. **Testing** - Write tests, improve coverage, report edge cases
4. **Design** - UI/UX improvements, accessibility enhancements
5. **Translation** - Help make our projects accessible globally

### Contribution Workflow

1. **Fork** the repository
2. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```
3. **Make your changes** following our code standards
4. **Write tests** for new functionality
5. **Commit** with clear, descriptive messages
6. **Push** to your fork
7. **Open a Pull Request**

### Commit Message Guidelines

We follow conventional commits:

```
type(scope): brief description

Longer description if needed.

Closes #123
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(terra-atlas): add 3D globe visualization`
- `fix(luminous-nix): resolve voice interface timeout`
- `docs(mycelix): update installation guide`

## Pull Request Process

1. **Ensure your PR**:
   - Has a clear title and description
   - References any related issues
   - Includes tests for new functionality
   - Passes all CI checks
   - Has no merge conflicts

2. **PR Template**: Fill out the PR template completely, including:
   - Summary of changes
   - Type of change (feature, bugfix, etc.)
   - How to test
   - Screenshots/demos if applicable

3. **Review Process**:
   - At least one maintainer review required
   - Address all feedback constructively
   - Keep discussions focused and respectful

4. **After Merge**:
   - Delete your feature branch
   - Update any related issues

## Issue Reporting

### Before Creating an Issue

1. Search existing issues to avoid duplicates
2. Check if there's a workaround in the documentation
3. Ensure you're using the latest version

### Bug Reports

Include:
- Clear title describing the problem
- Steps to reproduce
- Expected vs. actual behavior
- Environment details (OS, versions, etc.)
- Relevant logs or error messages
- Screenshots if applicable

### Feature Requests

Include:
- Clear description of the desired feature
- Use case and motivation
- Potential implementation approach (if you have ideas)
- Whether you're willing to work on it

## Communication Channels

- **GitHub Issues** - Bug reports, feature requests, technical discussions
- **GitHub Discussions** - General questions, ideas, community chat
- **Email** - tristan.stoltz@evolvingresonantcocreationism.com

## Core Projects

### Terra Atlas

Energy investment platform democratizing access to renewable energy projects.

**Tech Stack**: Next.js, TypeScript, Supabase, Three.js
**Location in monorepo**: `terra-lumina/terra-atlas-app/`

### Luminous Nix

Natural language interface for NixOS, making system management accessible to everyone.

**Tech Stack**: Python, PyTorch, FastAPI
**Location in monorepo**: `11-meta-consciousness/luminous-nix/`

### Mycelix-Core

Decentralized ML protocol for distributed neural network training without central coordination.

**Tech Stack**: Rust, Holochain
**Location in monorepo**: `Mycelix-Core/`

## Development Principles

### Engineering Excellence

- **Test before claiming** - Verify performance improvements with benchmarks
- **Honest metrics** - Use real measurements, not estimates
- **Clean architecture** - Write maintainable, well-documented code
- **Accessibility first** - Design for all users from the start

### Code Standards

- Follow existing code style in each project
- Write meaningful comments for complex logic
- Include type annotations where applicable
- Keep functions focused and testable

### Testing

- Write unit tests for new functionality
- Include integration tests for critical paths
- Aim for meaningful coverage, not just numbers
- Test edge cases and error conditions

## Recognition

Contributors are recognized in:
- Release notes
- Project README files
- Annual contributor highlights

## Questions?

If you have questions about contributing, please:
1. Check existing documentation
2. Open a GitHub Discussion
3. Email tristan.stoltz@evolvingresonantcocreationism.com

Thank you for helping build technology that serves humanity!

---

*"In unity we code, in love we debug, in consciousness we deploy"*
