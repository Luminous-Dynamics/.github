# 🧪 Testing Standards

> "Tests are not a burden—they are freedom. Freedom to refactor, freedom to ship confidently, freedom to evolve without fear."

This guide defines testing philosophy, standards, and practices across all Luminous Dynamics projects.

---

## 🎯 Testing Philosophy

### Why We Test

**Not Because:**
- ❌ Coverage metrics look good
- ❌ It's a checkbox requirement
- ❌ Other projects do it

**Because:**
- ✅ **Confidence to Change** - Refactor fearlessly, knowing tests catch regressions
- ✅ **Living Documentation** - Tests show how code actually works
- ✅ **Design Feedback** - Hard-to-test code is often poorly designed
- ✅ **Faster Development** - Catch bugs in seconds, not days
- ✅ **User Care** - Bugs harm people; tests prevent harm

### Core Principles

1. **Tests Enable Evolution**
   - Without tests: fear of breaking things → stagnation
   - With tests: confidence to improve → continuous evolution

2. **Tests Document Behavior**
   - Test names explain what code does
   - Test examples show how to use APIs
   - Tests preserve intent when refactoring

3. **Tests Serve Humans**
   - Write tests that help future you
   - Clear failure messages save debugging time
   - Good tests make code reviews easier

4. **Practical Over Perfect**
   - Some tests > No tests
   - 80% coverage of critical paths > 100% coverage of everything
   - Fast, reliable tests > slow, flaky tests

5. **Test What Matters**
   - User-facing behavior > Implementation details
   - Critical paths heavily tested > Every edge case
   - Integration > Mocking everything

---

## 🏗️ Types of Tests

### Test Pyramid

```
          /\
         /  \        E2E Tests
        /----\       (Fewer, Slower, Integration-focused)
       /      \
      /--------\     Integration Tests
     /          \    (Medium number, Medium speed)
    /------------\
   /--------------\  Unit Tests
  /                \ (Many, Fast, Isolated)
 /------------------\
```

**Ideal Distribution:**
- **70% Unit Tests** - Fast, isolated, many of them
- **20% Integration Tests** - Test components working together
- **10% E2E Tests** - Full system, user perspective

**Anti-Pattern: Ice Cream Cone**
```
  /------------------\
 /                    \ E2E Tests (Slow, Brittle)
/----------------------\
\                      / Integration Tests (Medium)
 \                    /
  \                  /
   \                /    Unit Tests (Few)
    \--------------/
```
*Avoid: Too many slow E2E tests, too few fast unit tests*

### Unit Tests

**Purpose:** Test single function/method in isolation

**Characteristics:**
- Fast (milliseconds)
- No network, database, or file system
- Use mocks/stubs for dependencies
- Many tests (hundreds or thousands)

**Example:**
```python
def test_calculate_byzantine_resistance():
    """Test Byzantine resistance calculation with various inputs."""
    # Arrange
    participants = [
        Participant(trust_score=0.9),
        Participant(trust_score=0.8),
        Participant(trust_score=0.2),  # Malicious
    ]

    # Act
    resistance = calculate_byzantine_resistance(
        participants,
        threshold=0.5
    )

    # Assert
    assert resistance == 0.67  # (0.9 + 0.8) / (0.9 + 0.8 + 0.2)


def test_byzantine_resistance_empty_participants():
    """Should raise error for empty participant list."""
    with pytest.raises(ValueError, match="at least one participant"):
        calculate_byzantine_resistance([], threshold=0.5)
```

**When to Use:**
- Pure functions (input → output, no side effects)
- Business logic and algorithms
- Validation and formatting
- Utility functions

### Integration Tests

**Purpose:** Test components working together

**Characteristics:**
- Medium speed (seconds)
- Real database/APIs (test instances)
- Test interactions between components
- Fewer than unit tests, more than E2E

**Example:**
```python
def test_federation_stores_and_retrieves_data(test_db):
    """Test federation data persists correctly."""
    # Arrange
    federation = Federation(name="test-fed", db=test_db)
    data = FederationData(participants=100, model_hash="abc123")

    # Act
    federation.save(data)
    retrieved = federation.load("test-fed")

    # Assert
    assert retrieved.participants == 100
    assert retrieved.model_hash == "abc123"


def test_mycelix_detects_byzantine_participant(test_network):
    """Test Byzantine detection in real network."""
    # Arrange
    network = test_network(participants=10)
    byzantine_node = network.nodes[5]
    byzantine_node.behave_maliciously = True

    # Act
    result = network.run_training(epochs=3)

    # Assert
    assert byzantine_node.id in result.excluded_nodes
    assert result.byzantine_detected == 1
```

