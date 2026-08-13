# test_connection_establishment.py

> 112 nodes

## Key Concepts

- **test_connection_establishment.py** (48 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **connection_establishment.py** (24 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (20 connections) — `server/realtime/connection_establishment.py`
- **ConnectionMetadata** (14 connections) — `server/realtime/connection_models.py`
- **asyncio** (14 connections)
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **Any** (11 connections)
- **UUID** (11 connections)
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **connection_models.py** (6 connections) — `server/realtime/connection_models.py`
- **test_establish_websocket_connection_error()** (5 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_success()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 87 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [is_player_in_grace_period](is_player_in_grace_period.md) (2 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (1 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/realtime/connection_models.py`
- `server/tests/unit/realtime/test_connection_establishment.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 225 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*