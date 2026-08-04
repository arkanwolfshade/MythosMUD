# persistence rationale player

> 22 nodes

## Key Concepts

- **SecurityHeadersMiddleware** (13 connections) — `server/middleware/security_headers.py`
- **security_headers.py** (6 connections) — `server/middleware/security_headers.py`
- **.__call__()** (5 connections) — `server/middleware/security_headers.py`
- **.dispatch()** (5 connections) — `server/middleware/security_headers.py`
- **._add_security_headers_to_response()** (4 connections) — `server/middleware/security_headers.py`
- **.__init__()** (3 connections) — `server/middleware/security_headers.py`
- **test_security_headers_middleware_init()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **test_security_headers_middleware_init_with_env_vars()** (3 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Any** (2 connections)
- **ASGIApp** (1 connections)
- **Scope** (1 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- **Request** (1 connections)
- **Security headers middleware for MythosMUD server.  This module provides comprehe** (1 connections) — `server/middleware/security_headers.py`
- **Pure ASGI middleware to add comprehensive security headers to all HTTP responses** (1 connections) — `server/middleware/security_headers.py`
- **Initialize security headers middleware.          Args:             app: ASGI app** (1 connections) — `server/middleware/security_headers.py`
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/security_headers.py`
- **Backward-compatible dispatch method for BaseHTTPMiddleware interface.          T** (1 connections) — `server/middleware/security_headers.py`
- **Add security headers to Response object (compatibility method).** (1 connections) — `server/middleware/security_headers.py`
- **Test SecurityHeadersMiddleware initialization.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **Test SecurityHeadersMiddleware initialization with environment variables.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [security headers middleware](security_headers_middleware.md) (5 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [npc combat services](npc_combat_services.md) (1 shared connections)
- [app factory rationale](app_factory_rationale.md) (1 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 56 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*