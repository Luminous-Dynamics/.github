# 🌍 Environment Management

> "Production is not the place to discover environment differences."

*Last updated: January 2025*

This document outlines **environment management**—how we maintain development, staging, and production environments with proper configuration management, secrets handling, and environment parity to ensure reliability and security across the software delivery lifecycle.

## 📋 Environment Quick Reference

### Environment Comparison

| Aspect | Development | Staging | Production |
|--------|------------|---------|------------|
| **Purpose** | Individual coding & testing | Pre-release validation | Serve real users |
| **Scale** | Single instance, local | 2-3 instances, minimal | Auto-scaling, multi-AZ |
| **Data** | Synthetic/mock data | Sanitized prod data | Real customer data |
| **Security** | Relaxed for debugging | Production-like | Strictest security |
| **Secrets** | Test/dummy keys | Real but non-prod | Production secrets only |
| **Monitoring** | Basic/optional | Full monitoring | Full + alerts + on-call |
| **Deployment** | Manual, frequent (100x/day) | Auto on main merge | Manual approval required |
| **Costs** | Minimal (~$10/mo) | Low (~$100/mo) | High (~$1000s/mo) |
| **Availability** | Can go down anytime | Best effort 99%+ | SLA 99.9%+ |

### Secrets Management Quick Lookup

| Secret Type | Tool | Storage | Rotation | Access |
|-------------|------|---------|----------|--------|
| **Database Passwords** | AWS Secrets Manager | Encrypted | Auto 30-90 days | IAM roles |
| **API Keys** | Secrets Manager / Vault | Encrypted | Manual or auto | Environment vars |
| **TLS Certificates** | AWS ACM / Let's Encrypt | Encrypted | Auto renewal | Load balancer |
| **SSH Keys** | AWS Systems Manager | Encrypted | Manual | Bastion host only |
| **Encryption Keys** | AWS KMS | HSM-backed | Manual | Application IAM role |

### Configuration Hierarchy

```
Priority (highest to lowest):
1. Runtime Flags (feature flags) - Change without deploy
2. Environment Variables - Per-environment config
3. Secret Manager - Sensitive credentials
4. Config Files (config/production.js) - Environment defaults
5. Code Defaults (config/default.js) - Fallback values
```

### Environment Promotion Rules

| Gate | Requirement | Who Approves | Time Window |
|------|-------------|--------------|-------------|
| **Dev → Staging** | All tests pass, code review | Automatic | Any time |
| **Staging → Prod** | QA sign-off, E2E tests pass | Platform team | Mon-Thu 10am-2pm |
| **Hotfix → Prod** | Critical bug, manager approval | CTO/VP Eng | Emergency only |

### Common Environment Variables

```bash
# Application
NODE_ENV=production           # Environment name
PORT=8080                     # Server port
LOG_LEVEL=info               # Logging verbosity

# Database
DATABASE_URL=postgres://...  # Connection string
DB_POOL_MIN=10               # Connection pool min
DB_POOL_MAX=50               # Connection pool max

# External Services
STRIPE_API_KEY=sk_live_...   # Payment provider
SENDGRID_API_KEY=SG.abc...   # Email service
REDIS_URL=redis://...        # Cache/sessions

# Observability
SENTRY_DSN=https://...       # Error tracking
DATADOG_API_KEY=abc123...    # Metrics/traces
```

---

## 🎯 Environment Philosophy

### Why Multiple Environments Matter

**Without proper environments**:
- ❌ "Works on my machine" syndrome
- ❌ Bugs discovered in production
- ❌ No safe testing ground
- ❌ Secrets leaked in code
- ❌ Configuration drift
- ❌ Risky deployments

**With proper environments**:
- ✅ Test changes safely before production
- ✅ Catch bugs early
- ✅ Secure secrets management
- ✅ Consistent configuration
- ✅ Confident deployments
- ✅ Faster feedback loops

### Environment Principles

1. **Parity**: Environments should be as similar as possible
2. **Isolation**: Changes in dev don't affect production
3. **Progression**: Code flows dev → staging → production
4. **Configuration as code**: Environment config versioned in Git
5. **Secrets never in code**: Use secure secret management
6. **Automate everything**: Manual setup leads to drift
7. **Production-like data**: Use realistic (but safe) test data

