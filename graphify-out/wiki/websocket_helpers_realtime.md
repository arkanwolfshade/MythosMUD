# websocket helpers realtime

> 59 nodes

## Key Concepts

- **websocket_helpers.py** (37 connections) — `server/realtime/websocket_helpers.py`
- **test_websocket_helpers_player.py** (23 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
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
- **test_get_player_service_from_connection_manager_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_service_from_connection_manager_no_app()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_service_from_connection_manager_no_state()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_stats_data_with_get_stats()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_stats_data_string_stats()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_stats_data_adds_health()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_get_player_stats_data_no_get_stats()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_build_basic_player_data()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_build_basic_player_data_defaults()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_with_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **test_prepare_player_data_no_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- *... and 34 more nodes in this community*

## Relationships

- [realtime websocket initial](realtime_websocket_initial.md) (11 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (7 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (5 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [realtime game state](realtime_game_state.md) (2 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 214 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*