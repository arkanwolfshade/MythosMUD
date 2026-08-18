# UUID

> 71 nodes

## Key Concepts

- **UUID** (41 connections)
- **._track_player_disconnected()** (7 connections) — `server/realtime/connection_manager.py`
- **.broadcast_connection_message()** (5 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket()** (5 connections) — `server/realtime/connection_manager.py`
- **._get_player()** (5 connections) — `server/realtime/connection_manager.py`
- **.track_player_connected()** (5 connections) — `server/realtime/connection_manager.py`
- **Player** (5 connections)
- **._check_and_process_disconnect()** (4 connections) — `server/realtime/connection_manager.py`
- **.check_connection_health()** (4 connections) — `server/realtime/connection_manager.py`
- **._cleanup_dead_websocket()** (4 connections) — `server/realtime/connection_manager.py`
- **.force_disconnect_player()** (4 connections) — `server/realtime/connection_manager.py`
- **._get_players_batch()** (4 connections) — `server/realtime/connection_manager.py`
- **.handle_new_login()** (4 connections) — `server/realtime/connection_manager.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **._prune_player_from_all_rooms()** (4 connections) — `server/realtime/connection_manager.py`
- **.recover_from_error()** (4 connections) — `server/realtime/connection_manager.py`
- **._send_initial_game_state()** (4 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (4 connections) — `server/realtime/connection_manager.py`
- **._validate_token()** (4 connections) — `server/realtime/connection_manager.py`
- **.broadcast_to_room()** (3 connections) — `server/realtime/connection_manager.py`
- **.check_rate_limit()** (3 connections) — `server/realtime/connection_manager.py`
- **.disconnect_websocket_connection()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_connection_count()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_message_delivery_stats()** (3 connections) — `server/realtime/connection_manager.py`
- **.get_pending_messages()** (3 connections) — `server/realtime/connection_manager.py`
- *... and 46 more nodes in this community*

## Relationships

- [ConnectionManager](ConnectionManager.md) (33 shared connections)
- [delegate_error_handler](delegate_error_handler.md) (5 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (1 shared connections)
- [test_connection_cleanup_methods.py](test_connection_cleanup_methods.py.md) (1 shared connections)
- [.connect_websocket](connect_websocket.md) (1 shared connections)
- [NewGameSessionResult](NewGameSessionResult.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 129 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*