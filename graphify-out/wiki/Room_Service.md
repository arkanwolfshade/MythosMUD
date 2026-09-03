# Room Service

> 47 nodes

## Key Concepts

- **RoomService** (78 connections) — `server/game/room_service.py`
- **Any** (13 connections)
- **.get_room()** (8 connections) — `server/game/room_service.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **.filter_rooms_by_exploration()** (6 connections) — `server/game/room_service.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **.list_rooms()** (5 connections) — `server/game/room_service.py`
- **.get_local_chat_scope()** (4 connections) — `server/game/room_service.py`
- **.get_room_exits()** (4 connections) — `server/game/room_service.py`
- **.get_room_occupants()** (4 connections) — `server/game/room_service.py`
- **._extract_occupants_from_room()** (3 connections) — `server/game/room_service.py`
- **.get_environment_state()** (3 connections) — `server/game/room_service.py`
- **.get_room_by_name()** (3 connections) — `server/game/room_service.py`
- **.get_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **.list_rooms_in_zone()** (3 connections) — `server/game/room_service.py`
- **._lookup_explored_stable_ids()** (3 connections) — `server/game/room_service.py`
- **._prepare_room_for_list()** (3 connections) — `server/game/room_service.py`
- **._room_matches_zone_filters()** (3 connections) — `server/game/room_service.py`
- **.search_rooms_by_name()** (3 connections) — `server/game/room_service.py`
- **.validate_exit_exists()** (3 connections) — `server/game/room_service.py`
- **.describe_lighting()** (2 connections) — `server/game/room_service.py`
- **.__init__()** (2 connections) — `server/game/room_service.py`
- **.update_environment_state()** (2 connections) — `server/game/room_service.py`
- **.validate_player_in_room()** (2 connections) — `server/game/room_service.py`
- **.validate_room_exists()** (2 connections) — `server/game/room_service.py`
- *... and 22 more nodes in this community*

## Relationships

- [Test Rooms Write Api](Test_Rooms_Write_Api.md) (15 shared connections)
- [Rooms](Rooms.md) (13 shared connections)
- [Maps](Maps.md) (9 shared connections)
- [Test Map Minimap Helpers](Test_Map_Minimap_Helpers.md) (5 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (4 shared connections)
- [Test Room Service](Test_Room_Service.md) (3 shared connections)
- [Test Schedule Service](Test_Schedule_Service.md) (3 shared connections)
- [Player Skill Repository](Player_Skill_Repository.md) (1 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)

## Source Files

- `server/game/room_service.py`

## Audit Trail

- EXTRACTED: 89 (70%)
- INFERRED: 38 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*