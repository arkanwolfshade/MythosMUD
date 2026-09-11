# _as_mgr

> 69 nodes

## Key Concepts

- **_as_mgr()** (44 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_make_manager()** (42 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **establish_websocket_connection()** (25 connections) — `server/realtime/connection_establishment.py`
- **_FakeWebSocket** (23 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_connection_establishment_ws.py** (23 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_as_ws()** (21 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_meta()** (12 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
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
- **test_cleanup_failed_connection_success()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_player_not_found()** (8 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_find_dead_connections_all_active()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_connected()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection_existing_player()** (7 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 44 more nodes in this community*

## Relationships

- [test_connection_establishment.py](test_connection_establishment.py.md) (55 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (27 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [_FakeEstablishmentManager](_FakeEstablishmentManager.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment_ws.py`

## Audit Trail

- EXTRACTED: 262 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*