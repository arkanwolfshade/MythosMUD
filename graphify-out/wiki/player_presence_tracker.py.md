# player_presence_tracker.py

> 70 nodes

## Key Concepts

- **player_presence_tracker.py** (60 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (32 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_connected_impl()** (22 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (11 connections)
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_warm_corruption_tier_cache()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (10 connections)
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id_for_tutorial_reconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_send_grace_reconnect_catchup()** (8 connections) — `server/realtime/player_presence_tracker.py`
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **.async_persistence()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (7 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **_GraceReconnectManager** (6 connections) — `server/realtime/player_presence_tracker.py`
- **RoomLookup** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_stranded_template_id()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **_RoomLookupOwner** (4 connections) — `server/realtime/player_presence_tracker.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_mid_rest_skips_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_removes_from_intentional_set()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_unintentional_starts_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- *... and 45 more nodes in this community*

## Relationships

- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (42 shared connections)
- [get_logger](get_logger.md) (21 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (7 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (6 shared connections)
- [extract_player_name](extract_player_name.md) (5 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [test_instance_manager.py](test_instance_manager.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (3 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [ground_channel.py](ground_channel.py.md) (2 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 220 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*