**When to Use:**
- Database interactions
- API endpoint testing
- Service integration
- Message queue processing

### End-to-End (E2E) Tests

**Purpose:** Test complete user workflows

**Characteristics:**
- Slow (seconds to minutes)
- Real browser, real services
- Tests critical user journeys
- Fewest tests (10-50 typically)

**Example:**
```python
def test_user_creates_and_runs_federation(browser):
    """Test complete federation creation workflow."""
    # Navigate to Terra Atlas
    browser.goto("https://atlas.luminous-dynamics.io")

    # Create new federation
    browser.click("#create-federation")
    browser.fill("#federation-name", "Climate Research")
    browser.select("#privacy-mode", "local-only")
    browser.click("#submit")

    # Verify federation created
    assert browser.text_content("h1") == "Climate Research"
    assert "Federation active" in browser.text_content(".status")

    # Add participant
    browser.click("#add-participant")
    browser.fill("#participant-id", "node-001")
    browser.click("#confirm")

    # Start training
    browser.click("#start-training")
    browser.wait_for_selector(".training-progress")

    # Verify training started
    assert "Training in progress" in browser.text_content(".status")
```

**When to Use:**
- Critical user workflows (signup, purchase, core features)
- Cross-browser compatibility
- Visual regression testing
- User acceptance criteria

### Property-Based Tests

**Purpose:** Test properties that should always hold

**Characteristics:**
- Generates many random inputs
- Tests invariants and properties
- Catches edge cases humans miss

**Example:**
```python
from hypothesis import given, strategies as st

@given(
    trust_scores=st.lists(
        st.floats(min_value=0.0, max_value=1.0),
        min_size=1,
        max_size=1000
    )
)
def test_byzantine_resistance_always_between_0_and_1(trust_scores):
    """Byzantine resistance should always be in [0, 1] range."""
    participants = [Participant(trust_score=s) for s in trust_scores]
    resistance = calculate_byzantine_resistance(participants, threshold=0.3)

    assert 0.0 <= resistance <= 1.0


@given(
    participants=st.lists(st.integers(min_value=1, max_value=10000)),
    threshold=st.floats(min_value=0.0, max_value=1.0)
)
def test_adding_trusted_participant_increases_resistance(participants, threshold):
    """Adding a highly trusted participant should increase resistance."""
    initial = calculate_byzantine_resistance(participants, threshold)

    # Add highly trusted participant
    participants.append(Participant(trust_score=1.0))
    final = calculate_byzantine_resistance(participants, threshold)

    assert final >= initial
```

**When to Use:**
- Complex algorithms
- Parsers and serializers
- Mathematical properties
- Data structure invariants

---

## 📏 Coverage Standards

### Minimum Coverage by Project

| Project | Minimum Coverage | Critical Path Coverage |
|---------|-----------------|------------------------|
| Mycelix Core | 85% | 95% |
| Terra Atlas (Backend) | 80% | 90% |
| Terra Atlas (Frontend) | 70% | 85% |
| Luminos/Simulacra | 80% | 90% |
| CLI Tools | 75% | 85% |
| Documentation | N/A | Manual review |

**Critical Paths:** Core features users depend on (Byzantine detection, energy calculations, auth, payments)

### Coverage != Quality

✅ **Good (80% coverage):**
```python
# Tests cover critical authentication flow thoroughly
def test_user_authentication_with_valid_credentials():
    # 20 lines testing happy path, edge cases, security

def test_user_authentication_with_invalid_credentials():
    # 15 lines testing various failure modes

def test_user_authentication_prevents_timing_attacks():
    # 10 lines testing security property
```

❌ **Bad (80% coverage):**
```python
# Tests just execute code without assertions
def test_user_authentication():
    result = authenticate("user", "pass")
    # No assertions! Just hits the code.
```

**Measure:**
- Coverage (quantitative)
- Test quality (code review)
- Mutation testing (do tests catch bugs?)

---

## ✅ Test Quality Standards

### Good Test Characteristics

**1. Clear Names**

