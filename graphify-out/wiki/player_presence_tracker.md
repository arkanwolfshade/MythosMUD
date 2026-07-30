# player presence tracker

> 88 nodes

## Key Concepts

- **test_player_presence_tracker.py** (38 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (31 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (29 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_connected_impl()** (16 connections) — `server/realtime/player_presence_tracker.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (9 connections)
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (4 connections)
- **instance_manager()** (4 connections) — `server/tests/unit/game/test_instance_manager.py`
- **test_broadcast_connection_message_impl_error()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_new_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_existing_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_no_level()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_success()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_room_no_id()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 63 more nodes in this community*

## Relationships

- [player disconnect handlers](player_disconnect_handlers.md) (12 shared connections)
- [real time](real_time.md) (10 shared connections)
- [Player](Player.md) (9 shared connections)
- [Any](Any.md) (8 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [command admin](command_admin.md) (2 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (1 shared connections)
- [spawn defaults](spawn_defaults.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/game/test_instance_manager.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 325 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*