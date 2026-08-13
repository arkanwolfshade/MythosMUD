# websocket_initial_state.py

> 113 nodes

## Key Concepts

- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **test_websocket_initial_state.py** (45 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **asyncio** (21 connections)
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
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
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- *... and 88 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (16 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (15 shared connections)
- [ConnectionManager](ConnectionManager.md) (9 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (9 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [log_and_raise](log_and_raise.md) (4 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [.state](state.md) (3 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 264 (94%)
- INFERRED: 16 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*