❌ **Bad:**
```python
def test_1():
def test_edge_case():
def test_function():
```

✅ **Good:**
```python
def test_byzantine_resistance_excludes_participants_below_threshold():
def test_federation_raises_error_when_name_is_empty():
def test_api_returns_401_for_invalid_api_key():
```

**Format:** `test_[what]_[condition]_[expected_result]`

**2. Arrange-Act-Assert (AAA)**

```python
def test_trust_score_calculation():
    # Arrange - Set up test data
    participant = Participant(
        successful_validations=90,
        total_validations=100
    )

    # Act - Execute the code being tested
    score = participant.calculate_trust_score()

    # Assert - Verify expected outcome
    assert score == 0.9
```

**3. Isolated (FIRST Principles)**

- **F**ast - Run in milliseconds
- **I**solated - No dependencies between tests
- **R**epeatable - Same result every time
- **S**elf-validating - Pass/fail, no manual inspection
- **T**imely - Written with (or before) production code

**4. Single Responsibility**

❌ **Bad - Tests Multiple Things:**
```python
def test_federation_lifecycle():
    # Tests creation, data storage, participant management,
    # training, and cleanup all in one test
    # (150 lines of test code)
```

✅ **Good - Focused Tests:**
```python
def test_federation_creation_with_valid_params():
    # 10 lines testing just creation

def test_federation_stores_data_correctly():
    # 10 lines testing just persistence

def test_federation_manages_participants():
    # 15 lines testing just participant management
```

**5. Descriptive Failures**

❌ **Bad Failure Message:**
```python
assert result == expected  # AssertionError (What failed? Why?)
```

✅ **Good Failure Message:**
```python
assert result == expected, (
    f"Byzantine resistance calculation incorrect. "
    f"Expected {expected} for {len(participants)} participants "
    f"with threshold {threshold}, but got {result}"
)
```

**Even Better - Use Testing Library Features:**
```python
# Pytest shows detailed diff automatically
assert result == expected

# Custom assertions for clarity
assert_byzantine_resistance(
    participants=participants,
    threshold=0.3,
    expected=0.67,
    tolerance=0.01
)
```

### Test Anti-Patterns

❌ **Flaky Tests (Non-Deterministic)**
```python
def test_response_time():
    start = time.time()
    result = api_call()
    duration = time.time() - start
    assert duration < 0.1  # Fails randomly based on system load
```

✅ **Better:**
```python
def test_response_time():
    with mock.patch('time.time', side_effect=[0, 0.05]):
        # Deterministic timing
        assert check_performance_threshold(api_call) is True
```

---

❌ **Testing Implementation, Not Behavior**
```python
def test_uses_redis_cache():
    user_service.get_user(123)
    assert redis_client.get.called  # Breaks if we change caching strategy
```

✅ **Better:**
```python
def test_repeated_requests_are_fast():
    # Test the behavior (speed) not implementation (Redis)
    first_call = timed(lambda: user_service.get_user(123))
    second_call = timed(lambda: user_service.get_user(123))
    assert second_call < first_call * 0.1  # 10x faster = cached
```

---

❌ **Excessive Mocking**
```python
def test_federation_training():
    mock_db = Mock()
    mock_network = Mock()
    mock_trust_layer = Mock()
    mock_logger = Mock()
    mock_metrics = Mock()
    # ... now testing mocks, not real code
```

✅ **Better:**
```python
def test_federation_training(test_db, test_network):
    # Use real components when practical
    # Only mock external services (APIs, slow operations)
    with mock.patch('external_api.report_metrics'):
        federation = Federation(db=test_db, network=test_network)
        result = federation.train(model, epochs=3)
        assert result.accuracy > 0.9
```

---

❌ **Tests Depending on Each Other**
```python
class TestFederation:
    def test_1_create(self):
        self.fed = Federation("test")

    def test_2_add_participants(self):
        self.fed.add_participant("node-1")  # Fails if test_1 didn't run

    def test_3_train(self):
        self.fed.train()  # Depends on test_1 AND test_2
```

✅ **Better:**
```python
class TestFederation:
    def test_create(self):
        fed = Federation("test")
        assert fed.name == "test"

    def test_add_participants(self):
        fed = Federation("test")  # Each test independent
        fed.add_participant("node-1")
        assert len(fed.participants) == 1

    def test_train(self):
        fed = create_test_federation_with_participants()  # Helper function
        result = fed.train()
        assert result.success
```

