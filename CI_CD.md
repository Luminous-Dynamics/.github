# 🔄 Continuous Integration & Continuous Deployment (CI/CD)

> "If it hurts, do it more often. If deployment hurts, deploy more often."  
> — Martin Fowler

*Last updated: January 2025*

This document outlines our **CI/CD philosophy and practices**—how we automate the path from code commit to production deployment to ship quality software quickly and safely.

---

## 🎯 CI/CD Philosophy

### What is CI/CD?

**Continuous Integration (CI)**:
- Automatically build and test every code change
- Merge to main branch frequently (daily or more)
- Keep main branch always releasable
- Fast feedback on code quality

**Continuous Delivery (CD)**:
- Code is always in a deployable state
- Deployment is automated but requires manual approval
- Can release on demand

**Continuous Deployment (CD)**:
- Every change that passes tests automatically deploys to production
- No manual gate (except emergencies)
- Fastest path to users

### Our CI/CD Principles

1. **Automate everything**: If humans can forget it, automate it
2. **Fail fast**: Find problems in seconds/minutes, not hours/days
3. **Keep main green**: Main branch must always be deployable
4. **Small batches**: Small, frequent commits over large, infrequent ones
5. **Fast feedback**: CI pipeline <10 minutes
6. **Security built-in**: Security scanning in every pipeline
7. **Deployment as routine**: Deploy daily, not monthly
8. **Rollback always possible**: Every deploy can be undone quickly
9. **Monitor everything**: Know immediately if deploy breaks something
10. **Learn from failures**: Incidents improve the pipeline

---

## 🏗️ CI Pipeline Design

### Pipeline Stages

**Complete CI pipeline** (typical):

```
┌─────────────┐
│ Code Commit │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Checkout  │ ← Clone repository
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Build    │ ← Compile, bundle, package
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Unit Tests │ ← Fast, isolated tests
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Lint     │ ← Code style, static analysis
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Security   │ ← SAST, dependency scanning
│   Scanning  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Integration │ ← Tests with real services
│    Tests    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Build      │ ← Create deployable artifact
│  Artifact   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Deploy    │ ← Deploy to staging/prod
└─────────────┘
```

**Key characteristics**:
- **Fast stages first**: Fail fast on cheap checks
- **Parallel where possible**: Run tests concurrently
- **Cache aggressively**: Reuse dependencies
- **Fail on first error**: Don't waste time after failure

### Stage Breakdown

#### 1. Checkout (5-30 seconds)

```yaml
# GitHub Actions example
- name: Checkout code
  uses: actions/checkout@v4
  with:
    fetch-depth: 0  # Full history for some tools
```

**Optimizations**:
- Shallow clone when possible
- Cache git objects
- Use sparse checkout for monorepos

#### 2. Build (30 seconds - 5 minutes)

```yaml
- name: Setup Node.js
  uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'

- name: Install dependencies
  run: npm ci  # Faster than npm install

- name: Build
  run: npm run build
```

**Optimizations**:
- Cache dependencies between runs
- Incremental builds
- Parallel compilation
- Remove debug info in CI builds

#### 3. Unit Tests (1-3 minutes)

```yaml
- name: Run unit tests
  run: npm test -- --coverage --maxWorkers=50%

- name: Upload coverage
  uses: codecov/codecov-action@v3
```

**Best practices**:
- Run in parallel
- Fail fast (stop on first failure in CI)
- Generate coverage report
- Upload to coverage service

#### 4. Lint & Static Analysis (30 seconds - 2 minutes)

```yaml
- name: Lint
  run: npm run lint

- name: Type check
  run: npm run typecheck

- name: Check formatting
  run: npm run format:check
```

**Tools**:
- **JavaScript/TypeScript**: ESLint, Prettier, TypeScript compiler
- **Python**: flake8, black, mypy, pylint
- **Rust**: clippy, rustfmt
- **Go**: golint, gofmt

#### 5. Security Scanning (1-5 minutes)

```yaml
- name: Dependency audit
  run: npm audit --audit-level=high

- name: SAST scan
  uses: github/codeql-action/analyze@v2

- name: Secret scanning
  uses: trufflesecurity/trufflehog@main
```

