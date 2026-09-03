# Test Security Headers

> 16 nodes

## Key Concepts

- **middleware()** (12 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **asyncio** (5 connections)
- **test_security_headers_middleware_adds_headers()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_error_handling()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_non_http_scope()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **mock_app()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method_error_handling()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **fixture** (2 connections)
- **Test middleware error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Create a mock ASGI app.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method (backward compatibility).** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Create SecurityHeadersMiddleware instance.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware passes through non-HTTP connections.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware adds security headers to HTTP responses.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [Test Security Headers](Test_Security_Headers.md) (7 shared connections)
- [Test Comprehensive Logging](Test_Comprehensive_Logging.md) (3 shared connections)
- [Websocket Integration](Websocket_Integration.md) (1 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (1 shared connections)
- [Security Headers](Security_Headers.md) (1 shared connections)

## Source Files

- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 26 (87%)
- INFERRED: 4 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*