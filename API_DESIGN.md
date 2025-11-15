# 🔌 API Design

> "A well-designed API is a joy to use. A poorly designed API is a constant source of frustration."

*Last updated: January 2025*

This document outlines our **API design principles and standards** for creating intuitive, consistent, and developer-friendly APIs across all Luminous Dynamics projects.

---

## 🎯 API Design Philosophy

### What Makes a Great API?

**Great APIs are**:
- **Intuitive**: Developers can guess how it works
- **Consistent**: Similar things work similarly
- **Well-documented**: Clear examples and explanations
- **Forgiving**: Helpful error messages guide users
- **Stable**: Breaking changes are rare and well-communicated
- **Performant**: Fast enough for real-world use

**Our goal**: APIs that developers **enjoy using** and **recommend to others**.

### Design Principles

1. **Developer-centric**: Design for the developer using your API, not for implementation convenience
2. **Consistency over cleverness**: Predictable patterns beat clever tricks
3. **Explicit over implicit**: Clear is better than magical
4. **Progressive disclosure**: Simple things simple, complex things possible
5. **Fail loudly and clearly**: Errors should teach, not confuse
6. **Backward compatibility**: Don't break existing users without very good reason
7. **Security by default**: Safe defaults, opt-in for dangerous operations
8. **Performance-aware**: Design with performance in mind from the start

---

## 🏗️ REST API Design

### Resource-Oriented Design

**REST APIs organize around resources** (nouns), not actions (verbs).

**Good resource names**:
```
GET    /users              # Collection of users
GET    /users/123          # Specific user
GET    /users/123/posts    # User's posts
POST   /users              # Create new user
PUT    /users/123          # Update user (full replace)
PATCH  /users/123          # Update user (partial)
DELETE /users/123          # Delete user
```

**Avoid RPC-style endpoints in REST**:
```
❌ POST /createUser
❌ GET  /getUserById?id=123
❌ POST /users/123/activate

✅ POST   /users
✅ GET    /users/123
✅ PATCH  /users/123/status  (with {"status": "active"})
```

### HTTP Methods

**Use HTTP methods semantically**:

| Method | Purpose | Idempotent? | Safe? |
|--------|---------|-------------|-------|
| GET | Retrieve resource(s) | Yes | Yes |
| POST | Create resource | No | No |
| PUT | Replace resource (full) | Yes | No |
| PATCH | Update resource (partial) | No* | No |
| DELETE | Remove resource | Yes | No |
| HEAD | Get headers only | Yes | Yes |
| OPTIONS | Get allowed methods | Yes | Yes |

*PATCH can be idempotent if designed carefully

**Examples**:
```http
# Retrieve all users
GET /api/v1/users

# Retrieve specific user
GET /api/v1/users/42

# Create new user
POST /api/v1/users
Content-Type: application/json

{
  "email": "alice@example.com",
  "name": "Alice"
}

# Update user (replace entirely)
PUT /api/v1/users/42
Content-Type: application/json

{
  "email": "alice@example.com",
  "name": "Alice Smith",
  "role": "admin"
}

# Update user (partially)
PATCH /api/v1/users/42
Content-Type: application/json

{
  "name": "Alice Smith"
}

# Delete user
DELETE /api/v1/users/42
```

### URL Design

**Consistent, readable, hierarchical URLs**:

**Good URLs**:
```
/api/v1/users
/api/v1/users/123
/api/v1/users/123/posts
/api/v1/users/123/posts/456
/api/v1/organizations/acme/projects
```

**URL Guidelines**:
- ✅ Use **plural nouns** for collections: `/users`, not `/user`
- ✅ Use **lowercase**: `/users`, not `/Users`
- ✅ Use **hyphens** for multi-word resources: `/user-profiles`
- ✅ Use **hierarchy** to show relationships: `/users/123/posts`
- ❌ Don't use **verbs**: `/getUsers`, `/createPost`
- ❌ Don't use **file extensions**: `/users.json`
- ❌ Don't use **trailing slashes**: `/users/`, just `/users`

### Query Parameters

**Use query parameters for filtering, sorting, pagination**:

```http
# Filtering
GET /api/v1/users?role=admin&status=active

# Sorting
GET /api/v1/users?sort=name&order=asc

# Pagination
GET /api/v1/users?page=2&limit=50

# Searching
GET /api/v1/users?q=alice

# Multiple parameters
GET /api/v1/users?role=admin&sort=created_at&order=desc&limit=20
```

**Guidelines**:
- Use descriptive parameter names: `limit` not `l`
- Support common filters for each resource type
- Document all supported parameters
- Validate and sanitize all inputs

