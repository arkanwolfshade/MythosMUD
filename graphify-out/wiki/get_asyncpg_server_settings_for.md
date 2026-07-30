# get asyncpg server settings for

> 20 nodes

## Key Concepts

- **test_player_presence_tracker.py** (38 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_new_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_existing_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_no_level()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_reconnect_during_grace()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_error()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_broadcast_connection_message_impl()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_broadcast_connection_message_impl_no_room()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_no_player()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Unit tests for player presence tracker.  Tests the player_presence_tracker modul** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test _build_player_info() creates new player info.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test _build_player_info() updates existing player info.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test _build_player_info() handles player without level.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Reconnect during disconnect grace must run enter setup (player_entered_game).** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test track_player_connected_impl() handles errors.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test broadcast_connection_message_impl() handles broadcast.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test broadcast_connection_message_impl() handles no room.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test broadcast_connection_message_impl() handles errors.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test track_player_disconnected_impl() handles player not found.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`

## Relationships

- [player presence tracker](player_presence_tracker.md) (11 shared connections)
- [Any](Any.md) (9 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [real time](real_time.md) (3 shared connections)
- [test_acquire_disconnect_lock_stuck_player](test_acquire_disconnect_lock_stuck_player.md) (1 shared connections)
- [Enhanced Logging Migration Report](Enhanced_Logging_Migration_Report.md) (1 shared connections)
- [test_resolve_room_id_room_no_id](test_resolve_room_id_room_no_id.md) (1 shared connections)
- [test_should_skip_disconnect_no_websocket](test_should_skip_disconnect_no_websocket.md) (1 shared connections)
- [test_track_player_disconnected_impl_error](test_track_player_disconnected_impl_error.md) (1 shared connections)
- [test_track_player_disconnected_impl_success](test_track_player_disconnected_impl_success.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_presence_tracker.py`

## Audit Trail

- EXTRACTED: 76 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*