---

## 🏗️ Environment Types

### Development Environment

**Purpose**: Individual developer experimentation and iteration

**Characteristics**:
- Runs locally on developer machine or cloud dev environment
- Fast feedback loop (seconds to minutes)
- Easy to reset/rebuild
- Uses local or shared dev databases
- Relaxed security for debugging
- May use mocked external services

**Tools**:
- Docker Compose for local services
- `.env.local` for configuration
- Hot reload for rapid iteration
- Local databases (SQLite, PostgreSQL in Docker)

**Example Docker Compose**:
```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  app:
    build: .
    volumes:
      - .:/app
      - /app/node_modules
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgres://postgres:dev@db:5432/myapp_dev
      - LOG_LEVEL=debug
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=dev
      - POSTGRES_DB=myapp_dev
    volumes:
      - dev-db-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  dev-db-data:
```

### Staging Environment

**Purpose**: Production-like testing before release

**Characteristics**:
- Mirrors production infrastructure
- Uses production-like data (sanitized)
- Full integration testing
- Performance testing
- Security testing
- User acceptance testing (UAT)

**Key difference from production**:
- Smaller scale (fewer servers, smaller databases)
- Synthetic traffic, not real users
- Can be reset/rebuilt
- May use test payment processors

**Infrastructure**:
```hcl
# terraform/staging/main.tf
module "app" {
  source = "../modules/app"

  environment = "staging"

  # Smaller than production
  instance_count = 2  # vs 10 in prod
  instance_type  = "t3.medium"  # vs c5.xlarge in prod

  database_instance_class = "db.t3.medium"  # vs db.r5.xlarge in prod

  # Same structure, different scale
  enable_monitoring = true
  enable_autoscaling = true

  # Use staging secrets
  secrets_prefix = "staging/"
}
```

### Production Environment

**Purpose**: Serve real users with reliability and performance

**Characteristics**:
- High availability (multiple zones/regions)
- Autoscaling
- Full monitoring and alerting
- Strict security
- Real customer data
- Backup and disaster recovery
- Performance optimized

**Non-negotiables**:
- ✅ Never deploy untested code
- ✅ All secrets in secret manager
- ✅ Encryption at rest and in transit
- ✅ Audit logging enabled
- ✅ Automated backups
- ✅ Disaster recovery plan
- ✅ Rate limiting and DDoS protection

---

## 🔐 Secrets Management

### What Are Secrets?

**Secrets** are sensitive credentials that must never be committed to code:
- API keys and tokens
- Database passwords
- Encryption keys
- OAuth client secrets
- TLS certificates
- SSH private keys

### ❌ Never Do This

```javascript
// WRONG: Hardcoded secrets
const API_KEY = "sk_live_abc123xyz789";
const db = connect("postgres://admin:password123@db.prod.com/app");

// WRONG: Committed .env file
// .env (committed to Git)
DATABASE_PASSWORD=super_secret_password
STRIPE_SECRET_KEY=sk_live_real_key
```

### ✅ Always Do This

```javascript
// RIGHT: Use environment variables
const API_KEY = process.env.STRIPE_API_KEY;
const db = connect(process.env.DATABASE_URL);

// RIGHT: .env in .gitignore
// .env.example (committed as template)
DATABASE_URL=postgres://user:password@localhost:5432/myapp
STRIPE_API_KEY=sk_test_your_key_here
LOG_LEVEL=info
```

### Secrets Management Tools

| Tool | Best For | Pros | Cons |
|------|----------|------|------|
| **AWS Secrets Manager** | AWS-native | Automatic rotation, audit logs | AWS-only, cost |
| **HashiCorp Vault** | Multi-cloud | Powerful, flexible | Complex setup |
| **Azure Key Vault** | Azure-native | Azure integration | Azure-only |
| **Google Secret Manager** | GCP-native | Simple, GCP integration | GCP-only |
| **Doppler** | Any platform | Great DX, cross-platform | SaaS dependency |
| **1Password/Bitwarden** | Small teams | Familiar interface | Manual processes |

