# ExplorationService

> 91 nodes

## Key Concepts

- **ExplorationService** (77 connections) — `server/services/exploration_service.py`
- **test_exploration_service.py** (46 connections) — `server/tests/unit/services/test_exploration_service.py`
- **asyncio** (28 connections)
- **_row_scalar_one_or_none()** (10 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (7 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (7 connections) — `server/tests/unit/api/test_maps.py`
- **test_filter_explored_rooms_calls_room_service()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_room_uuid_by_stable_id_no_session()** (6 connections) — `server/tests/unit/services/test_exploration_service.py`
- **_async_session_maker_mock()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_database_error()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_explored_rooms_empty()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_like_uuid_object()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_asyncpg_uuid()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_database_error()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_not_found()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_string_uuid()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_with_session()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_database_error()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_database_error_in_query()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_false()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_is_room_explored_true()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_existing_record()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_mark_explored_in_session_new_record()** (5 connections) — `server/tests/unit/services/test_exploration_service.py`
- *... and 66 more nodes in this community*

## Relationships

- [maps.py](maps.py.md) (26 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (7 shared connections)
- [_apply_exploration_filter_if_needed](_apply_exploration_filter_if_needed.md) (6 shared connections)
- [RoomService](RoomService.md) (3 shared connections)
- [map_minimap.py](map_minimap.py.md) (2 shared connections)
- [User](User.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [test_rooms_api.py](test_rooms_api.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 176 (75%)
- INFERRED: 58 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*