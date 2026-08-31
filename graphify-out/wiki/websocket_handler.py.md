# websocket_handler.py

> 274 nodes

## Key Concepts

- **websocket_handler.py** (64 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_core.py** (43 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **websocket_handler_commands.py** (35 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (29 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **asyncio** (28 connections)
- **websocket_handler_message_loop.py** (27 connections) — `server/realtime/websocket_handler_message_loop.py`
- **test_websocket_handler_coverage_gaps.py** (26 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_websocket_handler_app_state_connection.py** (25 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **asyncio** (20 connections)
- **resolve_and_setup_app_state_services()** (19 connections) — `server/realtime/websocket_handler_app_state.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **websocket_handler_connection.py** (19 connections) — `server/realtime/websocket_handler_connection.py`
- **handle_websocket_connection()** (18 connections) — `server/realtime/websocket_handler.py`
- **handle_chat_message()** (17 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **create_websocket_request_context()** (11 connections) — `server/realtime/request_context.py`
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **is_websocket_disconnect_message()** (11 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (11 connections)
- **resolve_websocket_connection_manager()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_message_loop_exception()** (10 connections) — `server/realtime/websocket_handler_message_loop.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_system_message.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- *... and 249 more nodes in this community*

## Relationships

- [ErrorType](ErrorType.md) (30 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (14 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (13 shared connections)
- [build_event](build_event.md) (11 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (5 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (5 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (4 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (4 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)

## Source Files

- `server/realtime/request_context.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`

## Audit Trail

- EXTRACTED: 593 (93%)
- INFERRED: 46 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*