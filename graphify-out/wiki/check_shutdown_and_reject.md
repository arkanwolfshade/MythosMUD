# check_shutdown_and_reject

> 22 nodes

## Key Concepts

- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **asyncio** (9 connections)
- **test_check_shutdown_and_reject_not_shutting_down()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_shutting_down()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_check_shutdown_and_reject_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_empty()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_filters_uuid()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_none()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_get_occupant_names_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_import_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **test_load_player_mute_data_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **WebSocket** (1 connections)
- **Check if server is shutting down and reject connection if so. Returns True if…** (1 connections) — `server/realtime/websocket_helpers.py`
- **Test check_shutdown_and_reject() returns True and closes connection when…** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test check_shutdown_and_reject() handles WebSocketDisconnect.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test load_player_mute_data() successfully loads mute data.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test load_player_mute_data() handles ImportError.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test get_occupant_names() extracts valid occupant names.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test get_occupant_names() filters out UUID strings.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test get_occupant_names() returns empty list for empty occupants.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test get_occupant_names() handles None occupants.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **Test check_shutdown_and_reject() returns False when not shutting down.** (1 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (12 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (4 shared connections)
- [test_websocket_handler_app_state_connection.py](test_websocket_handler_app_state_connection.py.md) (3 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*