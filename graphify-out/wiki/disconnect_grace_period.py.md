# disconnect_grace_period.py

> 108 nodes

## Key Concepts

- **disconnect_grace_period.py** (35 connections) — `server/realtime/disconnect_grace_period.py`
- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_disconnect_handlers.py** (28 connections) — `server/realtime/player_disconnect_handlers.py`
- **extract_player_name()** (22 connections) — `server/realtime/player_presence_utils.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **player_presence_utils.py** (18 connections) — `server/realtime/player_presence_utils.py`
- **test_player_presence_utils.py** (18 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **get_player_position()** (10 connections) — `server/realtime/player_presence_utils.py`
- **asyncio** (8 connections)
- **UUID** (7 connections)
- **_is_valid_name()** (6 connections) — `server/realtime/player_presence_utils.py`
- **_is_uuid_string()** (5 connections) — `server/realtime/player_presence_utils.py`
- **_grace_period_seconds()** (4 connections) — `server/realtime/disconnect_grace_period.py`
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_get_name_from_user()** (4 connections) — `server/realtime/player_presence_utils.py`
- **test_handle_player_disconnect_broadcast_empty_player_name()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_player_name()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room_found()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 83 more nodes in this community*

## Relationships

- [player_presence_tracker.py](player_presence_tracker.py.md) (16 shared connections)
- [start_grace_period](start_grace_period.md) (11 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [Player](Player.md) (5 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (4 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (3 shared connections)
- [get_config](get_config.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_presence_utils.py`

## Audit Trail

- EXTRACTED: 256 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*