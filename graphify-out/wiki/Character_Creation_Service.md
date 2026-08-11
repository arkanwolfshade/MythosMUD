# Character Creation Service

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
- **.model_dump()** (4 connections) — `server/models/alias.py`
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
- *... and 34 more nodes in this community*

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (10 shared connections)
- [Party Service Management](Party_Service_Management.md) (9 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (5 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Real-Time Architecture Docs](Real-Time_Architecture_Docs.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)
- [Alias Expansion Logic](Alias_Expansion_Logic.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (1 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (1 shared connections)

## Source Files

- `server/models/alias.py`
- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`

## Audit Trail

- EXTRACTED: 213 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*