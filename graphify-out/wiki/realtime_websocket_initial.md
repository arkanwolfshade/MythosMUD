# realtime websocket initial

> 151 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
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
- *... and 126 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (19 shared connections)
- [Room Broadcast](Room_Broadcast.md) (11 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (11 shared connections)
- [room websocket updates](room_websocket_updates.md) (11 shared connections)
- [combat models rationale](combat_models_rationale.md) (8 shared connections)
- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [combat services messaging](combat_services_messaging.md) (5 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (4 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (3 shared connections)
- [room models instance](room_models_instance.md) (3 shared connections)
- [models player rationale](models_player_rationale.md) (3 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 518 (92%)
- INFERRED: 45 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*