# test_connection_disconnection.py

> 136 nodes

## Key Concepts

- **test_connection_disconnection.py** (40 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (35 connections) — `server/realtime/connection_disconnection.py`
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
- **connection_websocket_close.py** (9 connections) — `server/realtime/connection_websocket_close.py`
- **asyncio** (8 connections)
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_websocket_close.py`
- **_close_and_untrack_websockets()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_CloseableWebSocketManager** (5 connections) — `server/realtime/connection_websocket_close.py`
- **_session_cleanup_manager()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- *... and 111 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (20 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (9 shared connections)
- [RateLimiter](RateLimiter.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_websocket_close.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_manager_methods.py`

## Audit Trail

- EXTRACTED: 297 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*