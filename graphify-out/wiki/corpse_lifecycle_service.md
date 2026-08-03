# corpse lifecycle service

> 82 nodes

## Key Concepts

- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_async_session_maker_mock()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_no_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_scalar_one()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_fetchall()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_no_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_with_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_not_found()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_string_uuid()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_like_uuid_object()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_new_record()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_existing_record()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_empty()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_true()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_false()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_sync_with_error_handler()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_uuid()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_database_error_in_query()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_commits_session()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- *... and 57 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (36 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [room game service](room_game_service.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 232 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*