# FeedbackManager

> 24 nodes · cohesion 0.10

## Key Concepts

- **test_security_headers.py** (20 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **asyncio** (5 connections)
- **test_security_headers_middleware_error_handling()** (5 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method_error_handling()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_adds_headers()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_non_http_scope()** (4 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **mock_app()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_dispatch_method()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init_with_env_vars()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **fixture** (2 connections)
- **test_add_security_headers_to_response()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_with_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_add_security_headers_to_response_hsts_without_subdomains()** (2 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Unit tests for security headers middleware. Tests the SecurityHeadersMiddleware…** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response adds headers to Response.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response includes subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test _add_security_headers_to_response without subdomains in HSTS.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Create a mock ASGI app.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method (backward compatibility).** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test dispatch method error handling.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test SecurityHeadersMiddleware initialization with environment variables.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware passes through non-HTTP connections.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test middleware adds security headers to HTTP responses.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [TestDepartures](TestDepartures.md) (5 shared connections)
- [test_player_repository_room.py](test_player_repository_room.py.md) (5 shared connections)
- [_WearablePersistence](_WearablePersistence.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 41 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*