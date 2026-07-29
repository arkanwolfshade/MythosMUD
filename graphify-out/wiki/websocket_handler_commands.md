# websocket handler commands

> 119 nodes

## Key Concepts

- **test_websocket_handler_core.py** (42 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_websocket_message()** (10 connections) — `server/realtime/websocket_handler.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **is_client_disconnected_exception()** (6 connections) — `server/realtime/websocket_helpers.py`
- **test_process_websocket_command_attaches_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_generic_exception()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception_should_break()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_get_help_content()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 94 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (19 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (11 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (10 shared connections)
- [Any](Any.md) (4 shared connections)
- [UUID](UUID.md) (4 shared connections)
- [help content](help_content.md) (4 shared connections)
- [.state()](state%28%29.md) (3 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (2 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (2 shared connections)
- [command execution request](command_execution_request.md) (2 shared connections)
- [.get room by id()](get_room_by_id%28%29.md) (2 shared connections)
- [main()](main%28%29.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_commands.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`

## Audit Trail

- EXTRACTED: 382 (91%)
- INFERRED: 39 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*