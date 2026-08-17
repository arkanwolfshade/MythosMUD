# docs examples logging correct patterns

> 42 nodes

## Key Concepts

- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **bind_request_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (13 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (13 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **get_current_context()** (8 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (8 connections) — `server/structured_logging/logging_context.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **update_player_background_task()** (7 connections) — `docs/examples/logging/fastapi_integration.py`
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **.disconnect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **.broadcast_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.connect()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_get_current_context_returns_empty_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (3 connections)
- **test_bind_request_context_generates_correlation_id()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_bind_request_context_omits_none_values()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_clear_request_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_get_current_context_returns_contextvars()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_log_with_context_merges_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (2 connections)
- **.__init__()** (1 connections) — `docs/examples/logging/websocket_integration.py`
- *... and 17 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (6 shared connections)
- [server middleware correlation middleware](server_middleware_correlation_middleware.md) (5 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (4 shared connections)
- [docs examples logging websocket integration](docs_examples_logging_websocket_integration.md) (3 shared connections)
- [docs examples logging correct patterns](docs_examples_logging_correct_patterns.md) (3 shared connections)
- [server monitoring init getattr](server_monitoring_init_getattr.md) (3 shared connections)
- [performancestats](performancestats.md) (3 shared connections)
- [docs examples logging testing examples](docs_examples_logging_testing_examples.md) (2 shared connections)
- [claude rules structlog](claude_rules_structlog.md) (2 shared connections)
- [docs examples logging migration examples](docs_examples_logging_migration_examples.md) (1 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/middleware/correlation_middleware.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 68 (67%)
- INFERRED: 33 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*