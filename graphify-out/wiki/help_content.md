# help content

> 104 nodes

## Key Concepts

- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content_with_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_system_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_chat_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_with_provided_args()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 79 more nodes in this community*

## Relationships

- [.is required()](is_required%28%29.md) (35 shared connections)
- [DropResolved](DropResolved.md) (4 shared connections)
- [convert pydantic error()](convert_pydantic_error%28%29.md) (3 shared connections)
- [.state()](state%28%29.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [websocket handler commands](websocket_handler_commands.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 290 (93%)
- INFERRED: 23 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*