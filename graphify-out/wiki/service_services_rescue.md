# service services rescue

> 4 nodes

## Key Concepts

- **mock_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **_passthrough_room_data()** (3 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Return room data unchanged for convert_room_players_uuids_to_names mocks.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/realtime/test_websocket_initial_state.py`

## Relationships

- [realtime websocket initial](realtime_websocket_initial.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 6 (67%)
- INFERRED: 3 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*