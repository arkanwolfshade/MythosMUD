# Combat Domain Events

> 175 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **room.py** (31 connections) — `server/models/room.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Protocol** (7 connections)
- **_AppWithState** (7 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateForEventHandler** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- *... and 150 more nodes in this community*

## Relationships

- [Archive Bug Fix](Archive_Bug_Fix.md) (13 shared connections)
- [Party Service Management](Party_Service_Management.md) (13 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (12 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (10 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (10 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (9 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (9 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (8 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (7 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (6 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/models/room.py`
- `server/realtime/event_handler.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 652 (94%)
- INFERRED: 45 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*