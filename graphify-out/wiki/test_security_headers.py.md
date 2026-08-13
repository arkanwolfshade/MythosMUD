# test_security_headers.py

> 41 nodes

## Key Concepts

- **test_security_headers.py** (20 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **middleware()** (9 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **MutableHeaders** (6 connections)
- **asyncio** (5 connections)
- **test_security_headers_middleware_adds_headers()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_error_handling()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_non_http_scope()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **._add_security_headers()** (3 connections) — `server/middleware/security_headers.py`
- **mock_app()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_csp_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_hsts_value()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_permissions_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_referrer_policy()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method_error_handling()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init_with_env_vars()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_with_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_without_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **fixture** (2 connections)
- **Add all security headers to the response.** (1 connections) — `server/middleware/security_headers.py`
- **Unit tests for security headers middleware. Tests the SecurityHeadersMiddleware…** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- *... and 16 more nodes in this community*

## Relationships

- [get_config](get_config.md) (5 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 55 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*