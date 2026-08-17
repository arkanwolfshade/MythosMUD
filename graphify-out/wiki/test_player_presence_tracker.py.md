# test_player_presence_tracker.py

> 94 nodes

## Key Concepts

- **test_player_presence_tracker.py** (39 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (35 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (30 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (17 connections)
- **track_player_connected_impl()** (15 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (11 connections)
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (8 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (6 connections)
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_mid_rest_skips_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_removes_from_intentional_set()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_unintentional_starts_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_acquire_disconnect_lock_already_disconnecting()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 69 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (10 shared connections)
- [extract_player_name](extract_player_name.md) (6 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (3 shared connections)
- [.state](state.md) (2 shared connections)
- [start_grace_period](start_grace_period.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 218 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*