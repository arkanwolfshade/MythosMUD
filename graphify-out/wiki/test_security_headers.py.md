# test_security_headers.py

> 26 nodes

## Key Concepts

- **test_security_headers.py** (20 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **asyncio** (5 connections)
- **test_security_headers_middleware_adds_headers()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_error_handling()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_non_http_scope()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **mock_app()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method_error_handling()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init_with_env_vars()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_with_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_without_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **fixture** (2 connections)
- **Unit tests for security headers middleware. Tests the SecurityHeadersMiddleware…** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response adds headers to Response.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response includes subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response without subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Create a mock ASGI app.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method (backward compatibility).** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test SecurityHeadersMiddleware initialization.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test SecurityHeadersMiddleware initialization with environment variables.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware passes through non-HTTP connections.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- *... and 1 more nodes in this community*

## Relationships

- [middleware](middleware.md) (5 shared connections)
- [MutableHeaders](MutableHeaders.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*