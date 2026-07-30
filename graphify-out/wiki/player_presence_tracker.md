# player presence tracker

> 21 nodes

## Key Concepts

- **track_player_disconnected_impl()** (29 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (4 connections)
- **test_track_player_disconnected_impl_finally_cleanup()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_should_skip_disconnect_has_websocket()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_should_skip_disconnect_no_connection_type()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_success()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_already_disconnecting()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_skip_disconnect()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_no_lock()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Check if player disconnection should be skipped.      Args:         player_id: T** (1 connections) — `server/realtime/player_presence_tracker.py`
- **Acquire disconnect lock and mark player as disconnecting.      Args:         pla** (1 connections) — `server/realtime/player_presence_tracker.py`
- **Track when a player disconnects.      For unintentional disconnects (connection** (1 connections) — `server/realtime/player_presence_tracker.py`
- **Test _should_skip_disconnect() returns True when player has websocket.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test _should_skip_disconnect() returns False when connection_type is None.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test _acquire_disconnect_lock() acquires lock successfully.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test _acquire_disconnect_lock() clears stuck player and succeeds.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test track_player_disconnected_impl() skips when player has connections.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test track_player_disconnected_impl() returns early if lock not acquired.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **Test track_player_disconnected_impl() always removes from disconnecting_players** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`

## Relationships

- [get asyncpg server settings for](get_asyncpg_server_settings_for.md) (11 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (10 shared connections)
- [Test get mortally wounded players()](Test_get_mortally_wounded_players%28%29.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [command admin](command_admin.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [test_should_skip_disconnect_no_websocket](test_should_skip_disconnect_no_websocket.md) (1 shared connections)
- [test_acquire_disconnect_lock_stuck_player](test_acquire_disconnect_lock_stuck_player.md) (1 shared connections)
- [test_track_player_disconnected_impl_error](test_track_player_disconnected_impl_error.md) (1 shared connections)
- [test_track_player_disconnected_impl_success](test_track_player_disconnected_impl_success.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`

## Audit Trail

- EXTRACTED: 82 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*