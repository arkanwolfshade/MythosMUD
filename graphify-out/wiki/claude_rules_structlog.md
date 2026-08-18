# claude rules structlog

> 55 nodes

## Key Concepts

- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **bind_request_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (13 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (13 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **get_current_context()** (8 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (8 connections) — `server/structured_logging/logging_context.py`
- **structlog.md** (8 connections) — `.claude/rules/structlog.md`
- **Structured Logging with Structlog Best Practices** (8 connections) — `.claude/rules/structlog.md`
- **update_player_background_task()** (7 connections) — `docs/examples/logging/fastapi_integration.py`
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **7. Tooling and Environment** (5 connections) — `.claude/rules/structlog.md`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **1. Code Organization and Structure** (4 connections) — `.claude/rules/structlog.md`
- **2. Common Patterns and Anti-patterns** (4 connections) — `.claude/rules/structlog.md`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_get_current_context_returns_empty_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (3 connections)
- **3. Performance Considerations** (3 connections) — `.claude/rules/structlog.md`
- **4. Security Best Practices** (3 connections) — `.claude/rules/structlog.md`
- **5. Testing Approaches** (3 connections) — `.claude/rules/structlog.md`
- **6. Common Pitfalls and Gotchas** (3 connections) — `.claude/rules/structlog.md`
- **test_bind_request_context_generates_correlation_id()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_bind_request_context_omits_none_values()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_clear_request_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_get_current_context_returns_contextvars()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- *... and 30 more nodes in this community*

## Relationships

- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server middleware correlation middleware](server_middleware_correlation_middleware.md) (5 shared connections)
- [server monitoring exception metrics](server_monitoring_exception_metrics.md) (5 shared connections)
- [docs examples logging correct patterns](docs_examples_logging_correct_patterns.md) (3 shared connections)
- [server monitoring monitoring dashboard monitoringdashboard](server_monitoring_monitoring_dashboard_monitoringdashboard.md) (3 shared connections)
- [performancestats](performancestats.md) (3 shared connections)
- [docs examples logging testing examples](docs_examples_logging_testing_examples.md) (3 shared connections)
- [server monitoring exception tracker](server_monitoring_exception_tracker.md) (2 shared connections)
- [docs examples logging websocket integration](docs_examples_logging_websocket_integration.md) (2 shared connections)
- [docs examples logging migration examples](docs_examples_logging_migration_examples.md) (1 shared connections)
- [server game player service playerservice](server_game_player_service_playerservice.md) (1 shared connections)

## Source Files

- `.claude/rules/structlog.md`
- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 82 (71%)
- INFERRED: 33 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*