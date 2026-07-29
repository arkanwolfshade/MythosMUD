# player presence tracker

> 82 nodes

## Key Concepts

- **test_player_presence_tracker.py** (37 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **track_player_disconnected_impl()** (22 connections) — `server/realtime/player_presence_tracker.py`
- **player_presence_tracker.py** (15 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_connected_impl()** (14 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (9 connections)
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_build_player_info()** (8 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (4 connections)
- **_get_instance_manager_from_manager()** (4 connections) — `server/realtime/player_presence_tracker.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_unintentional_starts_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_removes_from_intentional_set()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_build_player_info_new_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_existing_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_build_player_info_no_level()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_no_persistence()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_success()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_resolve_room_id_room_no_id()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_new_connection()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 57 more nodes in this community*

## Relationships

- [Any](Any.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [disconnect grace period](disconnect_grace_period.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 292 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*