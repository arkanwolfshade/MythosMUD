# RateLimiter

> 187 nodes

## Key Concepts

- **RateLimiter** (66 connections) — `server/realtime/rate_limiter.py`
- **test_connection_disconnection.py** (37 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (19 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **cleanup_websocket_disconnect()** (16 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (14 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (14 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_manager_methods.py`
- **force_disconnect_player_impl()** (12 connections) — `server/realtime/connection_manager_methods.py`
- **asyncio** (12 connections)
- **_cleanup_player_data()** (11 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (11 connections)
- **_cleanup_fully_disconnected_player()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (7 connections)
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **mock_manager()** (6 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_connection_by_id_impl_websocket()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 162 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (46 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (10 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [RateLimiter](RateLimiter.md) (3 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (2 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (1 shared connections)
- [handle_new_game_session_impl](handle_new_game_session_impl.md) (1 shared connections)
- [test_rate_limiter.py](test_rate_limiter.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`

## Audit Trail

- EXTRACTED: 323 (87%)
- INFERRED: 49 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*