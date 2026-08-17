# asyncio

> 17 nodes

## Key Concepts

- **asyncio** (21 connections)
- **test_check_and_send_death_notification_in_limbo()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_check_and_send_death_notification_player_dead()** (5 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_prepare_room_data_with_occupants()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_game_state_event_safely_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_game_state_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_room_state_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_room_state_skips_closed_websocket()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_initial_room_state_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_initial_game_state() returns None when player not found.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test check_and_send_death_notification() sends notification when player dead.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test check_and_send_death_notification() sends notification when in limbo.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_initial_room_state() successfully sends initial room state.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_initial_room_state() skips send when WebSocket already closed.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_initial_room_state() handles exceptions.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test prepare_room_data_with_occupants() prepares room data and occupant names.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_game_state_event_safely() successfully sends event.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (11 shared connections)
- [send_initial_room_state](send_initial_room_state.md) (7 shared connections)
- [add_npc_occupants_to_list](add_npc_occupants_to_list.md) (3 shared connections)
- [send_occupants_snapshot_if_needed](send_occupants_snapshot_if_needed.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [test_check_and_send_death_notification_player_alive](test_check_and_send_death_notification_player_alive.md) (1 shared connections)
- [prepare_initial_room_data](prepare_initial_room_data.md) (1 shared connections)
- [test_send_initial_game_state_handles_exception](test_send_initial_game_state_handles_exception.md) (1 shared connections)
- [test_send_initial_room_state_room_not_found](test_send_initial_room_state_room_not_found.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 45 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*