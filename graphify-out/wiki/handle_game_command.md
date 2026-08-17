# handle_game_command

> 41 nodes

## Key Concepts

- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (29 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **asyncio** (11 connections)
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_missing_room_attr()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_attach_room_state_to_result_adds_room_state_when_available()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_attach_room_state_to_result_noop_when_room_not_changed()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command_empty_sends_invalid_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_ok()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_empty_returns_none()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_explicit_args()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- *... and 16 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (18 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (11 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (6 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [ErrorType](ErrorType.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`

## Audit Trail

- EXTRACTED: 101 (80%)
- INFERRED: 25 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*