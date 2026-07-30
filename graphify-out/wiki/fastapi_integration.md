# fastapi integration

> 50 nodes

## Key Concepts

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
- **Any** (3 connections)
- **.accept()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.receive_text()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.send_text()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **Scope** (2 connections)
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- *... and 25 more nodes in this community*

## Relationships

- [world](world.md) (12 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (7 shared connections)
- [item](item.md) (3 shared connections)
- [testing examples](testing_examples.md) (2 shared connections)
- [websocket integration](websocket_integration.md) (2 shared connections)
- [migration examples](migration_examples.md) (1 shared connections)
- [Tests for get container dependency](Tests_for_get_container_dependency.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/migration_examples.py`
- `docs/examples/logging/testing_examples.py`
- `server/middleware/correlation_middleware.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 114 (79%)
- INFERRED: 30 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*