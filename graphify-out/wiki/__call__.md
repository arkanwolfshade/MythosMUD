# .__call__

> 7 nodes

## Key Concepts

- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **Scope** (2 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- **Return first header value for name (case-insensitive) from ASGI scope.** (1 connections) — `server/middleware/correlation_middleware.py`
- **ASGI application interface. Args: scope: ASGI connection scope receive: ASGI…** (1 connections) — `server/middleware/correlation_middleware.py`

## Relationships

- [get_config](get_config.md) (2 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`

## Audit Trail

- EXTRACTED: 9 (82%)
- INFERRED: 2 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*