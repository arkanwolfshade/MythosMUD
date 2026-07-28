# Server Realtime (6)

> 145 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
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
- *... and 120 more nodes in this community*

## Relationships

- [Server Events](Server_Events.md) (24 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (11 shared connections)
- [Server Services](Server_Services.md) (11 shared connections)
- [Server Realtime (9)](Server_Realtime_%289%29.md) (10 shared connections)
- [Server Realtime (21)](Server_Realtime_%2821%29.md) (9 shared connections)
- [Server Realtime (24)](Server_Realtime_%2824%29.md) (7 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (5 shared connections)
- [Server Infrastructure (6)](Server_Infrastructure_%286%29.md) (4 shared connections)
- [Server Realtime (13)](Server_Realtime_%2813%29.md) (4 shared connections)
- [Server Api (9)](Server_Api_%289%29.md) (3 shared connections)
- [Server Realtime (16)](Server_Realtime_%2816%29.md) (3 shared connections)
- [Server Models (23)](Server_Models_%2823%29.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/event_handler.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 522 (92%)
- INFERRED: 43 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*