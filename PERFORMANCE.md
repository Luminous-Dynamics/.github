# ⚡ Performance Standards

> "Performance is accessibility. Performance is respect. Performance is sustainability. Every millisecond saved is energy conserved and user time honored."

This document defines performance standards, budgets, and optimization guidelines for all Luminous Dynamics projects.

---

## 🎯 Performance Philosophy

### Why Performance Matters

1. **Accessibility**
   - Fast sites work on slow devices and networks
   - Performance = serving more users
   - Especially critical for users in developing regions

2. **User Respect**
   - Time is precious—don't waste it
   - Users shouldn't wait for unnecessarily slow software
   - Good performance signals care for users

3. **Environmental Impact**
   - CPU cycles = energy consumption
   - Efficient code = smaller carbon footprint
   - Sustainable technology serves the planet

4. **Cost**
   - Better performance = lower infrastructure costs
   - Fewer servers needed
   - More users served per dollar

5. **Trust**
   - Slow software feels broken
   - Fast software feels polished
   - Performance builds confidence

### Core Principles

1. **Measure First, Optimize Second**
   - Don't guess—profile and measure
   - Fix what actually matters
   - Premature optimization wastes time

2. **User-Perceived Performance > Raw Speed**
   - 100ms perceived = better than 50ms hidden
   - Loading states and feedback matter
   - Perceived performance is UX, not just engineering

3. **Progressive Enhancement**
   - Core functionality fast for everyone
   - Enhanced features for capable devices
   - Graceful degradation

4. **Performance as Feature**
   - Budget for performance in planning
   - Test performance in CI/CD
   - Monitor performance in production

---

## 📊 Performance Budgets

### Web Applications (Terra Atlas, Visualizers)

**Core Web Vitals (Target):

**
- **LCP (Largest Contentful Paint)**: < 2.5s (Good), < 4s (Acceptable)
- **FID (First Input Delay)**: < 100ms (Good), < 300ms (Acceptable)
- **CLS (Cumulative Layout Shift)**: < 0.1 (Good), < 0.25 (Acceptable)

**Additional Metrics:**
- **Time to Interactive (TTI)**: < 3.5s on 4G
- **First Contentful Paint (FCP)**: < 1.5s
- **Speed Index**: < 3s
- **Total Blocking Time (TBT)**: < 300ms

**Asset Budgets:**
```
Total JavaScript:     < 200KB (gzipped)
Total CSS:           < 50KB (gzipped)
Total Images:        < 500KB (optimized)
Total Fonts:         < 100KB (subsetted)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Page Weight:   < 1MB (first load)
```

**Request Budgets:**
```
HTTP Requests:       < 50 (first load)
Third-party requests: < 10
```

### APIs (Mycelix, Backend Services)

**Response Time (p95):**
```
Simple queries:      < 100ms
Complex queries:     < 500ms
Byzantine detection: < 1ms (Mycelix requirement)
Bulk operations:     < 2s
```

**Throughput:**
```
Mycelix:             > 1000 req/s
Terra Atlas API:     > 500 req/s
```

**Database:**
```
Query time (p95):    < 50ms
Index coverage:      > 95% of queries
Connection pool:     Properly configured (no exhaustion)
```

### CLI Tools

**Startup Time:**
```
Simple commands:     < 100ms
Complex commands:    < 500ms
Help text:           < 50ms
```

**Responsiveness:**
```
Interactive prompts: < 50ms response to input
Progress updates:    At least every 500ms for long operations
```

### Build Times

```
Development build:   < 10s
Production build:    < 2 minutes
Test suite:          < 5 minutes
CI/CD pipeline:      < 10 minutes
```

---

## 🔍 Measuring Performance

### Web Performance

