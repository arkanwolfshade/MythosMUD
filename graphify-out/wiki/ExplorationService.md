# ExplorationService

> 119 nodes

## Key Concepts

- **ExplorationService** (76 connections) — `server/services/exploration_service.py`
- **test_exploration_service.py** (44 connections) — `server/tests/unit/services/test_exploration_service.py`
- **asyncio** (27 connections)
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_row_scalar_one_or_none()** (8 connections) — `server/tests/unit/services/test_exploration_service.py`
- **._get_room_uuid_by_stable_id()** (7 connections) — `server/services/exploration_service.py`
- **.mark_room_as_explored()** (7 connections) — `server/services/exploration_service.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
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
- *... and 94 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (18 shared connections)
- [maps.py](maps.py.md) (17 shared connections)
- [RoomService](RoomService.md) (6 shared connections)
- [rooms.py](rooms.py.md) (4 shared connections)
- [map_minimap.py](map_minimap.py.md) (2 shared connections)
- [test_rooms_api.py](test_rooms_api.py.md) (2 shared connections)
- [InstanceManager](InstanceManager.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [User](User.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 222 (80%)
- INFERRED: 56 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*