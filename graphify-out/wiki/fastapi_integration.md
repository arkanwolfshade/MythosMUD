# fastapi integration

> 55 nodes

## Key Concepts

- **log_with_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **bind_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (11 connections) — `server/structured_logging/logging_context.py`
- **websocket_endpoint()** (9 connections) — `docs/examples/logging/fastapi_integration.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **logging_context.py** (6 connections) — `server/structured_logging/logging_context.py`
- **WebSocket** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **get_current_context()** (5 connections) — `server/structured_logging/logging_context.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **process_websocket_message()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **migration_example_5()** (3 connections) — `docs/examples/logging/migration_examples.py`
- **test_context_binding()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **test_logging_correlation_ids()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (3 connections) — `server/middleware/correlation_middleware.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (3 connections)
- **.accept()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.receive_text()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.send_text()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- *... and 30 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (10 shared connections)
- [websocket integration](websocket_integration.md) (9 shared connections)
- [useRoomMapData.test](useRoomMapData.test.md) (4 shared connections)
- [item](item.md) (3 shared connections)
- [PerformanceStats](PerformanceStats.md) (3 shared connections)
- [testing examples](testing_examples.md) (2 shared connections)
- [. is npc in combat()](_is_npc_in_combat%28%29.md) (2 shared connections)
- [migration examples](migration_examples.md) (1 shared connections)
- [test security headers](test_security_headers.md) (1 shared connections)
- [nats retry handler](nats_retry_handler.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [test player repository](test_player_repository.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/migration_examples.py`
- `docs/examples/logging/testing_examples.py`
- `server/middleware/correlation_middleware.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 125 (74%)
- INFERRED: 43 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*