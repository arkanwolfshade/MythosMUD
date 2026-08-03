# app factory rationale

> 36 nodes

## Key Concepts

- **test_correlation_middleware.py** (17 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **middleware()** (16 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **CorrelationMiddleware** (13 connections) — `server/middleware/correlation_middleware.py`
- **correlation_middleware.py** (10 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketCorrelationMiddleware** (9 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (6 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **test_create_correlation_middleware_factory()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_create_websocket_correlation_middleware()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_adds_response_header()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_reraises_exception()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware_generates_id()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Scope** (2 connections)
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **test_get_header_case_insensitive()** (2 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **ASGIApp** (1 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- *... and 11 more nodes in this community*

## Relationships

- [security headers middleware](security_headers_middleware.md) (5 shared connections)
- [world loader room](world_loader_room.md) (4 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (3 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 117 (84%)
- INFERRED: 23 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*