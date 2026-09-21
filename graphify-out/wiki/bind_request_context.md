# bind_request_context

> 40 nodes

## Key Concepts

- **bind_request_context()** (21 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (16 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **get_current_context()** (10 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (10 connections) — `server/structured_logging/logging_context.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **websocket_endpoint()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **.disconnect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **_clear_context_around_test()** (4 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
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
- **.__init__()** (1 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket** (1 connections)
- **fixture** (1 connections)
- *... and 15 more nodes in this community*

## Relationships

- [websocket_handler.py](websocket_handler.py.md) (13 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (6 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [middleware](middleware.md) (3 shared connections)
- [testing_examples.py](testing_examples.py.md) (2 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [migration_examples.py](migration_examples.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/realtime/test_websocket_correlation_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 75 (81%)
- INFERRED: 18 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*