**Lighthouse CI:**
```yaml
# .github/workflows/performance.yml
name: Performance Tests

on: [pull_request]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Lighthouse CI
        run: |
          npm install -g @lhci/cli
          lhci autorun
        env:
          LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_TOKEN }}

# lighthouserc.js
module.exports = {
  ci: {
    collect: {
      url: ['http://localhost:3000'],
      numberOfRuns: 3,
    },
    assert: {
      assertions: {
        'categories:performance': ['error', {minScore: 0.9}],
        'first-contentful-paint': ['error', {maxNumericValue: 1500}],
        'interactive': ['error', {maxNumericValue: 3500}],
        'speed-index': ['error', {maxNumericValue: 3000}],
      },
    },
  },
};
```

**Real User Monitoring (RUM):**
```javascript
// Track Core Web Vitals
import {getCLS, getFID, getLCP} from 'web-vitals';

function sendToAnalytics({name, delta, value, id}) {
  fetch('/analytics', {
    method: 'POST',
    body: JSON.stringify({metric: name, value, id}),
  });
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getLCP(sendToAnalytics);
```

### API Performance

**APM (Application Performance Monitoring):**
```python
# Example with OpenTelemetry
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

@app.get("/federations/{id}")
async def get_federation(id: str):
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("get_federation"):
        # Your code here
        pass
```

**Database Query Monitoring:**
```sql
-- Enable slow query log (MySQL/PostgreSQL)
SET slow_query_log = 1;
SET long_query_time = 0.05;  -- 50ms threshold
```

### Profiling

**Python:**
```python
# cProfile for CPU profiling
python -m cProfile -o output.prof your_script.py

# Memory profiling
from memory_profiler import profile

@profile
def memory_intensive_function():
    # Your code
    pass
```

**JavaScript:**
```javascript
// Browser DevTools Performance tab
// Or programmatic profiling
console.time('expensive-operation');
expensiveOperation();
console.timeEnd('expensive-operation');
```

---

## 🚀 Optimization Strategies

### Frontend Optimization

**1. Code Splitting**
```javascript
// Load routes on demand
const Dashboard = lazy(() => import('./pages/Dashboard'));
const FederationDetail = lazy(() => import('./pages/FederationDetail'));

<Routes>
  <Route path="/" element={<Suspense fallback={<Loading />}><Dashboard /></Suspense>} />
  <Route path="/federation/:id" element={<Suspense><FederationDetail /></Suspense>} />
</Routes>
```

**2. Asset Optimization**
```bash
# Image optimization
npm install sharp
# Then in build: convert images to WebP, generate multiple sizes

# Font subsetting
npx glyphhanger --subset=*.ttf --formats=woff2

# Tree shaking (automatic with modern bundlers)
# But verify: analyze bundle with webpack-bundle-analyzer
```

**3. Caching**
```nginx
# Static assets: long cache
location /static/ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}

# HTML: no cache (to get updates)
location / {
    add_header Cache-Control "no-cache";
}
```

**4. Lazy Loading**
```html
<!-- Images -->
<img src="hero.jpg" loading="lazy" alt="Description" />

<!-- iframes -->
<iframe src="map" loading="lazy"></iframe>
```

**5. Critical CSS**
```html
<!-- Inline critical CSS for above-the-fold content -->
<style>
  /* Critical CSS extracted and inlined */
  .header { /* styles */ }
</style>

<!-- Defer non-critical CSS -->
<link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'">
```

### Backend Optimization

**1. Database Indexing**
```sql
-- Add indexes for frequently queried columns
CREATE INDEX idx_participant_trust ON participants(trust_score);

-- Composite indexes for common query patterns
CREATE INDEX idx_federation_status ON federations(status, created_at);

-- Analyze query plans
EXPLAIN ANALYZE SELECT * FROM participants WHERE trust_score > 0.5;
```

**2. Query Optimization**
```python
# ❌ N+1 query problem
for federation in federations:
    participants = federation.participants.all()  # Query per federation!

# ✅ Eager loading
federations = Federation.objects.prefetch_related('participants').all()
```

