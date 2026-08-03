# security headers middleware

> 22 nodes

## Key Concepts

- **test_security_headers.py** (20 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **middleware()** (6 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_non_http_scope()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_adds_headers()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_error_handling()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **mock_app()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_with_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_without_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method_error_handling()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Unit tests for security headers middleware.  Tests the SecurityHeadersMiddleware** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Create a mock ASGI app.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Create SecurityHeadersMiddleware instance.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware passes through non-HTTP connections.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware adds security headers to HTTP responses.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response adds headers to Response.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response includes subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response without subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method (backward compatibility).** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [security headers middleware](security_headers_middleware.md) (5 shared connections)
- [middleware security headers](middleware_security_headers.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*