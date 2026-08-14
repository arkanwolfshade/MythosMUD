# .__call__

> 8 nodes

## Key Concepts

- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (6 connections) — `server/middleware/correlation_middleware.py`
- **test_get_header_case_insensitive()** (2 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Scope** (2 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- **Return first header value for name (case-insensitive) from ASGI scope.** (1 connections) — `server/middleware/correlation_middleware.py`
- **ASGI application interface. Args: scope: ASGI connection scope receive: ASGI…** (1 connections) — `server/middleware/correlation_middleware.py`

## Relationships

- [middleware](middleware.md) (4 shared connections)
- [log_with_context](log_with_context.md) (2 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`

## Audit Trail

- EXTRACTED: 12 (86%)
- INFERRED: 2 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*