**Security checks**:
- **Dependency vulnerabilities**: npm audit, Snyk, Dependabot
- **SAST** (Static Application Security Testing): CodeQL, SonarQube, Semgrep
- **Secret scanning**: TruffleHog, GitGuardian, detect-secrets
- **License compliance**: License scanners

#### 6. Integration Tests (3-10 minutes)

```yaml
- name: Start test dependencies
  run: docker-compose -f docker-compose.test.yml up -d

- name: Wait for services
  run: ./scripts/wait-for-services.sh

- name: Run integration tests
  run: npm run test:integration

- name: Cleanup
  if: always()
  run: docker-compose -f docker-compose.test.yml down
```

**Best practices**:
- Use Docker for service dependencies
- Parallel test execution
- Retry flaky tests (but fix them!)
- Clean up resources after tests

#### 7. Build Artifact (1-3 minutes)

```yaml
- name: Build production artifact
  run: npm run build:prod

- name: Create Docker image
  run: |
    docker build -t myapp:${{ github.sha }} .
    docker tag myapp:${{ github.sha }} myapp:latest

- name: Push to registry
  run: docker push myapp:${{ github.sha }}
```

**Artifacts**:
- Docker images
- Compiled binaries
- JavaScript bundles
- tar.gz archives

**Versioning**:
- Git SHA for traceability
- Semantic version for releases
- Tags: `latest`, `staging`, `v1.2.3`

---

## 🚀 CD Pipeline Design

### Deployment Stages

**Production deployment pipeline**:

```
┌──────────────┐
│  CI Pipeline │
│   Completes  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│Deploy Staging│ ← Automatic
└──────┬───────┘
       │
       ▼
┌──────────────┐
│Run E2E Tests │ ← Smoke tests in staging
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Manual      │ ← Optional gate
│  Approval    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│Deploy Prod   │ ← Blue-green/canary
└──────┬───────┘
       │
       ▼
┌──────────────┐
│Monitor & Verify│ ← Check metrics/errors
└──────┬───────┘
       │
       ▼
    Success!
```

### Deployment Strategies

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment strategies.

**Quick overview**:

**Rolling Deployment**:
- Update instances gradually
- Low risk, zero downtime
- Slow rollback

**Blue-Green**:
- Run two identical environments
- Switch traffic instantly
- Fast rollback
- Higher cost (2x resources during deploy)

**Canary**:
- Deploy to small % of users first
- Monitor for issues
- Gradually increase %
- Safest for high-traffic services

**Feature Flags**:
- Deploy code "dark" (disabled)
- Enable for subset of users
- Decouple deployment from release
- Best combined with other strategies

---

## 🛠️ CI/CD Tools

### GitHub Actions

**Why GitHub Actions**:
- Native GitHub integration
- Free for public repos
- Good free tier for private
- Easy to use
- Strong ecosystem

**Example workflow** (`.github/workflows/ci.yml`):

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: Test
        run: npm test -- --coverage
      
      - name: Build
        run: npm run build

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run CodeQL
        uses: github/codeql-action/analyze@v2
      
      - name: Dependency audit
        run: npm audit --audit-level=moderate

  deploy:
    needs: [test, security]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Deploy to staging
        run: ./scripts/deploy-staging.sh
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

### GitLab CI

**Why GitLab CI**:
- Integrated with GitLab
- Powerful runner system
- Built-in container registry
- Good for self-hosted

**Example** (`.gitlab-ci.yml`):

```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths:
      - dist/
    expire_in: 1 hour

test:
  stage: test
  script:
    - npm ci
    - npm test

deploy_staging:
  stage: deploy
  script:
    - ./deploy-staging.sh
  only:
    - main
  environment:
    name: staging
    url: https://staging.example.com
```

### Other Tools

**Jenkins**:
- Most mature CI/CD tool
- Highly customizable
- Requires self-hosting
- Steeper learning curve

**CircleCI**:
- Cloud-based
- Fast builds
- Good Docker support
- Paid tiers for private repos

**Travis CI**:
- Simple setup
- Good for open source
- Less popular now

**Terraform Cloud / Spacelift**:
- For infrastructure deployments
- Plan/apply workflows
- State management

---

## 📋 CI/CD Best Practices

### Keep Main Branch Green