### Status Codes

**Use HTTP status codes correctly**:

**Success codes**:
- **200 OK**: Successful GET, PATCH, PUT, DELETE
- **201 Created**: Successful POST creating a resource
- **202 Accepted**: Request accepted for async processing
- **204 No Content**: Successful DELETE, no response body needed

**Client error codes**:
- **400 Bad Request**: Invalid syntax, malformed request
- **401 Unauthorized**: Authentication required or failed
- **403 Forbidden**: Authenticated but not authorized
- **404 Not Found**: Resource doesn't exist
- **405 Method Not Allowed**: HTTP method not supported for endpoint
- **409 Conflict**: Request conflicts with current state (e.g., duplicate)
- **422 Unprocessable Entity**: Valid syntax but semantic errors (validation)
- **429 Too Many Requests**: Rate limit exceeded

**Server error codes**:
- **500 Internal Server Error**: Unexpected server error
- **502 Bad Gateway**: Invalid response from upstream
- **503 Service Unavailable**: Temporarily down (maintenance, overload)
- **504 Gateway Timeout**: Upstream timeout

**Example**:
```http
# Success
POST /api/v1/users
201 Created
Location: /api/v1/users/123
Content-Type: application/json

{
  "id": 123,
  "email": "alice@example.com",
  "name": "Alice",
  "created_at": "2025-01-15T10:30:00Z"
}

# Validation error
POST /api/v1/users
422 Unprocessable Entity
Content-Type: application/json

{
  "error": "Validation failed",
  "details": [
    {
      "field": "email",
      "message": "Email address is required"
    },
    {
      "field": "name",
      "message": "Name must be at least 2 characters"
    }
  ]
}
```

### Request/Response Format

**Use JSON as default format**:

**Request**:
```http
POST /api/v1/users
Content-Type: application/json

{
  "email": "alice@example.com",
  "name": "Alice",
  "role": "member"
}
```

**Response**:
```http
201 Created
Content-Type: application/json
Location: /api/v1/users/123

{
  "id": 123,
  "email": "alice@example.com",
  "name": "Alice",
  "role": "member",
  "status": "active",
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:30:00Z",
  "links": {
    "self": "/api/v1/users/123",
    "posts": "/api/v1/users/123/posts"
  }
}
```

**Response guidelines**:
- Use **camelCase** or **snake_case** consistently (we prefer snake_case)
- Include **timestamps** in ISO 8601 format with timezone
- Include **links** to related resources (HATEOAS principle)
- Include **metadata** in responses (pagination info, etc.)
- Return created/updated resource in response body

### Pagination

**Implement pagination for collections**:

**Offset-based pagination** (simple, good for small datasets):
```http
GET /api/v1/users?limit=20&offset=40

Response:
{
  "data": [ /* 20 users */ ],
  "pagination": {
    "limit": 20,
    "offset": 40,
    "total": 1234,
    "has_next": true,
    "has_prev": true
  }
}
```

**Cursor-based pagination** (better for large datasets, stable order):
```http
GET /api/v1/users?limit=20&cursor=eyJpZCI6MTIzfQ

Response:
{
  "data": [ /* 20 users */ ],
  "pagination": {
    "limit": 20,
    "next_cursor": "eyJpZCI6MTQzfQ",
    "prev_cursor": "eyJpZCI6MTAzfQ",
    "has_next": true,
    "has_prev": true
  }
}
```

**Page-based pagination** (familiar to users):
```http
GET /api/v1/users?page=3&per_page=20

Response:
{
  "data": [ /* 20 users */ ],
  "pagination": {
    "page": 3,
    "per_page": 20,
    "total_pages": 62,
    "total_items": 1234
  }
}
```

**Choose based on your use case**:
- **Offset**: Simple, works for most cases, but can skip/duplicate if data changes
- **Cursor**: Best for feeds/timelines, stable even with insertions
- **Page**: Most familiar to users, good for UIs with page numbers

### Filtering and Searching

**Support filtering and searching**:

**Simple filters**:
```http
GET /api/v1/users?role=admin&status=active
```

**Range filters**:
```http
GET /api/v1/posts?created_after=2025-01-01&created_before=2025-12-31
```

**Full-text search**:
```http
GET /api/v1/users?q=alice
```

**Advanced filters** (query language):
```http
GET /api/v1/users?filter=role:admin AND status:active
```

**Guidelines**:
- Support common filters for each resource
- Document all filter options
- Validate filter values
- Return 400 for invalid filters with clear error

### Sorting

**Allow sorting by various fields**:

