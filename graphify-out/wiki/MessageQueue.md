# MessageQueue

> 204 nodes

## Key Concepts

- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **test_connection_disconnection.py** (43 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (34 connections) — `server/realtime/connection_disconnection.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **_DisconnectConnectionManager** (26 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (25 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **message_queue.py** (17 connections) — `server/realtime/message_queue.py`
- **realtime/rate_limiter.py** (17 connections) — `server/realtime/rate_limiter.py`
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
- **asyncio** (8 connections)
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_close_and_untrack_websockets()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **mock_manager()** (6 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 179 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (18 shared connections)
- [deque](deque.md) (13 shared connections)
- [RateLimiter](RateLimiter.md) (9 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (9 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (8 shared connections)
- [safe_close_websocket_impl](safe_close_websocket_impl.md) (6 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (4 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (4 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (3 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (2 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/message_queue.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 420 (95%)
- INFERRED: 23 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*