**Main branch must always**:
- Build successfully
- Pass all tests
- Be deployable to production

**How to achieve**:
- **Protect main branch**: Require PR reviews
- **Status checks**: Require CI passing before merge
- **No direct commits**: All changes via PR
- **Fast feedback**: Know quickly if you broke something
- **Fix forward**: If main breaks, fix immediately (or revert)

**GitHub branch protection example**:
```
Settings → Branches → Branch protection rules

☑ Require pull request reviews before merging
☑ Require status checks to pass before merging
  ☑ CI / test
  ☑ CI / security
☑ Require branches to be up to date before merging
☑ Include administrators
```

### Optimize for Speed

**Why speed matters**:
- Faster feedback = faster fixes
- Developers stay in flow
- More frequent deploys
- Less context switching

**Optimization techniques**:

**1. Parallel execution**:
```yaml
jobs:
  test:
    strategy:
      matrix:
        node: [18, 20, 22]
        os: [ubuntu-latest, windows-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

**2. Caching**:
```yaml
- uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

**3. Fail fast**:
```yaml
- name: Test
  run: npm test -- --bail  # Stop on first failure
```

**4. Selective testing**:
```yaml
# Only run affected tests
- name: Test changed files
  run: npm test -- --onlyChanged
```

**5. Skip unnecessary work**:
```yaml
on:
  push:
    paths:
      - 'src/**'
      - 'tests/**'
      - 'package.json'
  # Don't run CI for docs-only changes
```

### Security in CI/CD

**Never commit secrets**:
```yaml
# ❌ DON'T
API_KEY=sk_live_1234567890

# ✅ DO - Use secrets management
- name: Deploy
  run: ./deploy.sh
  env:
    API_KEY: ${{ secrets.API_KEY }}
```

**Secrets management**:
- GitHub Secrets
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault

**Principle of least privilege**:
- CI tokens with minimal permissions
- Read-only where possible
- Separate tokens for dev/staging/prod

**Security scanning**:
- Every pipeline scans dependencies
- SAST on every commit
- Secret scanning enabled
- Container image scanning

### Testing in CI

**Test pyramid in CI**:

```
      ┌─────┐
     /   E2E  \      ← Few, slow, high value
    ───────────
   /   Integration  \   ← Some, medium speed
  ───────────────────
 /      Unit Tests     \ ← Many, fast, focused
───────────────────────
```

**CI testing strategy**:
- **Every commit**: Unit tests, linting
- **Every PR**: Integration tests
- **Before deploy**: E2E smoke tests
- **After deploy**: Production smoke tests

**Flaky test policy**:
- Track flaky tests
- Fix or remove
- Don't ignore failures
- Retry is a band-aid, not a solution

### Deployment Automation

**Deployment should be**:
- **One command**: `./deploy.sh production`
- **Idempotent**: Safe to run multiple times
- **Verified**: Health checks after deploy
- **Rollback-able**: Can undo in <5 minutes
- **Audited**: Who deployed what when

**Pre-deployment checklist**:
```yaml
- name: Pre-deploy checks
  run: |
    # Check if already deployed
    if ./scripts/check-version.sh ${{ github.sha }}; then
      echo "Already deployed, skipping"
      exit 0
    fi
    
    # Database migrations
    ./scripts/migrate.sh
    
    # Health check current version
    ./scripts/health-check.sh
```

**Post-deployment verification**:
```yaml
- name: Post-deploy verification
  run: |
    # Wait for rollout
    kubectl rollout status deployment/myapp
    
    # Smoke tests
    ./scripts/smoke-test.sh
    
    # Check error rates
    ./scripts/check-error-rates.sh
```

---

## 📊 CI/CD Metrics

### Key Metrics

**Deployment Frequency**:
- How often do we deploy to production?
- Target: Daily or more (for web apps)
- Elite: Multiple times per day

**Lead Time for Changes**:
- Code commit → running in production
- Target: <1 hour for small changes
- Elite: <15 minutes

**Mean Time to Recovery (MTTR)**:
- Production incident → fix deployed
- Target: <1 hour
- Elite: <15 minutes

**Change Failure Rate**:
- % of deployments causing production incident
- Target: <15%
- Elite: 0-5%

