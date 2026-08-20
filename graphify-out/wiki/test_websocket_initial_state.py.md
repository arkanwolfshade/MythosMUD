# test_websocket_initial_state.py

> 119 nodes

## Key Concepts

- **test_websocket_initial_state.py** (47 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **websocket_initial_state.py** (46 connections) — `server/realtime/websocket_initial_state.py`
- **.app()** (33 connections) — `server/commands/look_helpers.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **models/room.py** (32 connections) — `server/models/room.py`
- **asyncio** (21 connections)
- **get_container_async_persistence()** (19 connections) — `server/async_persistence.py`
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
- **get_npc_lifecycle_manager_from_connection_manager()** (7 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (7 connections)
- **UUID** (6 connections)
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **mock_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 94 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (14 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (12 shared connections)
- [pytest.md](pytest.md.md) (12 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (11 shared connections)
- [build_event](build_event.md) (7 shared connections)
- [Room](Room.md) (7 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [NPCEnteredRoom](NPCEnteredRoom.md) (6 shared connections)
- [real_time.py](real_time.py.md) (5 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/commands/look_helpers.py`
- `server/models/room.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 334 (90%)
- INFERRED: 39 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*