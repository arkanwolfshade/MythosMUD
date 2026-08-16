# test_connection_session_management.py

> 119 nodes

## Key Concepts

- **test_connection_session_management.py** (51 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **ConnectionMetadata** (28 connections) — `server/realtime/connection_models.py`
- **connection_session_management.py** (26 connections) — `server/realtime/connection_session_management.py`
- **_as_mgr()** (21 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_make_manager()** (20 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **handle_new_game_session_impl()** (17 connections) — `server/realtime/connection_session_management.py`
- **_SessionConnectionManager** (14 connections) — `server/realtime/connection_session_management.py`
- **_as_ws()** (14 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_FakeWebSocket** (13 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **_disconnect_connection_for_session()** (13 connections) — `server/realtime/connection_session_management.py`
- **asyncio** (13 connections)
- **connection_models.py** (12 connections) — `server/realtime/connection_models.py`
- **_disconnect_all_connections_for_session()** (10 connections) — `server/realtime/connection_session_management.py`
- **_cleanup_old_session_tracking()** (9 connections) — `server/realtime/connection_session_management.py`
- **_is_websocket_connected()** (9 connections) — `server/realtime/connection_session_management.py`
- **test_disconnect_all_connections_for_session()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_all_connections_for_session_partial_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_close_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_key_error()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_same_session_is_noop()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_handle_new_game_session_impl_success()** (9 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **_cleanup_player_data_for_session()** (8 connections) — `server/realtime/connection_session_management.py`
- **_meta()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- **test_disconnect_connection_for_session_not_connected()** (8 connections) — `server/tests/unit/realtime/test_connection_session_management.py`
- *... and 94 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (11 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (11 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (4 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [MessageQueue](MessageQueue.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/realtime/connection_models.py`
- `server/realtime/connection_session_management.py`
- `server/tests/unit/realtime/test_connection_models.py`
- `server/tests/unit/realtime/test_connection_session_management.py`

## Audit Trail

- EXTRACTED: 291 (93%)
- INFERRED: 21 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*