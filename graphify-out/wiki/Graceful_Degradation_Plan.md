# Graceful Degradation Plan

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

- [Phase Three Complete Summary](Phase_Three_Complete_Summary.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Components Map Layout](Components_Map_Layout.md) (2 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (1 shared connections)
- [Realtime Message Builders](Realtime_Message_Builders.md) (1 shared connections)
- [Game Profession Service](Game_Profession_Service.md) (1 shared connections)

## Source Files

- `server/middleware/security_headers.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 35 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*