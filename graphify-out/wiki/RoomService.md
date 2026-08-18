# RoomService

> 65 nodes

## Key Concepts

- **RoomService** (75 connections) — `server/game/room_service.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **Any** (13 connections)
- **test_rooms_exploration_filter.py** (13 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **.get_room()** (8 connections) — `server/game/room_service.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **.filter_rooms_by_exploration()** (6 connections) — `server/game/room_service.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **.list_rooms()** (5 connections) — `server/game/room_service.py`
- **RoomDictList** (5 connections)
- **.get_local_chat_scope()** (4 connections) — `server/game/room_service.py`
- **.get_room_exits()** (4 connections) — `server/game/room_service.py`
- **.get_room_occupants()** (4 connections) — `server/game/room_service.py`
- **sample_rooms()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **asyncio** (4 connections)
- **._extract_occupants_from_room()** (3 connections) — `server/game/room_service.py`
- **.get_environment_state()** (3 connections) — `server/game/room_service.py`
- **.get_room_by_name()** (3 connections) — `server/game/room_service.py`
- **.get_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **.list_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **._lookup_explored_stable_ids()** (3 connections) — `server/game/room_service.py`
- *... and 40 more nodes in this community*

## Relationships

- [ExplorationService](ExplorationService.md) (21 shared connections)
- [test_rooms_api.py](test_rooms_api.py.md) (12 shared connections)
- [room_service.py](room_service.py.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [test_room_service.py](test_room_service.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [HealthService](HealthService.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 138 (83%)
- INFERRED: 28 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*