### AWS Secrets Manager Example

```bash
# Store secret
aws secretsmanager create-secret \
  --name production/database/password \
  --secret-string "super_secure_password"

# Retrieve in application
aws secretsmanager get-secret-value \
  --secret-id production/database/password \
  --query SecretString --output text
```

```javascript
// Node.js example
const AWS = require('aws-sdk');
const secretsManager = new AWS.SecretsManager();

async function getSecret(secretName) {
  const response = await secretsManager.getSecretValue({
    SecretId: secretName
  }).promise();

  return response.SecretString;
}

// Use in app
const dbPassword = await getSecret('production/database/password');
```

### Environment Variables Best Practices

```bash
# .env.example - Committed to Git (no real values)
NODE_ENV=development
PORT=3000
DATABASE_URL=postgres://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379
API_KEY=your_api_key_here
LOG_LEVEL=info

# .env - NOT committed (.gitignore'd)
NODE_ENV=production
PORT=3000
DATABASE_URL=postgres://produser:real_password@db.prod.com:5432/proddb
REDIS_URL=redis://cache.prod.com:6379
API_KEY=sk_live_real_key_abc123
LOG_LEVEL=warn
```

---

## ⚙️ Configuration Management

### Configuration Hierarchy

```
1. Defaults (in code)
2. Environment-specific config files
3. Environment variables
4. Secrets from secret manager
5. Runtime flags (feature flags)
```

### Example Configuration System

```javascript
// config/default.js - Base configuration
module.exports = {
  server: {
    port: 3000,
    timeout: 30000
  },
  database: {
    pool: { min: 2, max: 10 }
  },
  features: {
    newCheckout: false
  }
};

// config/production.js - Production overrides
module.exports = {
  server: {
    port: process.env.PORT || 8080,
    timeout: 60000
  },
  database: {
    url: process.env.DATABASE_URL,
    pool: { min: 10, max: 50 },
    ssl: true
  },
  features: {
    newCheckout: true
  }
};

// config/index.js - Loader
const env = process.env.NODE_ENV || 'development';
const defaultConfig = require('./default');
const envConfig = require(`./${env}`);

module.exports = { ...defaultConfig, ...envConfig };
```

---

## 🔄 Environment Promotion Workflow

### Code Promotion Path

Complete flow from developer laptop to production with all gates and validations:

