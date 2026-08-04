# world loader room

> 29 nodes

## Key Concepts

- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **bind_request_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (13 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **get_current_context()** (8 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (7 connections) — `server/structured_logging/logging_context.py`
- **add_request_context()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (3 connections)
- **test_get_current_context_returns_empty_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (2 connections)
- **test_bind_request_context_generates_correlation_id()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_bind_request_context_omits_none_values()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_clear_request_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_get_current_context_returns_contextvars()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_log_with_context_merges_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Demonstrate correct request context binding.** (1 connections) — `docs/examples/logging/correct_patterns.py`
- **Add request context to all log entries using enhanced logging.** (1 connections) — `docs/examples/logging/fastapi_integration.py`
- **Process the WebSocket connection with correlation ID.          Args:** (1 connections) — `server/middleware/correlation_middleware.py`
- **Resolve an alert.          Args:             alert_id: ID of the alert to resolv** (1 connections) — `server/monitoring/monitoring_dashboard.py`
- **BoundLogger** (1 connections)
- **Context management utilities for enhanced logging.  This module provides functio** (1 connections) — `server/structured_logging/logging_context.py`
- **Bind request context to the current logging context.      This function sets up** (1 connections) — `server/structured_logging/logging_context.py`
- *... and 4 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (11 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (6 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (3 shared connections)
- [room cache services](room_cache_services.md) (3 shared connections)
- [app factory rationale](app_factory_rationale.md) (2 shared connections)
- [examples logging testing](examples_logging_testing.md) (2 shared connections)
- [add hashed password](add_hashed_password.md) (2 shared connections)
- [tick game service](tick_game_service.md) (2 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (2 shared connections)
- [examples migration logging](examples_migration_logging.md) (1 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `server/middleware/correlation_middleware.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 85 (69%)
- INFERRED: 39 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*