# Rooms

> 57 nodes

## Key Concepts

- **rooms.py** (49 connections) — `server/api/rooms.py`
- **room_service.py** (24 connections) — `server/game/room_service.py`
- **test_rooms_api.py** (24 connections) — `server/tests/unit/api/test_rooms_api.py`
- **exploration_service.py** (18 connections) — `server/services/exploration_service.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (13 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (9 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (9 connections) — `server/api/rooms.py`
- **asyncio** (8 connections)
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **test_update_room_position_room_missing()** (6 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_get_room_not_found()** (5 connections) — `server/tests/unit/api/test_rooms_api.py`
- **RoomDictList** (5 connections)
- **test_get_room_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_invalidate_room_cache()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_list_rooms_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_not_found()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- *... and 32 more nodes in this community*

## Relationships

- [Test Rooms Write Api](Test_Rooms_Write_Api.md) (40 shared connections)
- [Room Service](Room_Service.md) (13 shared connections)
- [Test Exploration Service](Test_Exploration_Service.md) (9 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (7 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (5 shared connections)
- [Players](Players.md) (4 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (4 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (4 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (4 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (4 shared connections)
- [Maps](Maps.md) (4 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (3 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 205 (90%)
- INFERRED: 22 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*