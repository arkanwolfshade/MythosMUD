# .state

> 146 nodes

## Key Concepts

- **.state()** (37 connections) — `server/realtime/connection_state_machine.py`
- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_websocket_handler_app_state_connection.py** (24 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_websocket_handler_coverage_gaps.py** (24 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **handle_websocket_connection()** (21 connections) — `server/realtime/websocket_handler.py`
- **asyncio** (20 connections)
- **resolve_and_setup_app_state_services()** (19 connections) — `server/realtime/websocket_handler_app_state.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_chat_message()** (17 connections) — `server/realtime/websocket_handler.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **asyncio** (11 connections)
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **create_websocket_request_context()** (9 connections) — `server/realtime/request_context.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **asyncio** (8 connections)
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- *... and 121 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (16 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (15 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (11 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (9 shared connections)
- [ErrorType](ErrorType.md) (6 shared connections)
- [real_time.py](real_time.py.md) (5 shared connections)
- [GameStateProvider](GameStateProvider.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (4 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (2 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/realtime/request_context.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`

## Audit Trail

- EXTRACTED: 311 (84%)
- INFERRED: 61 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*