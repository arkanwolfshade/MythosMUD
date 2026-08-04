# security headers middleware

> 33 nodes

## Key Concepts

- **test_security_headers.py** (20 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **MutableHeaders** (6 connections)
- **._add_security_headers()** (3 connections) — `server/middleware/security_headers.py`
- **test_security_headers_middleware_non_http_scope()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_adds_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_error_handling()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_hsts_value()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_permissions_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_csp_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_referrer_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **mock_app()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_with_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_without_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method_error_handling()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Add all security headers to the response.** (1 connections) — `server/middleware/security_headers.py`
- **Unit tests for security headers middleware.  Tests the SecurityHeadersMiddleware** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Create a mock ASGI app.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware passes through non-HTTP connections.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware adds security headers to HTTP responses.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response adds headers to Response.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response includes subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- *... and 8 more nodes in this community*

## Relationships

- [persistence rationale player](persistence_rationale_player.md) (5 shared connections)
- [app factory rationale](app_factory_rationale.md) (4 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 71 (88%)
- INFERRED: 10 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*