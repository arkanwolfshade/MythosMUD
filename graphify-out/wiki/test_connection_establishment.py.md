# test_connection_establishment.py

> 165 nodes

## Key Concepts

- **test_connection_establishment.py** (57 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_as_mgr()** (44 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **_make_manager()** (42 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **connection_establishment.py** (41 connections) — `server/realtime/connection_establishment.py`
- **ConnectionMetadata** (30 connections) — `server/realtime/connection_models.py`
- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (25 connections) — `server/realtime/connection_establishment.py`
- **_FakeWebSocket** (23 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_connection_establishment_ws.py** (23 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_as_ws()** (21 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **UUID** (16 connections)
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **connection_models.py** (13 connections) — `server/realtime/connection_models.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **_meta()** (11 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **asyncio** (11 connections)
- **asyncio** (11 connections)
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **test_establish_websocket_connection_first_session_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_missing_session_id_does_not_replace()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_new_session_disconnects_prior()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **test_establish_websocket_connection_same_session_appends()** (10 connections) — `server/tests/unit/realtime/test_connection_establishment_ws.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- *... and 140 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (19 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (10 shared connections)
- [MessageQueue](MessageQueue.md) (8 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (3 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (3 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (3 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [start_grace_period](start_grace_period.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [safe_close_websocket_impl](safe_close_websocket_impl.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/realtime/connection_models.py`
- `server/tests/unit/realtime/test_connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment_ws.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 481 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*