```mermaid
flowchart TB
    subgraph LocalDev["💻 Local Development"]
        DevCode[Developer Writes Code<br/>Feature branch]
        LocalTest[Local Testing<br/>Unit tests, lint<br/>Docker Compose]
        Commit[Git Commit<br/>Pre-commit hooks]
    end

    subgraph CI["🔍 Continuous Integration"]
        PRCreate[Create Pull Request<br/>Feature → main]
        CIRun[CI Pipeline<br/>Tests, lint, build<br/>Security scan]
        CodeReview[Code Review<br/>Team approval required]
    end

    subgraph DevEnv["🔧 Dev Environment"]
        DevDeploy[Auto-Deploy to Dev<br/>On PR creation]
        DevTest[Development Testing<br/>Integration tests<br/>Manual verification]
        DevGate{CI Checks<br/>Pass?}
    end

    subgraph StagingEnv["🎭 Staging Environment"]
        Merge[Merge to Main<br/>Automatic]
        StagingDeploy[Auto-Deploy to Staging<br/>Blue-green deployment]
        E2ETests[E2E Testing<br/>Full user flows<br/>15-30 minutes]
        LoadTest[Load Testing<br/>Performance validation]
        QATest[QA/UAT Testing<br/>Manual validation<br/>Business sign-off]
        StagingGate{All Tests<br/>Pass?}
    end

    subgraph ProdApproval["✅ Production Approval"]
        CreateRelease[Create Release<br/>Tag: v1.2.3]
        ManualApproval[Manual Approval<br/>Platform team<br/>Deploy window check]
        ChangeTicket{Change Mgmt<br/>Ticket?}
    end

    subgraph ProdEnv["🚀 Production Environment"]
        ProdDeploy[Deploy to Production<br/>Canary → 100%<br/>2-hour rollout]
        HealthCheck[Health Checks<br/>Smoke tests<br/>Monitor metrics]
        ProdVerify[Production Verification<br/>Critical flows<br/>Error rates<br/>Latency]
        ProdGate{Deploy<br/>Healthy?}
    end

    subgraph Rollback["⚠️ Rollback & Incident"]
        AutoRollback[Automatic Rollback<br/>Error rate > 2x<br/>Critical failure]
        ManualRollback[Manual Rollback<br/>Team decision<br/><5 minutes]
        Incident[Create Incident<br/>Post-mortem]
    end

    subgraph Success["🎉 Release Complete"]
        ReleaseNotes[Release Notes<br/>Changelog update]
        Notify[Notify Team<br/>Slack, email]
        Complete([Release v1.2.3<br/>in Production])
    end

    DevCode --> LocalTest
    LocalTest --> Commit
    Commit --> PRCreate

    PRCreate --> CIRun
    PRCreate --> DevDeploy

    CIRun --> CodeReview
    DevDeploy --> DevTest
    DevTest --> DevGate

    DevGate -->|Pass ✅| CodeReview
    DevGate -->|Fail ❌| FixBugs1[Fix Issues<br/>Push to PR]

    CodeReview --> Merge
    Merge --> StagingDeploy

    StagingDeploy --> E2ETests
    E2ETests --> LoadTest
    LoadTest --> QATest
    QATest --> StagingGate

    StagingGate -->|Pass ✅| CreateRelease
    StagingGate -->|Fail ❌| FixBugs2[Fix Issues<br/>New PR]

    CreateRelease --> ManualApproval
    ManualApproval --> ChangeTicket

    ChangeTicket -->|Approved ✅| ProdDeploy
    ChangeTicket -->|Rejected ❌| Hold[Hold Release<br/>Reschedule]

    ProdDeploy --> HealthCheck
    HealthCheck --> ProdVerify
    ProdVerify --> ProdGate

    ProdGate -->|Healthy ✅| ReleaseNotes
    ProdGate -->|Auto-trigger ⛔| AutoRollback
    ProdGate -->|Manual decision 🚨| ManualRollback

    AutoRollback --> Incident
    ManualRollback --> Incident

    ReleaseNotes --> Notify
    Notify --> Complete

    style DevCode fill:#e1bee7
    style StagingDeploy fill:#fff9c4
    style ProdDeploy fill:#ffccbc
    style ManualApproval fill:#ffe5b4
    style Complete fill:#a5d6a7
    style AutoRollback fill:#ffcdd2
    style ManualRollback fill:#ffcdd2
```

**Promotion Timeline:**

| Stage | Duration | Gates | Can Skip? |
|-------|----------|-------|-----------|
| **Local Dev → PR** | Minutes | Pre-commit hooks, local tests | No |
| **PR → Dev Deploy** | 2-5 minutes | CI pipeline | No |
| **Dev → Staging** | Immediate on merge | Code review, CI pass | No |
| **Staging Testing** | 4-24 hours | E2E, load tests, QA | No |
| **Staging → Prod Approval** | 15 min - 2 days | Manual approval, change ticket | No (except emergency) |
| **Prod Deployment** | 2 hours | Health checks, monitoring | No |
| **Total (Normal)** | 1-3 days | All gates | - |
| **Total (Hotfix)** | 1-2 hours | Emergency approval only | Some (with CTO approval) |

### Promotion Checklist

**Before promoting to staging**:
- [ ] All tests pass
- [ ] Code reviewed and approved
- [ ] No security vulnerabilities
- [ ] Documentation updated
- [ ] Database migrations tested

**Before promoting to production**:
- [ ] Staging tests pass
- [ ] Performance acceptable
- [ ] QA sign-off
- [ ] Rollback plan ready
- [ ] Monitoring configured
- [ ] On-call engineer available

---

## 🏗️ Environment Isolation Architecture

### Infrastructure Separation

How we maintain strict isolation between environments for security and reliability:

