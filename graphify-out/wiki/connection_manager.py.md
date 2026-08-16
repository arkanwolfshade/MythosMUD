# connection_manager.py

> 322 nodes

## Key Concepts

- **connection_manager.py** (169 connections) — `server/realtime/connection_manager.py`
- **connection_manager_methods.py** (82 connections) — `server/realtime/connection_manager_methods.py`
- **test_connection_manager_methods.py** (50 connections) — `server/tests/unit/realtime/test_connection_manager_methods.py`
- **test_connection_disconnection.py** (38 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (32 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (21 connections)
- **test_connection_disconnection_websockets.py** (20 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (16 connections) — `server/realtime/connection_disconnection.py`
- **canonical_room_id_impl()** (16 connections) — `server/realtime/connection_room_utils.py`
- **message_queue.py** (16 connections) — `server/realtime/message_queue.py`
- **realtime/rate_limiter.py** (16 connections) — `server/realtime/rate_limiter.py`
- **asyncio** (16 connections)
- **_cleanup_room_subscriptions()** (14 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (14 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_manager_methods.py`
- **delegate_game_state_provider()** (12 connections) — `server/realtime/connection_delegates.py`
- **force_disconnect_player_impl()** (12 connections) — `server/realtime/connection_manager_methods.py`
- **asyncio** (12 connections)
- **_cleanup_player_data()** (11 connections) — `server/realtime/connection_disconnection.py`
- **validate_player_presence_impl()** (11 connections) — `server/realtime/connection_statistics.py`
- **UUID** (11 connections)
- **unsubscribe_from_room_events_impl()** (10 connections) — `server/realtime/connection_event_helpers.py`
- *... and 297 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (84 shared connections)
- [UUID](UUID.md) (32 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (26 shared connections)
- [get_logger](get_logger.md) (26 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (20 shared connections)
- [test_connection_statistics.py](test_connection_statistics.py.md) (20 shared connections)
- [test_connection_room_utils.py](test_connection_room_utils.py.md) (12 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (11 shared connections)
- [RateLimiter](RateLimiter.md) (10 shared connections)
- [MessageQueue](MessageQueue.md) (8 shared connections)
- [test_connection_event_helpers.py](test_connection_event_helpers.py.md) (8 shared connections)
- [connection_manager_api.py](connection_manager_api.py.md) (8 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_room_utils.py`
- `server/realtime/connection_statistics.py`
- `server/realtime/message_queue.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 916 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*