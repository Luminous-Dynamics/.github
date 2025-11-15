# 📈 Scaling

> "Premature optimization is the root of all evil." — Donald Knuth
> "Premature pessimization is the root of all mediocrity." — We add this corollary

*Last updated: January 2025*

This document outlines our **scaling philosophy and practices**—when to scale, how to scale (horizontal vs vertical), caching strategies, load balancing, database scaling, and the trade-offs involved in building systems that serve millions of users reliably.

---

## 🎯 Scaling Philosophy

### When to Scale

**Don't scale prematurely**:
- ❌ "We might need to handle 1M users someday"
- ❌ Building for hypothetical traffic
- ❌ Over-engineering for problems you don't have

**Do scale when**:
- ✅ Current system can't handle load
- ✅ Response times degrading
- ✅ Error rates increasing
- ✅ Clear growth trajectory
- ✅ Cost of NOT scaling > cost of scaling

### Scaling Principles

1. **Measure first**: You can't improve what you don't measure
2. **Identify bottlenecks**: Find the constraint (CPU, memory, disk, network, database)
3. **Optimize before scaling**: Often cheaper than adding servers
4. **Scale incrementally**: Small steps, measure impact
5. **Plan for failure**: Redundancy and graceful degradation
6. **Automate**: Manual scaling doesn't scale

---

## 📊 Types of Scaling

### Vertical Scaling (Scale Up)

**What**: Increase resources of a single machine (more CPU, RAM, disk)

**Pros**:
- ✅ Simple (no code changes)
- ✅ No distributed system complexity
- ✅ Existing tools work
- ✅ Lower latency (single machine)

