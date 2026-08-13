# test_player_presence_tracker.py

> 105 nodes

## Key Concepts

- **test_player_presence_tracker.py** (37 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (35 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (30 connections) — `server/realtime/player_presence_tracker.py`
- **extract_player_name()** (16 connections) — `server/realtime/player_presence_utils.py`
- **asyncio** (16 connections)
- **track_player_connected_impl()** (14 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (11 connections)
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **broadcast_connection_message_impl()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (7 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **get_player_position()** (6 connections) — `server/realtime/player_presence_utils.py`
- **UUID** (6 connections)
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **_get_name_from_user()** (4 connections) — `server/realtime/player_presence_utils.py`
- **_is_valid_name()** (4 connections) — `server/realtime/player_presence_utils.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- *... and 80 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (17 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (13 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (5 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [is_player_in_grace_period](is_player_in_grace_period.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (3 shared connections)
- [.state](state.md) (1 shared connections)
- [test_instance_manager.py](test_instance_manager.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 241 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*