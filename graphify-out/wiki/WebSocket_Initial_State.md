# WebSocket Initial State

> 110 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (7 connections)
- **_AppWithState** (7 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateForEventHandler** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_RealTimeHandlerContainer** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcOccupantDisplay** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_ContainerWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **WebSocket** (5 connections)
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- *... and 85 more nodes in this community*

## Relationships

- [Combat Aggro Threat](Combat_Aggro_Threat.md) (16 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (10 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (9 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (8 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (8 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (5 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (4 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (3 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (3 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (3 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 416 (93%)
- INFERRED: 30 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*