# app factory rationale

> 25 nodes

## Key Concepts

- **test_correlation_middleware.py** (17 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **middleware()** (16 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **CorrelationMiddleware** (13 connections) — `server/middleware/correlation_middleware.py`
- **correlation_middleware.py** (10 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketCorrelationMiddleware** (9 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (5 connections) — `server/middleware/correlation_middleware.py`
- **test_create_correlation_middleware_factory()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_create_websocket_correlation_middleware()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_adds_response_header()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_reraises_exception()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_websocket_correlation_middleware_generates_id()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **Correlation middleware for request tracing and logging context.  This middleware** (1 connections) — `server/middleware/correlation_middleware.py`
- **Pure ASGI middleware for adding correlation IDs and request context to all reque** (1 connections) — `server/middleware/correlation_middleware.py`
- **Middleware for adding correlation IDs to WebSocket connections.      This middle** (1 connections) — `server/middleware/correlation_middleware.py`
- **Initialize the WebSocket correlation middleware.          Args:             corr** (1 connections) — `server/middleware/correlation_middleware.py`
- **Create a correlation middleware factory.      Args:         correlation_header:** (1 connections) — `server/middleware/correlation_middleware.py`
- **Create a WebSocket correlation middleware instance.      Args:         correlati** (1 connections) — `server/middleware/correlation_middleware.py`
- **Unit tests for correlation ID middleware.** (1 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Create SecurityHeadersMiddleware instance.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [tick game service](tick_game_service.md) (4 shared connections)
- [security headers middleware](security_headers_middleware.md) (4 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (3 shared connections)
- [npc combat services](npc_combat_services.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [world loader room](world_loader_room.md) (2 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (1 shared connections)
- [persistence rationale player](persistence_rationale_player.md) (1 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 92 (81%)
- INFERRED: 21 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*