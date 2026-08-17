# handle_game_command

> 21 nodes

## Key Concepts

- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **test_handle_game_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_with_provided_args()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_broadcast_no_current_room_id()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_broadcast_no_player()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_with_broadcast()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **test_handle_game_command_empty_sends_invalid_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **WebSocket** (2 connections)
- **Handle a game command from a player. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/websocket_handler_commands.py`
- **Broadcast command_response to room when result requests it.** (1 connections) — `server/realtime/websocket_handler_commands.py`
- **Test handle_game_command processes game command.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test handle_game_command handles single word command with no args.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test handle_game_command processes command with provided args.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **Test handle_game_command handles broadcast.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **Test handle_game_command handles broadcast when player not found.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **Test handle_game_command handles broadcast when player has no current_room_id.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- **Test handle_game_command handles error.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Relationships

- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (9 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (9 shared connections)
- [test_websocket_handler_commands.py](test_websocket_handler_commands.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_websocket_handler_coverage_gaps.py](test_websocket_handler_coverage_gaps.py.md) (3 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (1 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 44 (76%)
- INFERRED: 14 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*