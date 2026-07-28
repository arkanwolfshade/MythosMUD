# Active Lucidity Service

> 25 nodes · cohesion 0.10

## Key Concepts

- **correlation_middleware.py** (9 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (3 connections) — `server/middleware/correlation_middleware.py`
- **Any** (2 connections)
- **Scope** (2 connections)
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **ASGIApp** (1 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- **Correlation middleware for request tracing and logging context.  This middleware** (1 connections) — `server/middleware/correlation_middleware.py`
- **Middleware for adding correlation IDs to WebSocket connections.      This middle** (1 connections) — `server/middleware/correlation_middleware.py`
- **Initialize the WebSocket correlation middleware.          Args:             corr** (1 connections) — `server/middleware/correlation_middleware.py`
- **Process the WebSocket connection with correlation ID.          Args:** (1 connections) — `server/middleware/correlation_middleware.py`
- **Create a correlation middleware factory.      Args:         correlation_header:** (1 connections) — `server/middleware/correlation_middleware.py`
- **Create a WebSocket correlation middleware instance.      Args:         correlati** (1 connections) — `server/middleware/correlation_middleware.py`
- **Return first header value for name (case-insensitive) from ASGI scope.** (1 connections) — `server/middleware/correlation_middleware.py`
- **Pure ASGI middleware for adding correlation IDs and request context to all reque** (1 connections) — `server/middleware/correlation_middleware.py`
- **Initialize the correlation middleware.          Args:             app: ASGI appl** (1 connections) — `server/middleware/correlation_middleware.py`
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/correlation_middleware.py`

## Relationships

- [Development Setup Guide](Development_Setup_Guide.md) (4 shared connections)
- [FastAPI App Factory](FastAPI_App_Factory.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`

## Audit Trail

- EXTRACTED: 62 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*