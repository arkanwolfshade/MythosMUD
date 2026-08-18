# RateLimiter

> 302 nodes

## Key Concepts

- **RateLimiter** (68 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **test_connection_disconnection.py** (40 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (35 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **_DisconnectConnectionManager** (26 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (26 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **UUID** (16 connections)
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (14 connections)
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_websocket_close.py`
- **_cleanup_room_subscriptions()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (10 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_apply_disconnect_side_effects()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_player_data()** (9 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (8 connections)
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_websocket_close.py`
- **_close_and_untrack_websockets()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- *... and 277 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (34 shared connections)
- [build_event](build_event.md) (20 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (12 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [StatisticsAggregator](StatisticsAggregator.md) (2 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (2 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [.connect_websocket](connect_websocket.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_websocket_close.py`
- `server/realtime/message_queue.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 544 (94%)
- INFERRED: 34 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*