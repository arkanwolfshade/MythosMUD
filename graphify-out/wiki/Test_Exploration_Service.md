# Test Exploration Service

> 98 nodes

## Key Concepts

- **ExplorationService** (66 connections) — `server/services/exploration_service.py`
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
- *... and 73 more nodes in this community*

## Relationships

- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (12 shared connections)
- [Maps](Maps.md) (10 shared connections)
- [Rooms](Rooms.md) (9 shared connections)
- [Test Map Minimap Helpers](Test_Map_Minimap_Helpers.md) (2 shared connections)
- [Test Player Position Service](Test_Player_Position_Service.md) (1 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (1 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)
- [Test Database Error Handling](Test_Database_Error_Handling.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/services/exploration_service.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 176 (77%)
- INFERRED: 52 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*