# test_websocket_handler_commands.py

> 36 nodes

## Key Concepts

- **test_websocket_handler_commands.py** (29 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **resolve_websocket_connection_manager()** (12 connections) — `server/realtime/websocket_handler_commands.py`
- **asyncio** (11 connections)
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_missing_room_attr()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_attach_room_state_to_result_adds_room_state_when_available()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_attach_room_state_to_result_noop_when_room_not_changed()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_ok()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_empty_returns_none()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_explicit_args()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_single_word_no_args()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_parse_game_command_tokens_splits_string()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_resolve_get_room_state_callable_requires_player_handler_with_method()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- *... and 11 more nodes in this community*

## Relationships

- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [handle_game_command](handle_game_command.md) (6 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`

## Audit Trail

- EXTRACTED: 87 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*