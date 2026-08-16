# websocket_handler.py

> 50 nodes

## Key Concepts

- **websocket_handler.py** (65 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **websocket_handler_validation.py** (22 connections) — `server/realtime/websocket_handler_validation.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **validate_websocket_message()** (7 connections) — `server/realtime/websocket_handler_validation.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **resolve_expected_csrf_token()** (6 connections) — `server/realtime/websocket_handler_validation.py`
- **UUID** (6 connections)
- **check_websocket_message_rate_limit()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **validate_message_csrf_and_restore_metadata()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_connection_csrf_context()** (4 connections) — `server/realtime/websocket_handler_validation.py`
- **WebSocket** (4 connections)
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **extract_csrf_token_from_raw()** (3 connections) — `server/realtime/websocket_handler_validation.py`
- **restore_csrf_on_connection_metadata()** (3 connections) — `server/realtime/websocket_handler_validation.py`
- **Exception** (3 connections)
- **test_handle_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_handle_websocket_disconnect_no_connection_id()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- *... and 25 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (12 shared connections)
- [ErrorType](ErrorType.md) (11 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [build_event](build_event.md) (8 shared connections)
- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (5 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (5 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (4 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_handler_validation.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`

## Audit Trail

- EXTRACTED: 150 (89%)
- INFERRED: 19 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*