# player_presence_tracker.py

> 115 nodes

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
- **test_player_presence_tracker_grace_period.py** (7 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_GraceReconnectManager** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_connected_impl_warms_corruption_tier_cache()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- *... and 90 more nodes in this community*

## Relationships

- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (8 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (7 shared connections)
- [connection_manager.py](connection_manager.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [extract_player_name](extract_player_name.md) (5 shared connections)
- [models/player.py](models-player.py.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [CorruptionTier](CorruptionTier.md) (5 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 274 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*