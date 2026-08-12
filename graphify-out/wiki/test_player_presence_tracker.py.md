# test_player_presence_tracker.py

> 86 nodes

## Key Concepts

- **test_player_presence_tracker.py** (37 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (31 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (28 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (16 connections)
- **track_player_connected_impl()** (14 connections) — `server/realtime/player_presence_tracker.py`
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (9 connections)
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_removes_from_intentional_set()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_unintentional_starts_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_acquire_disconnect_lock_already_disconnecting()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_stuck_player()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_success()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_broadcast_connection_message_impl()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_broadcast_connection_message_impl_no_room()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 61 more nodes in this community*

## Relationships

- [disconnect_grace_period.py](disconnect_grace_period.py.md) (9 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (9 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 353 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*