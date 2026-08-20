# test_security_headers.py

> 36 nodes

## Key Concepts

- **test_security_headers.py** (21 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **SecurityHeadersMiddleware** (12 connections) — `server/middleware/security_headers.py`
- **MutableHeaders** (6 connections)
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **._add_security_headers()** (3 connections) — `server/middleware/security_headers.py`
- **.__init__()** (3 connections) — `server/middleware/security_headers.py`
- **test_add_security_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_csp_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_hsts_value()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_permissions_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_referrer_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init_with_env_vars()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_with_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_without_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Any** (2 connections)
- **ASGIApp** (1 connections)
- **Request** (1 connections)
- **Backward-compatible dispatch method for BaseHTTPMiddleware interface. This…** (1 connections) — `server/middleware/security_headers.py`
- **Add security headers to Response object (compatibility method).** (1 connections) — `server/middleware/security_headers.py`
- **Add all security headers to the response.** (1 connections) — `server/middleware/security_headers.py`
- **Pure ASGI middleware to add comprehensive security headers to all HTTP…** (1 connections) — `server/middleware/security_headers.py`
- **Initialize security headers middleware. Args: app: ASGI application instance** (1 connections) — `server/middleware/security_headers.py`
- *... and 11 more nodes in this community*

## Relationships

- [middleware](middleware.md) (8 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [.__call__](__call__.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 51 (89%)
- INFERRED: 6 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*