**3. Caching**
```python
from functools import lru_cache
import redis

# In-memory cache for expensive computations
@lru_cache(maxsize=1000)
def calculate_byzantine_resistance(participant_ids, threshold):
    # Expensive calculation
    pass

# Redis for shared cache
redis_client = redis.Redis()

def get_federation(id):
    # Check cache first
    cached = redis_client.get(f"federation:{id}")
    if cached:
        return json.loads(cached)

    # Not in cache: fetch from DB
    federation = db.query(Federation).get(id)

    # Store in cache (5 minute TTL)
    redis_client.setex(
        f"federation:{id}",
        300,
        json.dumps(federation.to_dict())
    )

    return federation
```

**4. Async/Concurrency**
```python
# Run independent operations concurrently
import asyncio

async def get_federation_data(id):
    # Fetch these in parallel
    participants, metrics, history = await asyncio.gather(
        fetch_participants(id),
        fetch_metrics(id),
        fetch_history(id),
    )
    return {
        'participants': participants,
        'metrics': metrics,
        'history': history,
    }
```

**5. Connection Pooling**
```python
# PostgreSQL connection pool
from sqlalchemy.pool import QueuePool

engine = create_engine(
    'postgresql://user:pass@localhost/db',
    poolclass=QueuePool,
    pool_size=20,  # Max connections
    max_overflow=10,  # Extra connections during spikes
    pool_pre_ping=True,  # Verify connections before use
)
```

### Algorithm Optimization

**1. Time Complexity**
```python
# ❌ O(n²) - Slow for large datasets
def find_duplicates(participants):
    duplicates = []
    for i in range(len(participants)):
        for j in range(i+1, len(participants)):
            if participants[i].id == participants[j].id:
                duplicates.append(participants[i])
    return duplicates

# ✅ O(n) - Much faster
def find_duplicates(participants):
    seen = set()
    duplicates = []
    for p in participants:
        if p.id in seen:
            duplicates.append(p)
        seen.add(p.id)
    return duplicates
```

**2. Space Complexity**
```python
# ❌ Memory inefficient (loads all in memory)
def process_large_dataset():
    all_data = load_all_participants()  # Could be millions!
    return [process(p) for p in all_data]

# ✅ Stream processing (constant memory)
def process_large_dataset():
    for batch in load_participants_in_batches(size=1000):
        for p in batch:
            yield process(p)
```

---

## 🧪 Performance Testing

### Load Testing

**Locust (Python):**
```python
from locust import HttpUser, task, between

class MycelixUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_federations(self):
        self.client.get("/api/federations")

    @task(3)  # 3x more common
    def get_federation_detail(self):
        federation_id = random.choice(self.federation_ids)
        self.client.get(f"/api/federations/{federation_id}")

# Run: locust -f loadtest.py --users 100 --spawn-rate 10
```

**k6 (JavaScript):**
```javascript
import http from 'k6/http';
import {check, sleep} from 'k6';

export let options = {
  stages: [
    {duration: '30s', target: 20},   // Ramp up to 20 users
    {duration: '1m', target: 100},   // Ramp up to 100 users
    {duration: '30s', target: 0},    // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests < 500ms
  },
};

export default function() {
  const res = http.get('http://test.api.com/federations');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

### Benchmarking

**Python (pytest-benchmark):**
```python
def test_byzantine_detection_performance(benchmark):
    participants = [create_participant() for _ in range(1000)]

    result = benchmark(
        calculate_byzantine_resistance,
        participants,
        threshold=0.3
    )

    # Assert performance requirement
    assert benchmark.stats.mean < 0.001  # < 1ms average
```

**JavaScript (Benchmark.js):**
```javascript
const Benchmark = require('benchmark');
const suite = new Benchmark.Suite;

