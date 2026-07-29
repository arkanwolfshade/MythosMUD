# ASGIApp

> 14 nodes

## Key Concepts

- **SecurityHeadersMiddleware** (13 connections) — `server/middleware/security_headers.py`
- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **.__init__()** (3 connections) — `server/middleware/security_headers.py`
- **test_security_headers_middleware_init()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init_with_env_vars()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **ASGIApp** (1 connections)
- **Scope** (1 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- **Pure ASGI middleware to add comprehensive security headers to all HTTP responses** (1 connections) — `server/middleware/security_headers.py`
- **Initialize security headers middleware.          Args:             app: ASGI app** (1 connections) — `server/middleware/security_headers.py`
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/security_headers.py`
- **Test SecurityHeadersMiddleware initialization.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test SecurityHeadersMiddleware initialization with environment variables.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [test security headers](test_security_headers.md) (3 shared connections)
- [BaseUserManager](BaseUserManager.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [MutableHeaders](MutableHeaders.md) (1 shared connections)
- [middleware()](middleware%28%29.md) (1 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 35 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*