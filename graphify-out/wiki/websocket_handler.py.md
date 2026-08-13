# websocket_handler.py

> 60 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **websocket_handler_message_loop.py** (25 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
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
- **check_websocket_message_rate_limit()** (5 connections) — `server/realtime/websocket_handler_validation.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **get_connection_csrf_context()** (4 connections) — `server/realtime/websocket_handler_validation.py`
- **WebSocket** (4 connections)
- **test_websocket_handler_disconnect.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- **test_websocket_handler_helpers.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- **test_websocket_handler_json_error.py** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **mock_websocket()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- **test_handle_json_decode_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_json_error.py`
- *... and 35 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (9 shared connections)
- [StandardizedErrorResponse](StandardizedErrorResponse.md) (6 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (5 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (5 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (4 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (4 shared connections)
- [websocket_handler_connection.py](websocket_handler_connection.py.md) (4 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (3 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (3 shared connections)
- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (3 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_handler_validation.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_disconnect.py`
- `server/tests/unit/realtime/test_websocket_handler_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_json_error.py`

## Audit Trail

- EXTRACTED: 151 (89%)
- INFERRED: 18 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*