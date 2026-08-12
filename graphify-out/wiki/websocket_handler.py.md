# websocket_handler.py

> 67 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **websocket_handler_validation.py** (21 connections) — `server/realtime/websocket_handler_validation.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_runtime_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **resolve_expected_csrf_token()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_websocket_message()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **is_websocket_disconnect_message()** (6 connections) — `server/realtime/websocket_helpers.py`
- **UUID** (6 connections)
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **check_websocket_message_rate_limit()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_message_csrf_and_restore_metadata()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_connection_csrf_context()** (4 connections) — `server/realtime/websocket_handler_validation.py`
- **WebSocket** (4 connections)
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_websocket_handler_json_error.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- *... and 42 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [ErrorType](ErrorType.md) (13 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (11 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (8 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (5 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (4 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [real_time.py](real_time.py.md) (1 shared connections)

## Source Files

- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_handler_validation.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`

## Audit Trail

- EXTRACTED: 259 (90%)
- INFERRED: 30 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*