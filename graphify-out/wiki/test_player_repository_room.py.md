# test_player_repository_room.py

> 20 nodes · cohesion 0.19

## Key Concepts

- **middleware()** (17 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **CorrelationMiddleware** (13 connections) — `server/middleware/correlation_middleware.py`
- **test_correlation_middleware.py** (12 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **correlation_middleware.py** (8 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **asyncio** (5 connections)
- **test_correlation_middleware_reraises_exception()** (5 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **log_api_requests()** (4 connections) — `docs/examples/logging/fastapi_integration.py`
- **test_correlation_middleware_adds_response_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_uses_existing_header()** (4 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_create_correlation_middleware_factory()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Log API requests with performance metrics.** (1 connections) — `docs/examples/logging/fastapi_integration.py`
- **Any** (1 connections)
- **Correlation middleware for request tracing and logging context. This middleware…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Create a correlation middleware factory. Args: correlation_header: HTTP header…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Pure ASGI middleware for adding correlation IDs and request context to all…** (1 connections) — `server/middleware/correlation_middleware.py`
- **Unit tests for correlation ID middleware.** (1 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **Create SecurityHeadersMiddleware instance.** (1 connections) — `server/tests/unit/middleware/test_security_headers.py`

## Relationships

- [FeedbackManager](FeedbackManager.md) (5 shared connections)
- [emote_row](emote_row.md) (4 shared connections)
- [AliasGraph](AliasGraph.md) (3 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [Detailed Feature Comparison](Detailed_Feature_Comparison.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [_WearablePersistence](_WearablePersistence.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `server/middleware/correlation_middleware.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`

## Audit Trail

- EXTRACTED: 43 (73%)
- INFERRED: 16 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*