**Cons**:
- ❌ Physical limits (can't add infinite RAM)
- ❌ Single point of failure
- ❌ Expensive at high end
- ❌ Downtime during upgrades

**When to use**:
- Early stage, traffic growing
- Database needs more memory
- Cheaper than horizontal scaling
- Application not ready for distribution

**Example**:
```bash
# AWS: Resize instance
aws ec2 modify-instance-attribute \
  --instance-id i-1234567890abcdef0 \
  --instance-type t3.xlarge  # Was t3.medium

# Requires instance stop/start (downtime!)
```

### Horizontal Scaling (Scale Out)

**What**: Add more machines to handle load

**Pros**:
- ✅ No theoretical limit
- ✅ Better fault tolerance (redundancy)
- ✅ Cost-effective (commodity hardware)
- ✅ Can scale on demand (autoscaling)

**Cons**:
- ❌ Application must support it
- ❌ Complexity (load balancing, state management)
- ❌ Data consistency challenges
- ❌ More operational overhead

**When to use**:
- Traffic spikes unpredictably
- Need high availability
- Hit vertical scaling limits
- Cost-effective at scale

**Example**:
```yaml
# Kubernetes: Horizontal Pod Autoscaler
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  minReplicas: 3
  maxReplicas: 50
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

---

## ⚡ Caching Strategies

### Why Cache?

**Without caching**: Every request hits database/API (slow, expensive)
**With caching**: Serve frequently requested data from memory (fast, cheap)

### Cache Layers

```
User Request
    ↓
1. CDN (static assets: images, CSS, JS)
    ↓
2. Application cache (rendered HTML, API responses)
    ↓
3. Database query cache (frequent queries)
    ↓
4. Database (source of truth)
```

### Common Caching Strategies

**Cache-Aside (Lazy Loading)**:
```javascript
async function getUser(userId) {
  // 1. Check cache first
  let user = await cache.get(`user:${userId}`);

  if (user) {
    return user;  // Cache hit!
  }

  // 2. Cache miss - fetch from database
  user = await db.users.findOne({ id: userId });

  // 3. Store in cache for next time
  await cache.set(`user:${userId}`, user, { ttl: 3600 });  // 1 hour

  return user;
}
```

**Write-Through**:
```javascript
async function updateUser(userId, data) {
  // 1. Update database
  const user = await db.users.update({ id: userId }, data);

  // 2. Update cache immediately
  await cache.set(`user:${userId}`, user, { ttl: 3600 });

  return user;
}
```

**Write-Behind (Write-Back)**:
```javascript
async function updateUser(userId, data) {
  // 1. Update cache immediately (fast!)
  await cache.set(`user:${userId}`, data);

  // 2. Queue database write for later (async)
  await writeQueue.add({ userId, data });

  return data;
}
```

### Cache Invalidation

**Time-based (TTL)**:
```javascript
await cache.set('user:123', user, { ttl: 3600 });  // Expire after 1 hour
```

**Event-based**:
```javascript
// When user updates profile
eventBus.on('user.updated', async (userId) => {
  await cache.del(`user:${userId}`);  // Invalidate cache
});
```

### Popular Caching Tools

| Tool | Type | Best For |
|------|------|----------|
| **Redis** | In-memory | Fast key-value, pub/sub, sessions |
| **Memcached** | In-memory | Simple key-value caching |
| **Varnish** | HTTP cache | Reverse proxy caching |
| **CloudFlare** | CDN | Static assets, global distribution |
| **AWS CloudFront** | CDN | AWS-integrated CDN |

---

## 🔀 Load Balancing

### What is Load Balancing?

Distribute traffic across multiple servers to:
- Prevent overloading a single server
- Improve reliability (failover)
- Enable horizontal scaling
- Maximize throughput

### Load Balancing Algorithms

**Round Robin**: Distribute evenly across servers
```
Request 1 → Server A
Request 2 → Server B
Request 3 → Server C
Request 4 → Server A  (repeat)
```

**Least Connections**: Send to server with fewest active connections
```
Server A: 10 connections
Server B: 5 connections   ← Send here!
Server C: 8 connections
```

**IP Hash**: Same client always goes to same server (session affinity)
```
hash(client_ip) % num_servers = server_index
```

### Load Balancer Types

**Layer 4 (Transport)**: Based on IP/port (fast, simple)
**Layer 7 (Application)**: Based on HTTP headers, paths, cookies (smart, flexible)

### Example: Nginx Load Balancer

```nginx
upstream app_servers {
  # Load balancing method
  least_conn;

  # Backend servers
  server app1.example.com:3000 weight=3;
  server app2.example.com:3000 weight=2;
  server app3.example.com:3000 weight=1;

  # Health checks
  server app4.example.com:3000 backup;
}

server {
  listen 80;

  location / {
    proxy_pass http://app_servers;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;

    # Timeout settings
    proxy_connect_timeout 5s;
    proxy_send_timeout 60s;
    proxy_read_timeout 60s;
  }
}
```

---

## 🗄️ Database Scaling

### Read Replicas

**Problem**: Database reads are 80%+ of queries, overwhelming primary

**Solution**: Replicate data to read-only replicas

```
                    ┌──────────────┐
                    │   Primary    │
                    │  (writes)    │
                    └──────┬───────┘
                           │
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │ Replica 1│    │ Replica 2│    │ Replica 3│
    │  (reads) │    │  (reads) │    │  (reads) │
    └──────────┘    └──────────┘    └──────────┘
```

**Implementation**:
```javascript
// Write to primary
await primaryDb.users.create({ name: 'Alice' });

// Read from replica (slightly stale data ok)
const users = await replicaDb.users.find({ active: true });
```

### Sharding (Horizontal Partitioning)

**Problem**: Single database too large, even with replicas

**Solution**: Split data across multiple databases

```
Users 0-1M     → Shard 1
Users 1M-2M    → Shard 2
Users 2M-3M    → Shard 3
```

**Sharding strategies**:
- **Range-based**: User IDs 0-1M, 1M-2M, etc.
- **Hash-based**: hash(user_id) % num_shards
- **Geographic**: US users → US shard, EU users → EU shard

**Example**:
```javascript
function getShardForUser(userId) {
  return userId % NUM_SHARDS;
}

async function getUser(userId) {
  const shardId = getShardForUser(userId);
  const db = shards[shardId];
  return db.users.findOne({ id: userId });
}
```

### Database Indexes

**Before indexing** (slow):
```sql
-- Full table scan: O(n)
SELECT * FROM users WHERE email = 'alice@example.com';
-- Scans 10M rows!
```

**After indexing** (fast):
```sql
-- Create index
CREATE INDEX idx_users_email ON users(email);

-- Now O(log n) lookup
SELECT * FROM users WHERE email = 'alice@example.com';
-- Uses index: 10M rows → 20 comparisons
```

### Connection Pooling

```javascript
// Bad: Create new connection per request (slow!)
app.get('/users', async (req, res) => {
  const db = await connectToDatabase();  // 100ms overhead!
  const users = await db.users.find();
  await db.close();
  res.json(users);
});

// Good: Reuse connection pool
const pool = createPool({
  min: 5,
  max: 50,
  acquireTimeout: 30000
});

app.get('/users', async (req, res) => {
  const users = await pool.query('SELECT * FROM users');
  res.json(users);
});
```

---

## 🚀 Autoscaling

### When to Autoscale

**Scale up when**:
- CPU > 70% for 5 minutes
- Memory > 80%
- Request queue depth > 100
- Response time > 1s

**Scale down when**:
- CPU < 30% for 10 minutes
- Low traffic periods
- Cost optimization

### AWS Auto Scaling Group

```json
{
  "AutoScalingGroupName": "app-asg",
  "MinSize": 2,
  "MaxSize": 20,
  "DesiredCapacity": 5,
  "HealthCheckType": "ELB",
  "HealthCheckGracePeriod": 300,

  "TargetTrackingScaling": {
    "TargetValue": 70.0,
    "PredefinedMetric": "ASGAverageCPUUtilization"
  }
}
```

---

## 🌍 Geographic Distribution

### Why Distribute Globally?

- **Latency**: Users in Tokyo shouldn't hit servers in Virginia
- **Reliability**: If one region fails, others continue
- **Compliance**: Some countries require data stay in-country

### Multi-Region Architecture

```
                    ┌─────────────┐
                    │   Route 53   │ (DNS)
                    │ (GeoDNS)     │
                    └──────┬───────┘
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
    ┌──────────┐     ┌──────────┐     ┌──────────┐
    │US Region │     │EU Region │     │APAC Region│
    │          │     │          │     │           │
    │ App+DB   │     │ App+DB   │     │ App+DB    │
    └──────────┘     └──────────┘     └───────────┘
```

---

## 📈 Scaling Checklist

**Before you scale**:
- [ ] Measure current performance
- [ ] Identify bottleneck (CPU, memory, database, network)
- [ ] Try optimization first
- [ ] Estimate cost of scaling
- [ ] Plan monitoring

**When scaling**:
- [ ] Start small (add 1-2 servers, not 10)
- [ ] Monitor impact
- [ ] Test failover
- [ ] Document changes
- [ ] Update runbooks

**After scaling**:
- [ ] Verify performance improvement
- [ ] Check for new bottlenecks
- [ ] Optimize costs
- [ ] Plan next steps

See [PERFORMANCE.md](PERFORMANCE.md), [INFRASTRUCTURE.md](INFRASTRUCTURE.md), [OBSERVABILITY.md](OBSERVABILITY.md) for complete scaling guidance.

---

*This scaling guide is maintained with care and consciousness by the Luminous Dynamics community.*
