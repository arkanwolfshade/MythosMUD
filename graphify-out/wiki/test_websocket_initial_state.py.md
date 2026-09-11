# test_websocket_initial_state.py

> 121 nodes

## Key Concepts

- **test_websocket_initial_state.py** (46 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **asyncio** (21 connections)
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **get_container_async_persistence()** (18 connections) — `server/container/async_persistence_access.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_event_handler_for_initial_state()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (9 connections)
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (7 connections)
- **_RealTimeEventHandlerForInitialState** (6 connections) — `server/realtime/websocket_initial_state.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **mock_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 96 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (16 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (11 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (8 shared connections)
- [Player](Player.md) (8 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [Room](Room.md) (5 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [real_time.py](real_time.py.md) (3 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [room_update_event_builder.py](room_update_event_builder.py.md) (2 shared connections)

## Source Files

- `server/container/async_persistence_access.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 289 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*