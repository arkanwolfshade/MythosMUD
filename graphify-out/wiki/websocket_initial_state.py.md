# websocket_initial_state.py

> 115 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **asyncio** (21 connections)
- **get_async_persistence()** (19 connections) — `server/async_persistence.py`
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Protocol** (7 connections)
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_AppStateForEventHandler** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_AppStateWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_AppWithState** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_ContainerWithNpcLifecycle** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcOccupantDisplay** (5 connections) — `server/realtime/websocket_initial_state.py`
- **_RealTimeHandlerContainer** (5 connections) — `server/realtime/websocket_initial_state.py`
- *... and 90 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (13 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (10 shared connections)
- [ConnectionManager](ConnectionManager.md) (9 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (8 shared connections)
- [event_types.py](event_types.py.md) (7 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (6 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [real_time.py](real_time.py.md) (3 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 276 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*