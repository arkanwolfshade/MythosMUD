# connection disconnection

> 96 nodes

## Key Concepts

- **test_connection_disconnection.py** (37 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (31 connections) — `server/realtime/connection_disconnection.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (15 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (15 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (15 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **message_queue.py** (14 connections) — `server/realtime/message_queue.py`
- **rate_limiter.py** (14 connections) — `server/realtime/rate_limiter.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_player_data()** (12 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (12 connections) — `server/realtime/connection_manager_methods.py`
- **UUID** (11 connections)
- **_cleanup_fully_disconnected_player()** (8 connections) — `server/realtime/connection_disconnection.py`
- **.has_websocket_connection()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_connection_by_id_impl_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **.disconnect_connection_by_id()** (3 connections) — `server/realtime/connection_manager.py`
- **test_track_disconnect_if_needed_new()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_already_processed()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 71 more nodes in this community*

## Relationships

- [Player](Player.md) (19 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (15 shared connections)
- [nats config()](nats_config%28%29.md) (8 shared connections)
- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (8 shared connections)
- [real time](real_time.md) (5 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [Any](Any.md) (3 shared connections)
- [test statistics aggregator](test_statistics_aggregator.md) (2 shared connections)
- [connection delegates](connection_delegates.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/message_queue.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 395 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*