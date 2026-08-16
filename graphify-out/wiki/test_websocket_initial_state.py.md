# test_websocket_initial_state.py

> 99 nodes

## Key Concepts

- **test_websocket_initial_state.py** (47 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **websocket_initial_state.py** (46 connections) — `server/realtime/websocket_initial_state.py`
- **asyncio** (21 connections)
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **Protocol** (7 connections)
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_success()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **WebSocket** (5 connections)
- **_NpcLifecycleManagerForOccupants** (4 connections) — `server/realtime/websocket_initial_state.py`
- **_get_death_location_name()** (4 connections) — `server/realtime/websocket_initial_state.py`
- **test_add_npc_occupants_to_list_filters_dead_npcs()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 74 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (13 shared connections)
- [Player](Player.md) (8 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [check_shutdown_and_reject](check_shutdown_and_reject.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [player_event_handlers_respawn.py](player_event_handlers_respawn.py.md) (4 shared connections)
- [mock_connection_manager](mock_connection_manager.md) (4 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 240 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*