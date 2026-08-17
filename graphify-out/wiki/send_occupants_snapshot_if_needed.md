# send_occupants_snapshot_if_needed

> 8 nodes

## Key Concepts

- **send_occupants_snapshot_if_needed()** (8 connections) — `server/realtime/websocket_initial_state.py`
- **test_send_occupants_snapshot_if_needed_no_handler()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_occupants_snapshot_if_needed_player_not_in_room()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **test_send_occupants_snapshot_if_needed_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Send occupants snapshot if event handler is available (include connecting…** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Test send_occupants_snapshot_if_needed() sends snapshot when conditions met.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_occupants_snapshot_if_needed() does nothing when no handler.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Test send_occupants_snapshot_if_needed() calls…** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (4 shared connections)
- [asyncio](asyncio.md) (3 shared connections)
- [send_initial_room_state](send_initial_room_state.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*