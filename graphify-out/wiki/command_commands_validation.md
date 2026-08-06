# command commands validation

> 8 nodes

## Key Concepts

- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (6 connections) — `server/middleware/correlation_middleware.py`
- **Scope** (2 connections)
- **test_get_header_case_insensitive()** (2 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Receive** (1 connections)
- **Send** (1 connections)
- **Return first header value for name (case-insensitive) from ASGI scope.** (1 connections) — `server/middleware/correlation_middleware.py`
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/correlation_middleware.py`

## Relationships

- [app factory rationale](app_factory_rationale.md) (4 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (2 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`

## Audit Trail

- EXTRACTED: 20 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*