# ExplorationService

> 86 nodes

## Key Concepts

- **ExplorationService** (64 connections) — `server/services/exploration_service.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **asyncio** (28 connections)
- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_no_session()** (6 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_async_session_maker_mock()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_empty()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_like_uuid_object()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_uuid()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_not_found()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_string_uuid()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_with_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_false()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_true()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_existing_record()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_new_record()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_commits_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_room_as_explored_no_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **exploration_service()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_fetchall()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_row_scalar_one()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_async_fetchall()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_database_error()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_generic_exception()** (4 connections) — `server/tests/unit/services/test_exploration_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [test_maps.py](test_maps.py.md) (7 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [MapZoneContext](MapZoneContext.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [_apply_exploration_filter_if_needed](_apply_exploration_filter_if_needed.md) (1 shared connections)
- [test_rooms_api.py](test_rooms_api.py.md) (1 shared connections)

## Source Files

- `server/services/exploration_service.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 193 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*