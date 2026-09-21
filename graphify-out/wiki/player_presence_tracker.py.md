# player_presence_tracker.py

> 101 nodes

## Key Concepts

- **player_presence_tracker.py** (50 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker.py** (48 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **track_player_disconnected_impl()** (30 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_connected_impl()** (22 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (20 connections)
- **Any** (11 connections)
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_warm_corruption_tier_cache()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (10 connections)
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_send_grace_reconnect_catchup()** (8 connections) — `server/realtime/player_presence_tracker.py`
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_GraceReconnectManager** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_warms_corruption_tier_cache()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_already_disconnecting()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_acquire_disconnect_lock_stuck_player()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 76 more nodes in this community*

## Relationships

- [disconnect_grace_period.py](disconnect_grace_period.py.md) (16 shared connections)
- [CorruptionTier](CorruptionTier.md) (9 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (7 shared connections)
- [test_player_presence_tracker_grace_period.py](test_player_presence_tracker_grace_period.py.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (3 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`

## Audit Trail

- EXTRACTED: 259 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*