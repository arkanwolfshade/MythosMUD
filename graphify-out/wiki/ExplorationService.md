# ExplorationService

> 100 nodes

## Key Concepts

- **ExplorationService** (64 connections) — `server/services/exploration_service.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **asyncio** (28 connections)
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_ensure_coordinates_generated()** (9 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **Any** (7 connections)
- **test_get_room_uuid_by_stable_id_no_session()** (6 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_CoordGenCtx** (5 connections) — `server/api/maps.py`
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
- *... and 75 more nodes in this community*

## Relationships

- [maps.py](maps.py.md) (18 shared connections)
- [test_maps.py](test_maps.py.md) (13 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [RoomService](RoomService.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [map_minimap.py](map_minimap.py.md) (2 shared connections)
- [update_room_position](update_room_position.md) (2 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [database.py](database.py.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/services/exploration_service.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 437 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*