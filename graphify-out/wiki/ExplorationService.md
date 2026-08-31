# ExplorationService

> 101 nodes

## Key Concepts

- **ExplorationService** (76 connections) — `server/services/exploration_service.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **asyncio** (27 connections)
- **_row_scalar_one_or_none()** (8 connections) — `server/tests/unit/services/test_exploration_service.py`
- **._get_room_uuid_by_stable_id()** (7 connections) — `server/services/exploration_service.py`
- **.mark_room_as_explored()** (7 connections) — `server/services/exploration_service.py`
- **UUID** (7 connections)
- **.is_room_explored()** (6 connections) — `server/services/exploration_service.py`
- **_row_scalar_one()** (6 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_get_room_uuid_by_stable_id_no_session()** (6 connections) — `server/tests/unit/services/test_exploration_service.py`
- **.get_explored_rooms()** (5 connections) — `server/services/exploration_service.py`
- **._mark_explored_in_session()** (5 connections) — `server/services/exploration_service.py`
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
- *... and 76 more nodes in this community*

## Relationships

- [maps.py](maps.py.md) (17 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [RoomService](RoomService.md) (8 shared connections)
- [map_minimap.py](map_minimap.py.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/exploration_service.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 186 (78%)
- INFERRED: 52 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*