# test_player_disconnect_handlers.py

> 67 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **asyncio** (8 connections)
- **UUID** (7 connections)
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
- **test_collect_disconnect_keys_no_canonical_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 42 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (12 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (8 shared connections)
- [start_grace_period](start_grace_period.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [extract_player_name](extract_player_name.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 126 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*