# test_player_disconnect_handlers.py

> 79 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **disconnect_grace_period.py** (27 connections) — `server/realtime/disconnect_grace_period.py`
- **player_disconnect_handlers.py** (27 connections) — `server/realtime/player_disconnect_handlers.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
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
- **_session_ids_past_age_off()** (3 connections) — `server/realtime/player_disconnect_handlers.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_keeps_recent()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_missing_attrs_returns_zero()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_age_off_disconnected_sessions_removes_expired()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 54 more nodes in this community*

## Relationships

- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (13 shared connections)
- [is_player_in_grace_period](is_player_in_grace_period.md) (9 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [test_look_player.py](test_look_player.py.md) (1 shared connections)
- [test_look_room.py](test_look_room.py.md) (1 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (1 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 178 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*