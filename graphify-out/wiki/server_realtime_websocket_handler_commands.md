# server realtime websocket handler commands

> 114 nodes

## Key Concepts

- **test_websocket_handler_core.py** (43 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **websocket_handler_commands.py** (33 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (29 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **asyncio** (28 connections)
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **resolve_websocket_connection_manager()** (12 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **asyncio** (11 connections)
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_broadcast_command_room_if_needed()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_missing_room_attr()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_chat_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 89 more nodes in this community*

## Relationships

- [server realtime websocket handler handle](server_realtime_websocket_handler_handle.md) (14 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (11 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (11 shared connections)
- [server realtime websocket handler app](server_realtime_websocket_handler_app.md) (6 shared connections)
- [server container main get container](server_container_main_get_container.md) (5 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server commands help commands](server_commands_help_commands.md) (3 shared connections)
- [server commands look helpers lookrequest](server_commands_look_helpers_lookrequest.md) (2 shared connections)
- [server commands rescue commands](server_commands_rescue_commands.md) (2 shared connections)
- [server config init](server_config_init.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`

## Audit Trail

- EXTRACTED: 250 (88%)
- INFERRED: 33 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*