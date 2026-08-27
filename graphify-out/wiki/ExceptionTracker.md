# ExceptionTracker

> 90 nodes

## Key Concepts

- **test_websocket_handler_core.py** (43 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **asyncio** (28 connections)
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_chat_message()** (17 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_handle_chat_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_empty_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_single_word_no_args()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_whitespace_only()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_game_command_with_provided_args()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_generic_exception_should_break()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_chat()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_handle_websocket_message_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_aliases_dir()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_in_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_app_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_no_player()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_process_websocket_command_type_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_send_error_response()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- *... and 65 more nodes in this community*

## Relationships

- [test_goto_helpers.py](test_goto_helpers.py.md) (15 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (8 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (7 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (7 shared connections)
- [App.tsx](App.tsx.md) (6 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`

## Audit Trail

- EXTRACTED: 174 (92%)
- INFERRED: 16 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*