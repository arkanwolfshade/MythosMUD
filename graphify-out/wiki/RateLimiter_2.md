# RateLimiter

> 277 nodes

## Key Concepts

- **RateLimiter** (68 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **test_connection_disconnection.py** (38 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (34 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_connection_disconnection_websockets.py** (26 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **_DisconnectConnectionManager** (23 connections) — `server/realtime/connection_disconnection.py`
- **message_queue.py** (17 connections) — `server/realtime/message_queue.py`
- **realtime/rate_limiter.py** (17 connections) — `server/realtime/rate_limiter.py`
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_websocket_close.py`
- **UUID** (13 connections)
- **_cleanup_room_subscriptions()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (12 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (12 connections)
- **_cleanup_fully_disconnected_player()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_player_data()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_apply_disconnect_side_effects()** (8 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (8 connections)
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_close_and_untrack_websockets()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- *... and 252 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (24 shared connections)
- [ConnectionManager](ConnectionManager.md) (18 shared connections)
- [deque](deque.md) (13 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (3 shared connections)
- [RateLimiter](RateLimiter.md) (3 shared connections)
- [is_websocket_open_impl](is_websocket_open_impl.md) (3 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [test_rate_limiter.py](test_rate_limiter.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_websocket_close.py`
- `server/realtime/message_queue.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 468 (84%)
- INFERRED: 91 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*