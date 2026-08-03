# nats services service

> 8 nodes

## Key Concepts

- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **Any** (2 connections)
- **ASGIApp** (1 connections)
- **Pure ASGI middleware for adding correlation IDs and request context to all reque** (1 connections) — `server/middleware/correlation_middleware.py`
- **Initialize the correlation middleware.          Args:             app: ASGI appl** (1 connections) — `server/middleware/correlation_middleware.py`
- **Create a correlation middleware factory.      Args:         correlation_header:** (1 connections) — `server/middleware/correlation_middleware.py`

## Relationships

- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (2 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*