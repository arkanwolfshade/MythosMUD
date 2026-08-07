# app factory rationale

> 71 nodes

## Key Concepts

- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **bind_request_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **test_correlation_middleware.py** (17 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **middleware()** (16 connections) — `server/tests/unit/middleware/test_security_headers.py`
- **CorrelationMiddleware** (13 connections) — `server/middleware/correlation_middleware.py`
- **clear_request_context()** (13 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **correlation_middleware.py** (10 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketCorrelationMiddleware** (9 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **get_current_context()** (8 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (7 connections) — `server/structured_logging/logging_context.py`
- **_get_header()** (6 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (6 connections) — `server/middleware/correlation_middleware.py`
- **add_request_context()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (5 connections) — `server/middleware/correlation_middleware.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (3 connections)
- **test_create_correlation_middleware_factory()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_create_websocket_correlation_middleware()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_passes_non_http()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- **test_correlation_middleware_generates_correlation_id()** (3 connections) — `server/tests/unit/middleware/test_correlation_middleware.py`
- *... and 46 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (7 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (6 shared connections)
- [spell game magic](spell_game_magic.md) (6 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (5 shared connections)
- [security headers middleware](security_headers_middleware.md) (5 shared connections)
- [room cache services](room_cache_services.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (3 shared connections)
- [feature services flag](feature_services_flag.md) (2 shared connections)
- [examples logging testing](examples_logging_testing.md) (2 shared connections)
- [examples migration logging](examples_migration_logging.md) (1 shared connections)
- [command models moderation](command_models_moderation.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `server/middleware/correlation_middleware.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/middleware/test_correlation_middleware.py`
- `server/tests/unit/middleware/test_security_headers.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 214 (78%)
- INFERRED: 62 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*