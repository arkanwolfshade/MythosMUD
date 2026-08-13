# test_connection_disconnection.py

> 96 nodes

## Key Concepts

- **test_connection_disconnection.py** (34 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **_DisconnectConnectionManager** (20 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (19 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (12 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (12 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (12 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (12 connections)
- **asyncio** (10 connections)
- **_cleanup_player_data()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_run_websocket_disconnect_cleanup()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (7 connections)
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect_when_mapping_cleared_during_close()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_connection_by_id_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_already_processed()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_force_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 71 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (21 shared connections)
- [connection_manager.py](connection_manager.py.md) (6 shared connections)
- [MessageQueue](MessageQueue.md) (3 shared connections)
- [RateLimiter](RateLimiter.md) (3 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 200 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*