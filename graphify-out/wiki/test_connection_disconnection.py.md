# test_connection_disconnection.py

> 95 nodes

## Key Concepts

- **test_connection_disconnection.py** (43 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (34 connections) — `server/realtime/connection_disconnection.py`
- **_DisconnectConnectionManager** (26 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (16 connections)
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (14 connections)
- **_cleanup_player_data()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (10 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_apply_disconnect_side_effects()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_close_and_untrack_websockets()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect_intentional_without_sockets()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect_when_mapping_cleared_during_close()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 70 more nodes in this community*

## Relationships

- [test_connection_disconnection_websockets.py](test_connection_disconnection_websockets.py.md) (14 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [connection_manager.py](connection_manager.py.md) (7 shared connections)
- [RateLimiter](RateLimiter.md) (4 shared connections)
- [safe_close_websocket_impl](safe_close_websocket_impl.md) (4 shared connections)
- [mock_manager](mock_manager.md) (4 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (3 shared connections)
- [MessageQueue](MessageQueue.md) (3 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`

## Audit Trail

- EXTRACTED: 228 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*