# 🏗️ Infrastructure as Code (IaC)

> "Infrastructure should be versionable, testable, and reproducible—just like application code."

*Last updated: January 2025*

This document outlines our approach to **Infrastructure as Code**—managing infrastructure through declarative configuration files rather than manual processes, enabling version control, testing, and automation of infrastructure.

---

## 🎯 IaC Philosophy

### What is Infrastructure as Code?

**Infrastructure as Code (IaC)** treats infrastructure configuration as software code:
- **Version controlled** in Git
- **Reviewed** through pull requests  
- **Tested** before deployment
- **Automated** with CI/CD
- **Documented** through code itself
- **Reproducible** across environments

### Why IaC Matters

**Without IaC** (manual/clickops):
- ❌ Configuration drift between environments
- ❌ "Works on my machine" but not production
- ❌ No audit trail of changes
- ❌ Disaster recovery requires tribal knowledge
- ❌ Scaling requires manual repetition
- ❌ Environment setup takes days/weeks

**With IaC**:
- ✅ Consistent environments
- ✅ Version history of all changes
- ✅ Automated testing and validation
- ✅ Disaster recovery is `terraform apply`
- ✅ Scaling is change a number
- ✅ Environment setup takes minutes

### IaC Principles

1. **Declarative over imperative**: Describe desired state, not steps to achieve it
2. **Idempotent**: Running twice produces same result as running once
3. **Version controlled**: All infrastructure code in Git
4. **Immutable infrastructure**: Replace, don't modify
5. **Modular and reusable**: DRY principles apply
6. **Environment parity**: Dev/staging/prod should be identical
7. **Self-documenting**: Code is the documentation

---

## 🛠️ IaC Tools

### Tool Comparison

| Tool | Best For | Language | State | Cloud |
|------|----------|----------|-------|-------|
| **Terraform** | Multi-cloud | HCL | Remote state | All |
| **Pulumi** | Developers | Real languages (TypeScript, Python) | SaaS/S3 | All |
| **CloudFormation** | AWS-only | YAML/JSON | AWS-managed | AWS only |
| **Ansible** | Configuration mgmt | YAML | Stateless | Any |
| **CDK** | AWS developers | TypeScript, Python | CloudFormation | AWS |

### Terraform (Recommended)

**Why Terraform**:
- Industry standard for IaC
- Multi-cloud support
- Large provider ecosystem
- Strong community
- Mature tooling

**Example Terraform**:
```hcl
# main.tf
terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "production/terraform.tfstate"
    region = "us-east-1"
    encrypt = true
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Project     = "luminous-dynamics"
    }
  }
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "${var.environment}-vpc"
  }
}

# Subnets
resource "aws_subnet" "public" {
  count = 2
  
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.${count.index}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${var.environment}-public-${count.index + 1}"
  }
}

# Application server
resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public[0].id
  
  vpc_security_group_ids = [aws_security_group.app.id]
  
  user_data = file("${path.module}/user-data.sh")
  
  tags = {
    Name = "${var.environment}-app-server"
  }
}
```

### Pulumi

**Why Pulumi**:
- Use real programming languages
- Better for complex logic
- Type safety and IDE support
- Great for developers

**Example Pulumi (TypeScript)**:
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create VPC
const vpc = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
    enableDnsHostnames: true,
    enableDnsSupport: true,
    tags: {
        Name: `${pulumi.getStack()}-vpc`,
    },
});

// Create subnets
const publicSubnets = [];
for (let i = 0; i < 2; i++) {
    const subnet = new aws.ec2.Subnet(`public-${i}`, {
        vpcId: vpc.id,
        cidrBlock: `10.0.${i}.0/24`,
        availabilityZone: aws.getAvailabilityZones().then(azs => azs.names[i]),
        mapPublicIpOnLaunch: true,
        tags: {
            Name: `${pulumi.getStack()}-public-${i + 1}`,
        },
    });
    publicSubnets.push(subnet);
}

// Export outputs
export const vpcId = vpc.id;
export const subnetIds = publicSubnets.map(s => s.id);
```

See [CI_CD.md](CI_CD.md), [DEPLOYMENT.md](DEPLOYMENT.md), and [ENVIRONMENTS.md](ENVIRONMENTS.md) for complete DevOps guidance.

---

*This infrastructure guide is maintained with care and consciousness by the Luminous Dynamics community.*
