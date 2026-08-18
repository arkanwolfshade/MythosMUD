# server realtime connection disconnection

> 127 nodes

## Key Concepts

- **test_connection_disconnection.py** (40 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (35 connections) — `server/realtime/connection_disconnection.py`
- **_DisconnectConnectionManager** (26 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (26 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **room_subscription_manager.py** (21 connections) — `server/realtime/room_subscription_manager.py`
- **UUID** (16 connections)
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (14 connections)
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (10 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_apply_disconnect_side_effects()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_player_data()** (9 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (8 connections)
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_close_and_untrack_websockets()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **mock_manager()** (6 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **_session_cleanup_manager()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_cleanup_websocket_disconnect_clears_session_tracking()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_websocket()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- *... and 102 more nodes in this community*

## Relationships

- [deque](deque.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (8 shared connections)
- [server realtime rate limiter py](server_realtime_rate_limiter_py.md) (7 shared connections)
- [server realtime connection websocket close](server_realtime_connection_websocket_close.md) (6 shared connections)
- [server realtime room subscription manager](server_realtime_room_subscription_manager.md) (5 shared connections)
- [server realtime connection models](server_realtime_connection_models.md) (4 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (4 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)
- [server realtime connection establishment](server_realtime_connection_establishment.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 293 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*