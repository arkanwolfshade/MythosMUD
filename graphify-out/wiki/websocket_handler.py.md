# websocket_handler.py

> 90 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_helpers.py** (42 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (9 connections)
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **load_player_mute_data()** (8 connections) — `server/realtime/websocket_helpers.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **WebSocket** (7 connections)
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **.model_dump()** (4 connections) — `server/models/alias.py`
- **handle_websocket_disconnect()** (4 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_check_shutdown_and_reject_not_shutting_down()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_shutting_down()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- *... and 65 more nodes in this community*

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (21 shared connections)
- [ErrorType](ErrorType.md) (16 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (9 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (8 shared connections)
- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (7 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (4 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [send_welcome_event](send_welcome_event.md) (3 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)

## Source Files

- `server/models/alias.py`
- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 231 (92%)
- INFERRED: 19 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*