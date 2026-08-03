# realtime player connection

> 29 nodes

## Key Concepts

- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **test_handle_game_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_with_provided_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_resolve_connection_manager_from_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_game_command_runtime_error_handling()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **test_handle_game_command_with_broadcast()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_player()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_current_room_id()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **WebSocket** (2 connections)
- **test_handle_game_command_empty_sends_invalid_error()** (2 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Handle a game command from a player.      Args:         websocket: The WebSoc** (1 connections) — `server/realtime/websocket_handler_commands.py`
- **Test handle_game_command processes game command.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test handle_game_command handles empty command.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test handle_game_command handles whitespace-only command.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test handle_game_command handles single word command with no args.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test handle_game_command processes command with provided args.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test handle_game_command resolves connection_manager from app when None (lines 4** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **Test handle_game_command RuntimeError handling path (lines 472-480).** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- **Test handle_game_command handles broadcast.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- *... and 4 more nodes in this community*

## Relationships

- [room look commands](room_look_commands.md) (7 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (5 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_coverage_gaps.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 60 (70%)
- INFERRED: 26 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*