```http
# Single field
GET /api/v1/users?sort=name

# Descending order
GET /api/v1/users?sort=-created_at

# Multiple fields
GET /api/v1/users?sort=role,-created_at
```

**Guidelines**:
- Use `-` prefix for descending order
- Support sorting by common fields
- Default sort order should be stable and documented
- Return 400 for invalid sort fields

---

## 🔐 Authentication & Authorization

### Authentication Methods

**API Key** (simple, for server-to-server):
```http
GET /api/v1/users
X-API-Key: sk_live_1234567890abcdef
```

**Bearer Token / JWT** (common for user APIs):
```http
GET /api/v1/users
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**OAuth 2.0** (for third-party access):
```http
GET /api/v1/users
Authorization: Bearer ya29.a0AfH6SMC...
```

**Choose based on use case**:
- **API keys**: Server-to-server, long-lived credentials
- **JWT**: User sessions, short-lived tokens
- **OAuth**: Third-party applications accessing user data

### Authorization

**Return appropriate status codes**:

```http
# Not authenticated
GET /api/v1/users
401 Unauthorized

{
  "error": "Authentication required",
  "message": "Please provide a valid API key or access token"
}

# Authenticated but not authorized
GET /api/v1/admin/users
403 Forbidden

{
  "error": "Insufficient permissions",
  "message": "Admin role required to access this resource"
}
```

### Security Best Practices

- **Always use HTTPS** in production
- **Never pass credentials** in URL query parameters
- **Rate limit** all endpoints (see below)
- **Validate all inputs** to prevent injection
- **Sanitize outputs** to prevent XSS
- **Use CORS** headers appropriately
- **Log authentication failures** for security monitoring

---

## ⚡ Rate Limiting

**Prevent abuse and ensure fair usage**:

**Return rate limit headers**:
```http
GET /api/v1/users
200 OK
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1642435200

{
  "data": [ /* users */ ]
}
```

**When rate limit exceeded**:
```http
GET /api/v1/users
429 Too Many Requests
Retry-After: 60
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1642435200

{
  "error": "Rate limit exceeded",
  "message": "Too many requests. Please retry after 60 seconds.",
  "retry_after": 60
}
```

**Rate limiting strategies**:
- **Fixed window**: X requests per hour (simple but can burst)
- **Sliding window**: More sophisticated, smoother
- **Token bucket**: Allows bursts but rate-limited over time

**Tier-based limits**:
```
Free tier:     100 requests/hour
Pro tier:     1000 requests/hour
Enterprise:  10000 requests/hour
```

---

## 🎨 Error Handling

**Consistent, helpful error responses**:

**Error response format**:
```json
{
  "error": "Short error code/type",
  "message": "Human-readable error message",
  "details": [ /* Optional: specific field errors */ ],
  "request_id": "req_1234567890",
  "timestamp": "2025-01-15T10:30:00Z",
  "documentation_url": "https://docs.example.com/errors/validation-failed"
}
```

**Examples**:

**Validation errors**:
```http
POST /api/v1/users
422 Unprocessable Entity

{
  "error": "validation_failed",
  "message": "Request validation failed",
  "details": [
    {
      "field": "email",
      "code": "required",
      "message": "Email address is required"
    },
    {
      "field": "password",
      "code": "too_short",
      "message": "Password must be at least 8 characters",
      "params": { "min_length": 8 }
    }
  ],
  "request_id": "req_1234567890"
}
```

**Resource not found**:
```http
GET /api/v1/users/999
404 Not Found

{
  "error": "not_found",
  "message": "User with ID 999 not found",
  "request_id": "req_1234567890"
}
```

**Server error**:
```http
GET /api/v1/users
500 Internal Server Error

{
  "error": "internal_server_error",
  "message": "An unexpected error occurred. Please try again later.",
  "request_id": "req_1234567890",
  "support_email": "support@example.com"
}
```

**Error handling principles**:
- **Be specific**: Say what went wrong
- **Be helpful**: Suggest how to fix it
- **Be consistent**: Same format for all errors
- **Don't leak internals**: No stack traces to users
- **Include request ID**: For support/debugging
- **Link to docs**: Help users help themselves

---

## 📚 Versioning

**APIs evolve—version them to avoid breaking users.**

### URL Versioning (Recommended)

```http
GET /api/v1/users     # Version 1
GET /api/v2/users     # Version 2
```

**Pros**:
- Simple and visible
- Easy to route different versions
- Clear in logs and URLs

**Cons**:
- URLs change between versions
- Can lead to URL proliferation

### Header Versioning

```http
GET /api/users
Accept: application/vnd.example.v1+json
```

**Pros**:
- URLs stay the same
- More RESTful

**Cons**:
- Less visible (hidden in headers)
- Harder to test in browser

### Our Recommendation

**Use URL versioning** (`/api/v1/...`) because:
- Simplicity and clarity
- Easy to test
- Clear in documentation
- Standard practice

### Versioning Strategy

**When to bump version**:
- **Major version** (v1 → v2): Breaking changes
  - Removing endpoints
  - Changing required fields
  - Changing response structure
  - Changing authentication
- **Minor version** (can be implicit): Non-breaking changes
  - Adding new endpoints
  - Adding optional parameters
  - Adding fields to responses

**Maintain old versions**:
- Support previous major version for **at least 12 months**
- Announce deprecation **6 months in advance**
- Provide **migration guide**
- Consider **dual-write** during transition

**Example migration**:
```markdown
## v1 Deprecation Notice

