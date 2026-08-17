# send_initial_room_state

> 14 nodes

## Key Concepts

- **send_initial_room_state()** (19 connections) — `server/realtime/websocket_initial_state.py`
- **send_initial_game_state()** (15 connections) — `server/realtime/websocket_initial_state.py`
- **check_and_send_death_notification()** (14 connections) — `server/realtime/websocket_initial_state.py`
- **send_game_state_event_safely()** (10 connections) — `server/realtime/websocket_initial_state.py`
- **get_event_handler_for_initial_state()** (9 connections) — `server/realtime/websocket_initial_state.py`
- **UUID** (6 connections)
- **_get_player_for_death_check()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **WebSocket** (5 connections)
- **Send initial game state to connecting player. Returns tuple of…** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Get player and updated room ID for death check.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Check if player is dead and send death notification if needed.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Get event handler from connection manager or websocket app state.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Send initial room state and occupants snapshot to connecting player.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Send game state event with proper error handling. Returns: True if should exit…** (1 connections) — `server/realtime/websocket_initial_state.py`

## Relationships

- [ConnectionManager](ConnectionManager.md) (14 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (11 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [send_occupants_snapshot_if_needed](send_occupants_snapshot_if_needed.md) (2 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)
- [_get_death_location_name](_get_death_location_name.md) (1 shared connections)
- [test_check_and_send_death_notification_player_alive](test_check_and_send_death_notification_player_alive.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [test_send_initial_game_state_handles_exception](test_send_initial_game_state_handles_exception.md) (1 shared connections)
- [add_npc_occupants_to_list](add_npc_occupants_to_list.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 69 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*