suite
  .add('Array#forEach', function() {
    array.forEach(item => process(item));
  })
  .add('for loop', function() {
    for (let i = 0; i < array.length; i++) {
      process(array[i]);
    }
  })
  .on('cycle', function(event) {
    console.log(String(event.target));
  })
  .on('complete', function() {
    console.log('Fastest is ' + this.filter('fastest').map('name'));
  })
  .run();
```

---

## 📈 Performance Monitoring

### Metrics to Track

**Application Metrics:**
- Request rate (requests/second)
- Response time (p50, p95, p99)
- Error rate (5xx errors)
- Apdex score (user satisfaction metric)

**Infrastructure Metrics:**
- CPU utilization
- Memory usage
- Disk I/O
- Network throughput

**Business Metrics:**
- User engagement (drop-off points)
- Conversion rates
- Task completion rates

### Alerting

```yaml
# Example: Prometheus alert rules
groups:
  - name: performance
    rules:
      - alert: HighResponseTime
        expr: http_request_duration_seconds{quantile="0.95"} > 0.5
        for: 5m
        annotations:
          summary: "95th percentile response time > 500ms"

      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 2m
        annotations:
          summary: "Error rate > 5%"
```

---

## 🌱 When NOT to Optimize

### Premature Optimization

**Optimize when:**
✅ Performance budget exceeded
✅ Users complaining about slowness
✅ Metrics show issues
✅ Known bottleneck identified

**Don't optimize when:**
❌ "Might be slow in the future"
❌ No measurement or evidence
❌ Adds significant complexity
❌ Would delay shipping useful features

### Micro-optimizations

**Focus on:**
- Algorithm choice (O(n) vs O(n²))
- Network round trips (batching, caching)
- Database queries (indexes, N+1)
- Asset sizes (images, JavaScript)

**Ignore:**
- Variable naming overhead
- Function call overhead (unless inner loop)
- Minor syntactic differences

### Readability vs Performance

**Readability wins unless:**
- Profile shows this is a bottleneck
- Performance impact is significant (>10%)
- Optimization doesn't sacrifice too much clarity

```python
# Readable (prefer this)
def is_trusted(participant):
    return participant.trust_score >= THRESHOLD

# Micro-optimized (only if profiling shows it matters)
def is_trusted(participant):
    return participant.trust_score >= 0.3  # Inlined constant
```

---

## 💚 Sustainable Performance

### Energy Efficiency

**Code Efficiency = Environmental Impact:**
- Efficient algorithms use less CPU
- Less CPU = less energy
- Less energy = smaller carbon footprint

**Measure Energy:**
```bash
# Linux: perf to measure energy
sudo perf stat -e power/energy-pkg/ python your_script.py
```

**Sustainable Practices:**
- Optimize hot paths
- Cache aggressively
- Use CDNs (reduce data transfer)
- Compress assets
- Efficient data structures

### Carbon-Aware Computing

**Time operations for clean energy:**
- Batch jobs during high renewable availability
- Defer non-urgent work to off-peak hours
- Use green hosting providers

**Resources:**
- [Green Web Foundation](https://www.thegreenwebfoundation.org/)
- [Cloud Carbon Footprint](https://www.cloudcarbonfootprint.org/)

---

## 📚 Related Resources

- **[TESTING.md](./TESTING.md)** - Performance testing requirements
- **[ACCESSIBILITY.md](./ACCESSIBILITY.md)** - Performance as accessibility
- **[DESIGN.md](./DESIGN.md)** - Perceived performance in UX
- **[SUSTAINABILITY.md](./SUSTAINABILITY.md)** - Environmental impact

---

## 💬 Questions About Performance?

- **Performance issues**: #performance Discord channel
- **Optimization help**: Office hours (see [COMMUNICATION.md](./COMMUNICATION.md))
- **Suggest improvements**: Open PR on this document

---

**Last Updated**: 2025-01-14
**Maintained by**: Performance Working Group

---

> "Fast is kind. Efficient is responsible. Performant is sustainable. Optimize with consciousness, measure with care." 💚
