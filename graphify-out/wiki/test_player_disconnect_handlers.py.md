# test_player_disconnect_handlers.py

> 77 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (35 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_disconnect_handlers.py** (28 connections) — `server/realtime/player_disconnect_handlers.py`
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
- **test_cleanup_player_references()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 52 more nodes in this community*

## Relationships

- [disconnect_grace_period.py](disconnect_grace_period.py.md) (9 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (9 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [connection_cleanup_methods.py](connection_cleanup_methods.py.md) (3 shared connections)
- [extract_player_name](extract_player_name.md) (3 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 158 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*