---

## 🛠️ Testing Tools and Frameworks

### By Language

**Python:**
- **pytest** - Primary testing framework
- **hypothesis** - Property-based testing
- **pytest-cov** - Coverage reporting
- **pytest-xdist** - Parallel test execution
- **faker** - Test data generation

**JavaScript/TypeScript:**
- **Jest** - Unit and integration tests
- **Playwright** - E2E browser testing
- **React Testing Library** - Component testing
- **Supertest** - API endpoint testing

**Rust:**
- **cargo test** - Built-in test runner
- **proptest** - Property-based testing
- **criterion** - Benchmarking

### CI/CD Integration

**GitHub Actions Example:**
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt

      - name: Run linters
        run: |
          ruff check .
          mypy .

      - name: Run tests with coverage
        run: |
          pytest --cov=src --cov-report=xml --cov-report=term

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          fail_ci_if_error: true

      - name: Check coverage threshold
        run: |
          coverage report --fail-under=80
```

---

## 🎯 Test-Driven Development (TDD)

### Red-Green-Refactor Cycle

1. **Red** - Write failing test
2. **Green** - Write minimum code to pass
3. **Refactor** - Improve code without changing behavior

**Example:**

**1. Red - Write Failing Test:**
```python
def test_calculate_byzantine_resistance_with_mixed_participants():
    """Test resistance calculation with trusted and untrusted participants."""
    participants = [
        Participant(trust_score=0.9),  # Trusted
        Participant(trust_score=0.8),  # Trusted
        Participant(trust_score=0.2),  # Untrusted
    ]

    resistance = calculate_byzantine_resistance(
        participants,
        threshold=0.5
    )

    assert resistance == 0.567  # (0.9 + 0.8) / (0.9 + 0.8 + 0.2)

# Run: FAILS - function doesn't exist yet
```

**2. Green - Minimum Implementation:**
```python
def calculate_byzantine_resistance(participants, threshold):
    """Calculate Byzantine resistance score."""
    total_trust = sum(p.trust_score for p in participants)
    trusted_trust = sum(
        p.trust_score
        for p in participants
        if p.trust_score >= threshold
    )
    return trusted_trust / total_trust if total_trust > 0 else 0

# Run: PASSES
```

**3. Refactor - Improve Code:**
```python
def calculate_byzantine_resistance(
    participants: List[Participant],
    threshold: float
) -> float:
    """
    Calculate Byzantine resistance score.

    The resistance score represents the fraction of trust held by
    participants meeting the trust threshold.

    Args:
        participants: List of network participants
        threshold: Minimum trust score to be considered trusted (0-1)

    Returns:
        Resistance score between 0 and 1

    Raises:
        ValueError: If participants is empty or threshold out of range
    """
    if not participants:
        raise ValueError("Must have at least one participant")
    if not 0 <= threshold <= 1:
        raise ValueError(f"Threshold must be in [0,1], got {threshold}")

    total_trust = sum(p.trust_score for p in participants)
    trusted_trust = sum(
        p.trust_score
        for p in participants
        if p.trust_score >= threshold
    )

    return trusted_trust / total_trust

