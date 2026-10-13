# Community 589

> 29 nodes

## Key Concepts

- **middleware()** (17 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **CorrelationMiddleware** (13 connections) — `server/middleware/correlation_middleware.py`
- **test_correlation_middleware.py** (12 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **correlation_middleware.py** (8 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (6 connections) — `server/middleware/correlation_middleware.py`
- **asyncio** (5 connections)
- **test_correlation_middleware_adds_response_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_reraises_exception()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **test_create_correlation_middleware_factory()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_get_header_case_insensitive()** (2 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Scope** (2 connections)
- **Any** (1 connections)
- **ASGIApp** (1 connections)
- **Receive** (1 connections)
- **Send** (1 connections)
- **Correlation middleware for request tracing and logging context. This middleware…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Create a correlation middleware factory. Args: correlation_header: HTTP header…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Return first header value for name (case-insensitive) from ASGI scope.** (1 connections) — `server/middleware/correlation_middleware.py`
- **Pure ASGI middleware for adding correlation IDs and request context to all…** (1 connections) — `server/middleware/correlation_middleware.py`
- *... and 4 more nodes in this community*

## Relationships

- [Community 298](Community_298.md) (6 shared connections)
- [Community 435](Community_435.md) (3 shared connections)
- [Community 571](Community_571.md) (3 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 307](Community_307.md) (1 shared connections)

## Source Files

- `server/middleware/correlation_middleware.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 50 (75%)
- INFERRED: 17 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*