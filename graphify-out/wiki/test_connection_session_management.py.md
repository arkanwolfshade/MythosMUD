# test_connection_session_management.py

> 105 nodes

## Key Concepts

- **test_connection_session_management.py** (49 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **connection_session_management.py** (26 connections) — `server/realtime/connection_session_management.py`
- **_as_mgr()** (21 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_make_manager()** (20 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_SessionConnectionManager** (15 connections) — `server/realtime/connection_session_management.py`
- **handle_new_game_session_impl()** (15 connections) — `server/realtime/connection_session_management.py`
- **_as_ws()** (14 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_FakeWebSocket** (13 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_disconnect_connection_for_session()** (13 connections) — `server/realtime/connection_session_management.py`
- **asyncio** (13 connections)
- **_disconnect_all_connections_for_session()** (10 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_old_session_tracking()** (9 connections) — `server/realtime/connection_session_management.py`
- **_is_websocket_connected()** (9 connections) — `server/realtime/connection_session_management.py`
- **_migrate_player_to_new_session()** (9 connections) — `server/realtime/connection_session_management.py`
- **test_disconnect_all_connections_for_session()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_partial_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_close_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_key_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_same_session_is_noop()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **NewGameSessionResult** (8 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_player_data_for_session()** (8 connections) — `server/realtime/connection_session_management.py`
- **_meta()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_not_connected()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_success()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- *... and 80 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (19 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 264 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*