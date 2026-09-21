# establish_websocket_connection

> 41 nodes

## Key Concepts

- **establish_websocket_connection()** (25 connections) — `server/realtime/connection_establishment.py`
- **_FakeWebSocket** (23 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_connection_establishment_ws.py** (23 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_as_ws()** (21 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **asyncio** (11 connections)
- **test_establish_websocket_connection_first_session_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_missing_session_id_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_new_session_disconnects_prior()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_same_session_appends()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_player_with_room()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_cancels_rest_countdown()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_error()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_stale_session_does_not_replace()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_success()** (9 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_player_not_found()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_find_dead_connections_all_active()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_connected()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection_existing_player()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_with_active()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **.accept()** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **.close()** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **WebSocket** (1 connections)
- **Establish a new WebSocket connection. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 16 more nodes in this community*

## Relationships

- [test_connection_establishment.py](test_connection_establishment.py.md) (51 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (15 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [_FakeClientState](_FakeClientState.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment_ws.py`

## Audit Trail

- EXTRACTED: 165 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*