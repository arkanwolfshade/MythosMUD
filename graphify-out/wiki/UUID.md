# UUID

> 61 nodes

## Key Concepts

- **UUID** (42 connections)
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_authentication_error()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_websocket_error()** (4 connections) — `server/realtime/connection_manager.py`
- **._prune_player_from_all_rooms()** (4 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (4 connections) — `server/realtime/connection_manager.py`
- **._validate_token()** (4 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (3 connections) — `server/realtime/connection_manager.py`
- **.check_rate_limit()** (3 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket_connection()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_connection_count()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_pending_messages()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_player_presence_info()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_player_session()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_player_websocket_connection_id()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_rate_limit_info()** (3 connections) — `server/realtime/connection_manager.py`
- **.has_websocket_connection()** (3 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message()** (3 connections) — `server/realtime/connection_manager.py`
- *... and 36 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (30 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (5 shared connections)
- [.broadcast_connection_message](broadcast_connection_message.md) (5 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (2 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (2 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (1 shared connections)
- [test_connection_cleanup_methods.py](test_connection_cleanup_methods.py.md) (1 shared connections)
- [NewGameSessionResult](NewGameSessionResult.md) (1 shared connections)
- [mark_player_seen_impl](mark_player_seen_impl.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 114 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*