**CI Pipeline Duration**:
- Commit → pipeline complete
- Target: <10 minutes
- Elite: <5 minutes

**Build Success Rate**:
- % of builds that pass
- Target: >90%
- Elite: >95%

### Dashboard

**Example CI/CD dashboard** (Grafana):
```
┌─────────────────────────────────────────┐
│ Deployments Last 7 Days: 42             │
│ Success Rate: 97%                       │
│ Avg Deploy Duration: 8m 23s             │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ CI Pipeline Metrics                     │
│ ├─ Avg Duration: 6m 45s                 │
│ ├─ Success Rate: 94%                    │
│ └─ Failures (last 24h): 3               │
└─────────────────────────────────────────┘

[Chart: Deployment frequency over time]
[Chart: Lead time for changes]
[Chart: Failed deployments]
```

---

## 🚨 Common CI/CD Anti-Patterns

### What NOT to Do

**❌ Testing in production**:
"We'll just deploy and see what happens" → Always test before production

**❌ Long-lived feature branches**:
Weeks-old branches → Merge conflicts, integration hell, delayed feedback

**❌ Manual deployments**:
SSH into server and copy files → Error-prone, not auditable, not repeatable

**❌ Skipping tests to "save time"**:
"Tests take too long, let's skip them" → Find bugs in production instead

**❌ No rollback plan**:
"It'll probably work" → When it doesn't, you're stuck

**❌ Ignoring failed builds**:
"It's just a flaky test" → Erodes trust in CI

**❌ Deploying without health checks**:
Deploy and pray → Don't know if deployment succeeded

**❌ No deployment windows**:
Deploy at 3pm Friday → Spend weekend debugging

**❌ Cowboy deployments**:
Deploying without telling anyone → Surprises team, users

**❌ One-size-fits-all pipeline**:
Same pipeline for all projects → Slow for small, inadequate for large

---

## 🎯 CI/CD Maturity Model

### Level 0: Manual

- No automation
- Manual testing
- Manual deployment
- Rare releases

**Action**: Automate build and basic tests

### Level 1: Continuous Build

- Automated build on commit
- Some automated tests
- Manual deployment
- Monthly releases

**Action**: Automate all tests, protect main branch

### Level 2: Continuous Integration

- All commits trigger CI
- Comprehensive automated tests
- Main branch always green
- Manual deployment
- Weekly releases

**Action**: Automate deployment to staging

### Level 3: Continuous Delivery

- Automated deployment to staging
- Manual deployment to prod
- Daily releases possible
- Feature flags in use

**Action**: Automate production deployment

### Level 4: Continuous Deployment

- Automated deployment to prod
- Every passing commit can deploy
- Multiple deploys per day
- Fast rollback

**Action**: Optimize for speed and reliability

### Level 5: Elite Performance

- <15 min commit to production
- <15 min MTTR
- <5% change failure rate
- Multiple deploys per day
- Sophisticated monitoring and rollback

---

## 💚 Conscious CI/CD

**CI/CD is about enabling humans to deliver value safely and joyfully.**

**Consciousness-first CI/CD**:
- **Respect developer time**: Fast feedback, don't waste time on slow builds
- **Respect user trust**: Thorough testing before production
- **Respect operations**: Deployments are routine, not heroic
- **Respect learning**: Failed builds teach us
- **Respect sustainability**: Automate toil, preserve energy for creativity

**Great CI/CD enables**:
- Developers to ship confidently
- Users to get value quickly
- Teams to iterate rapidly
- Organizations to experiment safely

**When deployment is routine, innovation flourishes.** 💚✨

---

## 📚 Related Resources

- [DEPLOYMENT.md](DEPLOYMENT.md) - Deployment strategies
- [ENVIRONMENTS.md](ENVIRONMENTS.md) - Environment management
- [INFRASTRUCTURE.md](INFRASTRUCTURE.md) - Infrastructure as Code
- [TESTING.md](TESTING.md) - Testing practices
- [OBSERVABILITY.md](OBSERVABILITY.md) - Monitoring deployments
- [SECURITY.md](SECURITY.md) - Security in CI/CD

---

*This CI/CD guide is maintained with care and consciousness by the Luminous Dynamics community.*
