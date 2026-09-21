# test_websocket_initial_state.py

> 92 nodes

## Key Concepts

- **test_websocket_initial_state.py** (46 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **websocket_initial_state.py** (45 connections) — `server/realtime/websocket_initial_state.py`
- **asyncio** (21 connections)
- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_event_handler_for_initial_state()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_room_data_with_occupants()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **send_occupants_snapshot_if_needed()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **add_npc_occupants_to_list()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (7 connections)
- **_RealTimeEventHandlerForInitialState** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **mock_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_in_limbo()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_alive()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_success()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **WebSocket** (5 connections)
- **_get_death_location_name()** (4 connections) — `server/realtime/websocket_initial_state.py`
- **_get_event_handler_from_app_host()** (4 connections) — `server/realtime/websocket_initial_state.py`
- **test_add_npc_occupants_to_list_filters_dead_npcs()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- *... and 67 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (11 shared connections)
- [Protocol](Protocol.md) (10 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (9 shared connections)
- [Player](Player.md) (9 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [player_event_handlers_respawn_room.py](player_event_handlers_respawn_room.py.md) (4 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 232 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*