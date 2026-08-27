# test_goto_helpers.py

> 47 nodes

## Key Concepts

- **websocket_handler_commands.py** (30 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (29 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **handle_game_command()** (28 connections) — `server/realtime/websocket_handler_commands.py`
- **asyncio** (11 connections)
- **resolve_websocket_connection_manager()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (5 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (5 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_send_invalid_command_empty()** (4 connections) — `server/realtime/websocket_handler_commands.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command_broadcasts_when_result_requests()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_missing_room_attr()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **_broadcast_command_room_if_needed()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_attach_room_state_to_result_adds_room_state_when_available()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_attach_room_state_to_result_noop_when_room_not_changed()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_handle_game_command_empty_sends_invalid_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_validate_player_and_persistence_not_found()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- *... and 22 more nodes in this community*

## Relationships

- [ExceptionTracker](ExceptionTracker.md) (15 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (7 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (5 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [App.tsx](App.tsx.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (2 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (1 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (1 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (1 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`

## Audit Trail

- EXTRACTED: 126 (89%)
- INFERRED: 16 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*