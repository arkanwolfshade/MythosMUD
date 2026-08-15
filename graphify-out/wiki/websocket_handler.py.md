# websocket_handler.py

> 104 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_helpers.py** (41 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_handler_message_loop.py** (26 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **is_client_disconnected_exception()** (9 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (9 connections)
- **handle_websocket_runtime_error()** (8 connections) — `server/realtime/websocket_handler_message_loop.py`
- **send_websocket_error_response()** (7 connections) — `server/realtime/websocket_handler_message_loop.py`
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **WebSocket** (7 connections)
- **send_welcome_event()** (6 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_json_decode_error()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_generic_exception()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **handle_websocket_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_exception_in_message_loop()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **process_websocket_inbound_message()** (6 connections) — `server/realtime/websocket_handler_message_loop.py`
- **UUID** (6 connections)
- **get_message_validator()** (5 connections) — `server/realtime/message_validator.py`
- **cleanup_websocket_connection()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **setup_initial_connection_state()** (5 connections) — `server/realtime/websocket_handler_connection.py`
- **UUID** (5 connections)
- *... and 79 more nodes in this community*

## Relationships

- [websocket_initial_state.py](websocket_initial_state.py.md) (20 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (14 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (14 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [MythosMUDError](MythosMUDError.md) (11 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (7 shared connections)
- [AttributeError](AttributeError.md) (5 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (3 shared connections)
- [test_cancel_shutdown_countdown_no_active](test_cancel_shutdown_countdown_no_active.md) (2 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/realtime/message_validator.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 263 (94%)
- INFERRED: 18 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*