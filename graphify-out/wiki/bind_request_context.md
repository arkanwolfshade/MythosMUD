# bind_request_context

> 40 nodes

## Key Concepts

- **bind_request_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (13 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (13 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **get_current_context()** (8 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (8 connections) — `server/structured_logging/logging_context.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **websocket_endpoint()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **.disconnect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **process_websocket_message()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **.broadcast_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.connect()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **test_get_current_context_returns_empty_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (3 connections)
- **test_bind_request_context_generates_correlation_id()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_bind_request_context_omits_none_values()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_clear_request_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_get_current_context_returns_contextvars()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_log_with_context_merges_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (2 connections)
- **.__init__()** (1 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket** (1 connections)
- *... and 15 more nodes in this community*

## Relationships

- [ExceptionTracker](ExceptionTracker.md) (6 shared connections)
- [middleware](middleware.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [testing_examples.py](testing_examples.py.md) (2 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (2 shared connections)
- [general_exception_handler](general_exception_handler.md) (1 shared connections)
- [migration_examples.py](migration_examples.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/middleware/correlation_middleware.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 65 (76%)
- INFERRED: 20 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*