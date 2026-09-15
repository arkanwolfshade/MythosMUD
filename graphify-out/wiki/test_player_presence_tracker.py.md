# test_player_presence_tracker.py

> 107 nodes

## Key Concepts

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
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (7 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_warms_corruption_tier_cache()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_mid_rest_skips_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_removes_from_intentional_set()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_unintentional_starts_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- *... and 82 more nodes in this community*

## Relationships

- [player_presence_tracker.py](player_presence_tracker.py.md) (22 shared connections)
- [CorruptionTier](CorruptionTier.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [extract_player_name](extract_player_name.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (3 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (1 shared connections)
- [.state](state.md) (1 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 231 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*