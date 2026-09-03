# Security Headers

> 20 nodes

## Key Concepts

- **SecurityHeadersMiddleware** (12 connections) — `server/middleware/security_headers.py`
- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **.__init__()** (3 connections) — `server/middleware/security_headers.py`
- **test_security_headers_middleware_init()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init_with_env_vars()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Any** (2 connections)
- **ASGIApp** (1 connections)
- **Receive** (1 connections)
- **Request** (1 connections)
- **Scope** (1 connections)
- **Send** (1 connections)
- **Backward-compatible dispatch method for BaseHTTPMiddleware interface. This…** (1 connections) — `server/middleware/security_headers.py`
- **Add security headers to Response object (compatibility method).** (1 connections) — `server/middleware/security_headers.py`
- **Pure ASGI middleware to add comprehensive security headers to all HTTP…** (1 connections) — `server/middleware/security_headers.py`
- **Initialize security headers middleware. Args: app: ASGI application instance** (1 connections) — `server/middleware/security_headers.py`
- **ASGI application interface. Args: scope: ASGI connection scope receive: ASGI…** (1 connections) — `server/middleware/security_headers.py`
- **Test SecurityHeadersMiddleware initialization.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test SecurityHeadersMiddleware initialization with environment variables.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [Test Security Headers](Test_Security_Headers.md) (5 shared connections)
- [Character Creation API](Character_Creation_API.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 27 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*