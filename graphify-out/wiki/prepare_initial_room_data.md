# prepare_initial_room_data

> 4 nodes

## Key Concepts

- **prepare_initial_room_data()** (5 connections) — `server/realtime/websocket_initial_state.py`
- **test_prepare_initial_room_data()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Prepare room data for initial state event.** (1 connections) — `server/realtime/websocket_initial_state.py`
- **Test prepare_initial_room_data() prepares room data.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`

## Relationships

- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (2 shared connections)
- [send_initial_room_state](send_initial_room_state.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_initial_state.py`
- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*