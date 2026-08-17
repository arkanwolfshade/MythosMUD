# RateLimiter

> 271 nodes

## Key Concepts

- **RateLimiter** (66 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (58 connections) — `server/realtime/message_queue.py`
- **test_connection_disconnection.py** (38 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **connection_disconnection.py** (32 connections) — `server/realtime/connection_disconnection.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_connection_disconnection_websockets.py** (25 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **_DisconnectConnectionManager** (21 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (17 connections) — `server/realtime/connection_disconnection.py`
- **message_queue.py** (16 connections) — `server/realtime/message_queue.py`
- **realtime/rate_limiter.py** (16 connections) — `server/realtime/rate_limiter.py`
- **_cleanup_room_subscriptions()** (14 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (14 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (12 connections) — `server/realtime/connection_manager_methods.py`
- **asyncio** (12 connections)
- **_cleanup_player_data()** (11 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (11 connections)
- **_cleanup_fully_disconnected_player()** (10 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (8 connections)
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **mock_manager()** (6 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 246 more nodes in this community*

## Relationships

- [deque](deque.md) (13 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (12 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (11 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [connection_manager.py](connection_manager.py.md) (8 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (8 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (3 shared connections)
- [test_rate_limiter.py](test_rate_limiter.py.md) (3 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (2 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/message_queue.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 456 (84%)
- INFERRED: 89 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*