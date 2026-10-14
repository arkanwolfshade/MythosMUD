# websocket_handler.py

> 70 nodes

## Key Concepts

- **websocket_handler.py** (73 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (29 connections) — `server/realtime/websocket_handler_message_loop.py`
- **bind_request_context()** (21 connections) — `server/structured_logging/logging_context.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (16 connections) — `server/structured_logging/logging_context.py`
- **test_websocket_correlation_context.py** (12 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_current_context()** (10 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (10 connections) — `server/structured_logging/logging_context.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **_cleanup_connection_and_clear_context()** (5 connections) — `server/realtime/websocket_handler.py`
- **test_connection_binds_context_fields_before_message_loop()** (5 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **_clear_context_around_test()** (4 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- *... and 45 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (17 shared connections)
- [ErrorType](ErrorType.md) (11 shared connections)
- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (9 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (9 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (8 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (7 shared connections)
- [test_websocket_handler_commands.py](test_websocket_handler_commands.py.md) (6 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (5 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [test_security_headers.py](test_security_headers.py.md) (3 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/realtime/test_websocket_correlation_context.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 196 (80%)
- INFERRED: 48 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*