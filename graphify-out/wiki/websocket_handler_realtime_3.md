# websocket handler realtime

> 77 nodes

## Key Concepts

- **websocket_handler_commands.py** (32 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (28 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_websocket_handler_app_state_connection.py** (23 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **resolve_and_setup_app_state_services()** (20 connections) — `server/realtime/websocket_handler_app_state.py`
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **websocket_handler_app_state.py** (11 connections) — `server/realtime/websocket_handler_app_state.py`
- **resolve_websocket_connection_manager()** (11 connections) — `server/realtime/websocket_handler_commands.py`
- **_websocket_unified_command_result()** (10 connections) — `server/realtime/websocket_handler_commands.py`
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **test_process_websocket_command_attaches_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_services_from_container()** (4 connections) — `server/realtime/websocket_handler_app_state.py`
- **_cm_with_player_and_app()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Path** (4 connections)
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **_mirror_service_to_app_state()** (3 connections) — `server/realtime/websocket_handler_app_state.py`
- **_invoke_get_room_state_event()** (3 connections) — `server/realtime/websocket_handler_commands.py`
- **test_resolve_and_setup_app_state_services_services_already_set()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_missing_services()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_no_app_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_container_no_services()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- **test_resolve_and_setup_app_state_services_no_container_attribute()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- *... and 52 more nodes in this community*

## Relationships

- [websocket validation realtime](websocket_validation_realtime.md) (11 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (7 shared connections)
- [room look commands](room_look_commands.md) (6 shared connections)
- [combat commands handler](combat_commands_handler.md) (6 shared connections)
- [request context realtime](request_context_realtime.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (4 shared connections)
- [realtime game state](realtime_game_state.md) (3 shared connections)
- [models player related](models_player_related.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [command commands handler](command_commands_handler.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_handler_app_state.py`
- `server/realtime/websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_app_state_connection.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`

## Audit Trail

- EXTRACTED: 299 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*