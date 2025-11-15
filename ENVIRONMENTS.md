# 🌍 Environment Management

> "Production is not the place to discover environment differences."

*Last updated: January 2025*

This document outlines **environment management**—how we maintain development, staging, and production environments with proper configuration management, secrets handling, and environment parity to ensure reliability and security across the software delivery lifecycle.

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

```
Developer → Feature Branch → Dev Environment
                ↓
            Pull Request Review
                ↓
            Main Branch → Staging Environment
                ↓
            QA/UAT Testing
                ↓
            Production Deploy
```

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
