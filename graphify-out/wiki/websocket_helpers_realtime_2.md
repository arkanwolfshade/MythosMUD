# websocket helpers realtime

> 72 nodes

## Key Concepts

- **websocket_helpers.py** (37 connections) — `server/realtime/websocket_helpers.py`
- **test_websocket_helpers_player.py** (23 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **prepare_player_data()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_player_service_from_connection_manager()** (9 connections) — `server/realtime/websocket_helpers.py`
- **get_player_stats_data()** (9 connections) — `server/realtime/websocket_helpers.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- **build_basic_player_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **UUID** (6 connections)
- **_ensure_player_in_room_occupancy()** (6 connections) — `server/realtime/websocket_helpers.py`
- **_get_tracked_player_from_connection_manager()** (5 connections) — `server/realtime/websocket_helpers.py`
- **_fetch_room_for_tracked_player()** (4 connections) — `server/realtime/websocket_helpers.py`
- **.get_room_by_id()** (3 connections) — `server/realtime/websocket_handler_connection.py`
- **_AppStateForPlayerService** (3 connections) — `server/realtime/websocket_helpers.py`
- **test_check_shutdown_and_reject_not_shutting_down()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_shutting_down()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_websocket_disconnect()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_schema_to_dict_with_model_dump()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_convert_schema_to_dict_with_dict()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_player_service_from_connection_manager_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_service_from_connection_manager_no_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_service_from_connection_manager_no_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_stats_data_with_get_stats()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_stats_data_string_stats()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- *... and 47 more nodes in this community*

## Relationships

- [realtime websocket initial](realtime_websocket_initial.md) (18 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (6 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (4 shared connections)
- [combat commands handler](combat_commands_handler.md) (3 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [realtime game state](realtime_game_state.md) (2 shared connections)
- [status game spell](status_game_spell.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 248 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*