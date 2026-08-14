# test_connection_establishment.py

> 102 nodes

## Key Concepts

- **test_connection_establishment.py** (51 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **connection_establishment.py** (24 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (22 connections) — `server/realtime/connection_establishment.py`
- **asyncio** (16 connections)
- **Any** (12 connections)
- **UUID** (12 connections)
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cancel_rest_countdown_if_active()** (8 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **test_establish_websocket_connection_error()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cancel_rest_countdown_if_active_cancels_leftover_rest()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cancels_rest_countdown()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_success()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 77 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 212 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*