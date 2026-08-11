# Async Persistence Layer

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

- [WebSocket Initial State](WebSocket_Initial_State.md) (9 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (9 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (2 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)
- [Alias Expansion Logic](Alias_Expansion_Logic.md) (1 shared connections)
- [Services Lucidity Repository](Services_Lucidity_Repository.md) (1 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)

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