# Run: Still PASSES, but code is better
```

### Benefits of TDD

✅ **Better Design:**
- Forces you to think about API before implementation
- Results in more testable (and therefore better) code

✅ **Confidence:**
- Know exactly when you're done (tests pass)
- Regression safety built in from start

✅ **Documentation:**
- Tests document expected behavior
- Examples show how to use the code

### When Not to TDD

- Exploratory spike work (figure out approach first)
- UI/visual work (faster to iterate visually)
- Research code (throw-away prototypes)

**After exploration, add tests before committing!**

---

## 🔐 Security Testing

### What to Test

1. **Authentication & Authorization**
   ```python
   def test_api_requires_authentication():
       response = client.get("/api/federations")
       assert response.status_code == 401

   def test_user_cannot_access_others_federations():
       user1_token = create_token(user_id=1)
       federation2 = create_federation(owner_id=2)

       response = client.get(
           f"/api/federations/{federation2.id}",
           headers={"Authorization": f"Bearer {user1_token}"}
       )
       assert response.status_code == 403
   ```

2. **Input Validation**
   ```python
   def test_api_rejects_sql_injection_attempts():
       malicious_input = "'; DROP TABLE users; --"
       response = client.post(
           "/api/search",
           json={"query": malicious_input}
       )
       assert response.status_code == 400
       assert "Invalid input" in response.json()["error"]

   def test_api_rejects_xss_attempts():
       xss_payload = "<script>alert('xss')</script>"
       response = client.post(
           "/api/federation/create",
           json={"name": xss_payload}
       )
       # Either rejected or sanitized
       assert response.status_code in [400, 201]
       if response.status_code == 201:
           assert "<script>" not in response.json()["name"]
   ```

3. **Rate Limiting**
   ```python
   def test_api_rate_limits_prevent_brute_force():
       for i in range(100):
           response = client.post(
               "/api/login",
               json={"username": "test", "password": f"wrong{i}"}
           )

       # Should be rate limited after N attempts
       assert response.status_code == 429
       assert "Too many requests" in response.json()["error"]
   ```

4. **Data Privacy**
   ```python
   def test_api_does_not_leak_user_data():
       user = create_user(email="private@example.com", ssn="123-45-6789")

       response = client.get(f"/api/users/{user.id}")
       data = response.json()

       # Should not include sensitive fields
       assert "ssn" not in data
       assert "password_hash" not in data
       # Email may be included for owner, but masked for others
   ```

---

## ⚡ Performance Testing

### Load Testing

```python
def test_api_handles_concurrent_requests():
    """Test API can handle 100 concurrent requests."""
    import concurrent.futures

    def make_request():
        return client.get("/api/federations")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(make_request) for _ in range(100)]
        results = [f.result() for f in futures]

    # All should succeed
    assert all(r.status_code == 200 for r in results)

    # Response times should be reasonable
    response_times = [r.elapsed.total_seconds() for r in results]
    assert max(response_times) < 1.0  # Max 1 second
    assert sum(response_times) / len(response_times) < 0.1  # Avg < 100ms
```

### Benchmarking

```python
import pytest

@pytest.mark.benchmark
def test_byzantine_detection_performance(benchmark):
    """Benchmark Byzantine detection for 1000 participants."""
    participants = [
        create_participant() for _ in range(1000)
    ]

    result = benchmark(
        calculate_byzantine_resistance,
        participants,
        threshold=0.3
    )

    # Should complete in < 1ms as per requirements
    assert benchmark.stats.mean < 0.001
```

---

## 📚 Project-Specific Testing

### Mycelix Protocol

**Critical Properties to Test:**
- Byzantine resistance: 100% detection when < 30% malicious
- Privacy: No data leakage between participants
- Performance: < 1ms latency for trust calculations
- Consistency: Eventual consistency across distributed network

### Terra Atlas

**Critical Features to Test:**
- Energy data accuracy (calculations correct)
- Real-time updates (WebSocket reliability)
- Accessibility (WCAG 2.1 AA compliance - use axe)
- Mobile responsiveness

### CLI Tools

**User Experience Tests:**
- Help text is clear and complete
- Error messages are helpful
- Progress indicators work
- Exit codes are correct

---

## 💚 Testing as Consciousness Practice

### Tests Serve Users

Every test prevents a bug from reaching users:
- Bugs cause frustration, lost time, lost data
- Tests are acts of care for future users
- Good tests honor the trust users place in us

### Tests Enable Evolution

Consciousness-first technology must evolve with understanding:
- Tests give confidence to improve
- Refactoring without tests = fear of breaking things
- Fear of breaking things = stagnation

### Tests as Teaching

Tests document how code should work:
- New contributors learn from tests
- Tests show intended behavior
- Good tests make onboarding easier

---

## 📚 Related Resources

- **[CODE_REVIEW.md](./CODE_REVIEW.md)** - Code review practices
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - How to contribute
- **[STYLE_GUIDE.md](./STYLE_GUIDE.md)** - Documentation standards
- **[RELEASES.md](./RELEASES.md)** - Release process (includes testing checklists)

---

## 💬 Questions?

- **Discuss testing practices**: [GitHub Discussions](https://github.com/orgs/Luminous-Dynamics/discussions)
- **Get help with testing**: Discord #dev channel
- **Suggest improvements**: Open PR on this document

---

**Last Updated**: 2025-01-14
**Maintained by**: Engineering Working Group

---

> "Tests are love letters to our future selves and to all who will use and maintain this code. Write them with care, clarity, and consciousness." 💚
