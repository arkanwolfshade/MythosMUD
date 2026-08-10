# Async Persistence Layer

> 58 nodes

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
- **test_prepare_player_data_service_error()** (3 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- *... and 33 more nodes in this community*

## Relationships

- [Combat Aggro Threat](Combat_Aggro_Threat.md) (10 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (7 shared connections)
- [Combat Command Helpers](Combat_Command_Helpers.md) (3 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (2 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (2 shared connections)
- [Logout and Quit Commands](Logout_and_Quit_Commands.md) (2 shared connections)
- [Plan Modernization Archive](Plan_Modernization_Archive.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 212 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*