```mermaid
flowchart TB
    subgraph Internet["🌐 Internet"]
        Users[End Users]
        Developers[Developers]
    end

    subgraph DevEnv["🔧 Development Environment"]
        DevVPC[Dev VPC<br/>10.0.0.0/16<br/>Isolated network]
        DevApp[App Servers<br/>1x t3.small<br/>Docker Compose]
        DevDB[(Dev Database<br/>PostgreSQL<br/>db.t3.micro<br/>Public snapshots)]
        DevCache[(Dev Redis<br/>Elasticache<br/>cache.t3.micro)]
        DevSecrets[Dev Secrets<br/>AWS Secrets Manager<br/>/dev/* namespace<br/>Test API keys]
    end

    subgraph StagingEnv["🎭 Staging Environment"]
        StagingVPC[Staging VPC<br/>10.1.0.0/16<br/>Isolated network]
        StagingLB[Load Balancer<br/>ALB]
        StagingApp[App Servers<br/>2x t3.medium<br/>Auto-scaling 2-4]
        StagingDB[(Staging Database<br/>PostgreSQL<br/>db.t3.medium<br/>Sanitized data)]
        StagingCache[(Staging Redis<br/>Elasticache<br/>cache.t3.small)]
        StagingSecrets[Staging Secrets<br/>AWS Secrets Manager<br/>/staging/* namespace<br/>Non-prod API keys]
    end

    subgraph ProdEnv["🚀 Production Environment"]
        ProdVPC[Production VPC<br/>10.2.0.0/16<br/>Multi-AZ, isolated]
        ProdCDN[CloudFront CDN<br/>Global edge]
        ProdLB[Load Balancer<br/>ALB<br/>Multi-AZ]
        ProdApp[App Servers<br/>10x c5.xlarge<br/>Auto-scaling 5-50]
        ProdDB[(Production Database<br/>PostgreSQL<br/>db.r5.xlarge<br/>Multi-AZ<br/>Encrypted<br/>Auto backups)]
        ProdCache[(Production Redis<br/>Elasticache<br/>cache.r5.large<br/>Replication)]
        ProdSecrets[Production Secrets<br/>AWS Secrets Manager<br/>/production/* namespace<br/>Auto-rotation enabled]
    end

    subgraph Shared["📦 Shared Infrastructure"]
        CI[CI/CD Pipeline<br/>GitHub Actions<br/>Deploys to all envs]
        Monitoring[Monitoring<br/>Datadog/Grafana<br/>All environments]
        Logs[Log Aggregation<br/>CloudWatch/Loki<br/>Separate log groups]
        IAM[IAM & Access Control<br/>Separate roles per env<br/>Least privilege]
    end

    subgraph IsolationBoundaries["🔒 Isolation Boundaries"]
        NetworkIso[Network Isolation:<br/>• Separate VPCs<br/>• No cross-env traffic<br/>• Security groups]
        DataIso[Data Isolation:<br/>• Separate databases<br/>• No prod data in lower envs<br/>• Data sanitization]
        SecretIso[Secret Isolation:<br/>• Namespace separation<br/>• IAM role restrictions<br/>• No cross-env access]
        AccessIso[Access Isolation:<br/>• Devs: Dev + Staging<br/>• Platform: All envs<br/>• Prod: Read-only for most]
    end

    Users --> ProdCDN
    ProdCDN --> ProdLB

    Developers --> DevApp
    Developers -.->|Testing only| StagingLB

    DevApp --> DevDB
    DevApp --> DevCache
    DevApp --> DevSecrets

    StagingLB --> StagingApp
    StagingApp --> StagingDB
    StagingApp --> StagingCache
    StagingApp --> StagingSecrets

    ProdLB --> ProdApp
    ProdApp --> ProdDB
    ProdApp --> ProdCache
    ProdApp --> ProdSecrets

    CI -.->|Deploy| DevApp
    CI -.->|Deploy| StagingApp
    CI -.->|Deploy| ProdApp

    DevApp -.-> Monitoring
    StagingApp -.-> Monitoring
    ProdApp -.-> Monitoring

    DevApp -.-> Logs
    StagingApp -.-> Logs
    ProdApp -.-> Logs

    IAM -.-> DevSecrets
    IAM -.-> StagingSecrets
    IAM -.-> ProdSecrets

    DevVPC -.-> NetworkIso
    StagingVPC -.-> NetworkIso
    ProdVPC -.-> NetworkIso

    DevDB -.-> DataIso
    StagingDB -.-> DataIso
    ProdDB -.-> DataIso

    style DevVPC fill:#bbdefb
    style StagingVPC fill:#fff9c4
    style ProdVPC fill:#ffccbc
    style DevSecrets fill:#c8e6c9
    style StagingSecrets fill:#c8e6c9
    style ProdSecrets fill:#c8e6c9
    style NetworkIso fill:#ffe5b4
    style DataIso fill:#ffe5b4
    style SecretIso fill:#ffe5b4
    style AccessIso fill:#ffe5b4
```

