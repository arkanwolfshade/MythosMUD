# Community 221

> 69 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (48 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **flush_departing_tutorial_instance()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **asyncio** (10 connections)
- **InstanceFlushOwner** (9 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_flush_departing_tutorial_instance_flushes_the_players_instance()** (7 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **_FlushOwner** (6 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_flush_departing_tutorial_instance_skips_non_tutorial_players()** (6 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_empty_player_name()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_player_name()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_room_found()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_room_no_player()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_room_player_left_called()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_with_room()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references_marks_session_for_aging()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references_partial_cleanup()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_cleanup_player_references_without_persistence_skips_container_release()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_canonical_id()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_name()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_collect_disconnect_keys_no_player()** (3 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 44 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (24 shared connections)
- [Community 43](Community_43.md) (8 shared connections)
- [Community 155](Community_155.md) (5 shared connections)
- [Community 139](Community_139.md) (4 shared connections)
- [Container API Models](Container_API_Models.md) (4 shared connections)
- [Community 366](Community_366.md) (4 shared connections)
- [Community 207](Community_207.md) (1 shared connections)
- [Community 41](Community_41.md) (1 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (1 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 145 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*