**Timeline**:
- 2025-01-15: v2 released
- 2025-07-15: v1 deprecated (still works, warnings added)
- 2026-01-15: v1 sunset (removed)

**What's changing**:
- User emails are now unique (v1 allowed duplicates)
- `POST /users` now returns 409 if email exists

**Migration guide**: https://docs.example.com/migration/v1-to-v2
```

---

## 📖 API Documentation

**Great APIs have great documentation.**

### What to Document

**Overview**:
- What does this API do?
- Who is it for?
- How do I get started?
- Where do I get help?

**Authentication**:
- How do I authenticate?
- How do I get API keys/tokens?
- Example authentication request

**Endpoints**:
For each endpoint:
- HTTP method and URL
- Description of what it does
- Authentication required?
- Request parameters (path, query, body)
- Request examples (curl, code samples)
- Response format
- Response examples (success, errors)
- Status codes
- Rate limits

**Errors**:
- Error response format
- Common error codes
- How to handle errors

**Rate Limiting**:
- Limits for each tier
- How to check remaining quota
- What to do when limited

**Changelog**:
- What changed in each version
- Migration guides

### Documentation Tools

**OpenAPI/Swagger**:
```yaml
openapi: 3.0.0
info:
  title: Luminous Dynamics API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List all users
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
```

**Generate docs from OpenAPI**:
- Swagger UI
- ReDoc
- Stoplight

**Interactive docs**:
- Allow trying API calls from docs
- Pre-filled examples
- Real API responses

---

## 🧪 Testing APIs

### What to Test

**Unit tests**:
- Validation logic
- Business logic
- Error handling

**Integration tests**:
- Endpoint behavior
- Database interactions
- Authentication/authorization

**Contract tests**:
- API matches documented contract
- Request/response schemas
- Status codes

**Performance tests**:
- Response times under load
- Rate limiting behavior
- Database query optimization

### Testing Tools

**REST API testing**:
- Postman/Insomnia collections
- HTTP clients (curl, httpie)
- Testing frameworks (Jest, pytest, etc.)

**Example test**:
```javascript
describe('POST /api/v1/users', () => {
  it('creates a new user', async () => {
    const response = await api.post('/api/v1/users', {
      email: 'alice@example.com',
      name: 'Alice'
    });

    expect(response.status).toBe(201);
    expect(response.data).toMatchObject({
      email: 'alice@example.com',
      name: 'Alice',
      status: 'active'
    });
    expect(response.data.id).toBeDefined();
  });

  it('returns 422 for invalid email', async () => {
    const response = await api.post('/api/v1/users', {
      email: 'not-an-email',
      name: 'Alice'
    });

    expect(response.status).toBe(422);
    expect(response.data.error).toBe('validation_failed');
  });
});
```

---

## 🚀 GraphQL APIs

**Alternative to REST for complex data requirements.**

### When to Use GraphQL

**Use GraphQL when**:
- Clients need flexible data fetching
- Multiple related resources in single request
- Over-fetching/under-fetching is a problem with REST
- Strong typing is valuable

**Stick with REST when**:
- Simple CRUD operations
- Caching is important (HTTP caching)
- Team unfamiliar with GraphQL
- File uploads (REST is simpler)

### GraphQL Best Practices

**Schema design**:
```graphql
type User {
  id: ID!
  email: String!
  name: String!
  posts: [Post!]!
  createdAt: DateTime!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  createdAt: DateTime!
}

type Query {
  user(id: ID!): User
  users(limit: Int, offset: Int): [User!]!
  post(id: ID!): Post
}

type Mutation {
  createUser(email: String!, name: String!): User!
  updateUser(id: ID!, name: String): User!
  deleteUser(id: ID!): Boolean!
}
```

**Error handling**:
```graphql
# Query
query {
  user(id: "999") {
    id
    name
  }
}

