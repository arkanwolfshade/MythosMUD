# websocket_handler.py

> 99 nodes

## Key Concepts

- **websocket_handler.py** (69 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (29 connections) — `server/realtime/websocket_handler_message_loop.py`
- **bind_request_context()** (21 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (16 connections) — `server/structured_logging/logging_context.py`
- **test_websocket_correlation_context.py** (12 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_current_context()** (10 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (10 connections) — `server/structured_logging/logging_context.py`
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **.disconnect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- *... and 74 more nodes in this community*

## Relationships

- [websocket_handler_commands.py](websocket_handler_commands.py.md) (14 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [ErrorType](ErrorType.md) (12 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (8 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (7 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (6 shared connections)
- [test_enhanced_error_logging.py](test_enhanced_error_logging.py.md) (5 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (4 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (4 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/realtime/test_websocket_correlation_context.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 236 (86%)
- INFERRED: 37 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*