# realtime websocket initial

> 144 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_websocket_helpers.py** (34 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
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
- **load_player_mute_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **Protocol** (7 connections)
- **_AppWithState** (7 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateForEventHandler** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_RealTimeHandlerContainer** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcOccupantDisplay** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_ContainerWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- *... and 119 more nodes in this community*

## Relationships

- [websocket helpers realtime](websocket_helpers_realtime.md) (18 shared connections)
- [Room Broadcast](Room_Broadcast.md) (12 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (9 shared connections)
- [room websocket updates](room_websocket_updates.md) (8 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [combat models rationale](combat_models_rationale.md) (6 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (5 shared connections)
- [combat commands handler](combat_commands_handler.md) (4 shared connections)
- [room models instance](room_models_instance.md) (3 shared connections)
- [models player rationale](models_player_rationale.md) (3 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 519 (95%)
- INFERRED: 30 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*