**Isolation Principles:**

| Isolation Type | Implementation | Purpose | Example |
|----------------|----------------|---------|---------|
| **Network** | Separate VPCs, security groups | Prevent unauthorized access | Dev VPC: 10.0.0.0/16, Prod VPC: 10.2.0.0/16 |
| **Data** | Separate databases, sanitization | Protect customer data | Prod DB encrypted, staging has fake emails |
| **Secrets** | Namespace separation, IAM roles | Prevent credential leakage | Dev can't read /production/* secrets |
| **Access** | Role-based access control | Least privilege | Devs have read-only prod access |
| **Compute** | Separate AWS accounts (optional) | Blast radius containment | Dev account != Prod account |

**AWS Account Strategy:**

**Option 1: Single Account (Simpler)**
- ✅ Easier to manage
- ✅ Lower overhead
- ❌ Shared resource limits
- ❌ Blast radius risk

**Option 2: Multi-Account (More Secure)**
- ✅ Complete isolation
- ✅ Separate billing and limits
- ✅ Better compliance
- ❌ More complex setup
- ❌ Cross-account access needed

**Recommended: Multi-account for companies with >10 engineers or compliance requirements (SOC2, HIPAA)**

**Cross-Environment Access Rules:**

| Environment | Developers | QA Team | Platform Team | Executives |
|-------------|-----------|---------|---------------|------------|
| **Development** | Full access | No access | Full access | No access |
| **Staging** | Read + Deploy | Full access | Full access | Read-only |
| **Production** | Read-only logs | Read-only | Full access | Read-only dashboards |

---

## 📊 Environment Parity

### 12-Factor App: Dev/Prod Parity

**Keep development, staging, and production as similar as possible**:

| Factor | Traditional | Modern (12-Factor) |
|--------|-------------|-------------------|
| **Time** | Weeks between deploys | Hours between deploys |
| **People** | Devs write, ops deploy | Devs write and deploy |
| **Tools** | Different tools per env | Same tools all envs |

### Achieving Parity

```dockerfile
# Same Dockerfile for all environments
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --production

COPY . .

# Environment-specific behavior via env vars
ENV NODE_ENV=production

CMD ["node", "server.js"]
```

### Configuration Differences

**Similar infrastructure**:
```hcl
# Development: 1 small instance
# Staging: 2 medium instances
# Production: 10 large instances + autoscaling

# But same structure!
module "app" {
  instance_type = var.instance_type  # Different values
  # ... same module code
}
```

---

## 🧪 Test Data Management

### Staging Data Strategy

**Options**:
1. **Sanitized production data**: Copy prod, remove PII
2. **Synthetic data**: Generate realistic fake data
3. **Anonymized data**: Hash/encrypt sensitive fields
4. **Subset of production**: Recent data only

**Never use real customer data in non-production environments!**

### Data Sanitization Example

```sql
-- Sanitize production data for staging
UPDATE users
SET
  email = CONCAT('user', id, '@example.com'),
  phone = NULL,
  address = 'Test Address',
  ssn = NULL
WHERE environment = 'staging';
```

See [CI_CD.md](CI_CD.md), [INFRASTRUCTURE.md](INFRASTRUCTURE.md), and [DEPLOYMENT.md](DEPLOYMENT.md) for complete DevOps guidance.

---

*This environment management guide is maintained with care and consciousness by the Luminous Dynamics community.*
