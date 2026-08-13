# bind_request_context

> 56 nodes

## Key Concepts

- **bind_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (11 connections) — `server/structured_logging/logging_context.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **websocket_endpoint()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **logging_context.py** (6 connections) — `server/structured_logging/logging_context.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **.disconnect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **get_current_context()** (5 connections) — `server/structured_logging/logging_context.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **process_websocket_message()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **migration_example_5()** (3 connections) — `docs/examples/logging/migration_examples.py`
- **test_context_binding()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **test_logging_correlation_ids()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **.broadcast_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.connect()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (3 connections) — `server/middleware/correlation_middleware.py`
- **Any** (3 connections)
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- *... and 31 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (6 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [log_with_context](log_with_context.md) (3 shared connections)
- [testing_examples.py](testing_examples.py.md) (2 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (1 shared connections)
- [factory.py](factory.py.md) (1 shared connections)
- [migration_examples.py](migration_examples.py.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/migration_examples.py`
- `docs/examples/logging/testing_examples.py`
- `docs/examples/logging/websocket_integration.py`
- `server/middleware/correlation_middleware.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 72 (79%)
- INFERRED: 19 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*