# test_player_disconnect_handlers.py

> 73 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **asyncio** (8 connections)
- **UUID** (7 connections)
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_empty_player_name()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_player_name()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room_found()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_room_no_player()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_room_player_left_called()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_with_room()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_keeps_recent()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_missing_attrs_returns_zero()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_removes_expired()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references_marks_session_for_aging()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references_partial_cleanup()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 48 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (9 shared connections)
- [start_grace_period](start_grace_period.md) (8 shared connections)
- [test_connection_delegates.py](test_connection_delegates.py.md) (6 shared connections)
- [extract_player_name](extract_player_name.md) (2 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [test_look_player.py](test_look_player.py.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [occupant_display.py](occupant_display.py.md) (1 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 154 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*