# Response
{
  "data": {
    "user": null
  },
  "errors": [
    {
      "message": "User not found",
      "path": ["user"],
      "extensions": {
        "code": "NOT_FOUND",
        "id": "999"
      }
    }
  ]
}
```

**Pagination**:
```graphql
type Query {
  users(first: Int, after: String): UserConnection!
}

type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
}

type UserEdge {
  node: User!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}
```

---

## 📊 API Metrics

**Measure API health and usage**:

### Key Metrics

**Performance**:
- **Response time**: p50, p95, p99
- **Throughput**: Requests per second
- **Error rate**: % of requests returning 5xx

**Usage**:
- **Active API keys**: Number of users
- **Endpoints**: Most/least used
- **Versions**: Usage by version

**Quality**:
- **4xx rate**: Client errors (may indicate poor UX)
- **5xx rate**: Server errors (reliability issue)
- **Rate limit hits**: Are limits appropriate?

**Business**:
- **Tier distribution**: Free vs paid usage
- **Retention**: Are developers staying?
- **Time to first call**: Onboarding effectiveness

### Monitoring Tools

- **Application monitoring**: New Relic, Datadog, AppDynamics
- **Logs**: ELK stack, Splunk, CloudWatch
- **Metrics**: Prometheus, Grafana
- **Tracing**: Jaeger, Zipkin
- **Uptime**: Pingdom, UptimeRobot

---

## 🌟 API Design Checklist

Use this to review API design:

### Resource Design
- [ ] Resources are nouns, not verbs
- [ ] Plural names for collections
- [ ] Hierarchy reflects relationships
- [ ] Consistent naming conventions

### HTTP Methods
- [ ] GET for retrieval (safe, idempotent)
- [ ] POST for creation
- [ ] PUT/PATCH for updates
- [ ] DELETE for removal
- [ ] Correct idempotency

### URLs
- [ ] Lowercase, hyphen-separated
- [ ] Logical hierarchy
- [ ] No file extensions
- [ ] No trailing slashes

### Request/Response
- [ ] JSON by default
- [ ] Consistent field naming (snake_case or camelCase)
- [ ] Timestamps in ISO 8601
- [ ] Links to related resources
- [ ] Appropriate status codes

### Pagination
- [ ] Implemented for collections
- [ ] Consistent pagination format
- [ ] Metadata included (total, pages, etc.)

### Filtering/Sorting
- [ ] Common filters supported
- [ ] Documented filter options
- [ ] Sorting by relevant fields
- [ ] Clear error messages for invalid filters

### Error Handling
- [ ] Consistent error format
- [ ] Helpful error messages
- [ ] Appropriate status codes
- [ ] Request IDs for debugging

### Authentication
- [ ] Secure method (OAuth, JWT, API keys)
- [ ] HTTPS only
- [ ] Clear auth documentation
- [ ] Good error messages for auth failures

### Rate Limiting
- [ ] Implemented for all endpoints
- [ ] Rate limit headers included
- [ ] Clear limit information
- [ ] Graceful handling of exceeded limits

### Versioning
- [ ] Version strategy defined
- [ ] Backwards compatibility maintained
- [ ] Deprecation policy clear
- [ ] Migration guides provided

### Documentation
- [ ] Overview and getting started
- [ ] All endpoints documented
- [ ] Request/response examples
- [ ] Error documentation
- [ ] Code samples in multiple languages
- [ ] Interactive docs/playground

### Testing
- [ ] Unit tests for logic
- [ ] Integration tests for endpoints
- [ ] Contract tests for schemas
- [ ] Performance tests

---

## 💚 Consciousness in API Design

**APIs are interfaces between humans and systems.**

**Consciousness-first API design**:
- **Respect developer time**: Intuitive, well-documented APIs
- **Helpful errors**: Guide developers to success
- **Stability**: Don't break users without necessity
- **Accessibility**: Clear docs, multiple languages
- **Privacy**: Thoughtful data handling
- **Security**: Safe by default

**Great APIs empower developers to create.**  
**Poor APIs create frustration and waste time.**

**Design with empathy. Build with care.** 💚✨

---

## 📚 Related Resources

- [DEVELOPER_EXPERIENCE.md](DEVELOPER_EXPERIENCE.md) - DX principles
- [TESTING.md](TESTING.md) - Testing standards
- [SECURITY.md](SECURITY.md) - Security practices
- [DEPRECATION.md](DEPRECATION.md) - Deprecation policy
- [OBSERVABILITY.md](OBSERVABILITY.md) - Monitoring APIs

---

*This API design guide is maintained with care and consciousness by the Luminous Dynamics community.*
