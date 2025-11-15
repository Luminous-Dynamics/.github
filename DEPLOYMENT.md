# 🚀 Deployment Strategies

> "The best deployment is one you don't notice happened."

*Last updated: January 2025*

This document outlines **deployment strategies**—how we safely ship code to production with zero downtime, fast rollback capabilities, and confidence that changes won't break user experiences.

---

## 🎯 Deployment Philosophy

### Deployment Principles

1. **Automate everything**: Manual steps get forgotten
2. **Deploy frequently**: Small changes are less risky
3. **Rollback should be trivial**: Every deploy can be undone in <5 minutes
4. **Decouple deploy from release**: Use feature flags
5. **Test in production-like environment**: Staging mirrors prod
6. **Monitor during and after**: Know immediately if something breaks

---

## 📊 Deployment Strategies Comparison

| Strategy | Downtime | Rollback Speed | Complexity | Cost |
|----------|----------|----------------|------------|------|
| **Rolling** | None | Medium (5-15min) | Low | Same |
| **Blue-Green** | None | Instant (<1min) | Medium | 2x during deploy |
| **Canary** | None | Fast (<5min) | High | Same |
| **Feature Flags** | None | Instant | Medium | Same |

###rolling Deployment

**What**: Update instances gradually.

**How**:
```
[V1] [V1] [V1] [V1]
[V2] [V1] [V1] [V1]  ← Update one
[V2] [V2] [V1] [V1]
[V2] [V2] [V2] [V2]  ← All updated
```

**When to use**: Default for most applications

### Blue-Green Deployment

**What**: Two identical environments. Switch traffic instantly.

**How**:
```
Blue (V1)  ← 100% traffic
Green (V2) ← Deploy here, test
           ← Switch!
Blue (V1)  ← Idle (ready for rollback)
Green (V2) ← 100% traffic
```

**When to use**: When instant rollback is critical

### Canary Deployment  

**What**: Deploy to 5% of users, gradually increase.

**How**:
```
5% → V2, 95% → V1  (monitor)
25% → V2, 75% → V1 (looking good)
100% → V2          (fully deployed)
```

**When to use**: High-traffic apps, risky changes

### Feature Flags

**What**: Deploy code disabled, enable gradually.

**Code**:
```javascript
if (featureFlags.isEnabled('new-checkout')) {
  return <NewCheckout />;
}
return <OldCheckout />;
```

**When to use**: Large features, A/B testing

---

## 🛡️ Zero-Downtime Deployments

**Health checks ensure traffic only goes to healthy instances**:

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
```

**Database migrations**: Use expand-contract pattern
1. Expand: Add new column
2. Deploy: Write to both columns  
3. Backfill: Migrate data
4. Contract: Remove old column

---

## 🔄 Rollback

**When to rollback**:
- Error rate spikes >2x
- Key flows broken
- Performance degrades
- Data corruption

**How**:
- Blue-green: Switch back (<1min)
- Rolling: Deploy previous version (5-15min)
- Canary: Route all to V1 (<1min)
- Feature flag: Disable (instant)

See [CI_CD.md](CI_CD.md), [INFRASTRUCTURE.md](INFRASTRUCTURE.md), [ENVIRONMENTS.md](ENVIRONMENTS.md) for complete guidance.

---

*This deployment guide is maintained with care and consciousness by the Luminous Dynamics community.*
