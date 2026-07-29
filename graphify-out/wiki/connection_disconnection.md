# connection disconnection

> 90 nodes

## Key Concepts

- **test_connection_disconnection.py** (33 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (18 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (15 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **_DisconnectConnectionManager** (15 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (14 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (14 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (14 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (12 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (11 connections)
- **_cleanup_player_data()** (11 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (8 connections) — `server/realtime/connection_disconnection.py`
- **.has_websocket_connection()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (5 connections) — `server/realtime/connection_disconnection.py`
- **test_disconnect_connection_by_id_impl_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **testdisconnect_all_websockets_impl_empty_list()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_idempotent_second_pass()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **testdisconnect_all_websockets_impl_continues_after_none_websocket()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **test_disconnect_connection_by_id_impl_not_found()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **.disconnect_connection_by_id()** (3 connections) — `server/realtime/connection_manager.py`
- **test_track_disconnect_if_needed_new()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_already_processed()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 65 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (5 shared connections)
- [Any](Any.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 333 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*