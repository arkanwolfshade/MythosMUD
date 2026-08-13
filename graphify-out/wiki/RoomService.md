# RoomService

> 47 nodes

## Key Concepts

- **RoomService** (61 connections) — `server/game/room_service.py`
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

- [server/dependencies.py](server-dependencies.py.md) (8 shared connections)
- [rooms.py](rooms.py.md) (6 shared connections)
- [map_minimap.py](map_minimap.py.md) (5 shared connections)
- [test_maps.py](test_maps.py.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [maps.py](maps.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [HealthService](HealthService.md) (1 shared connections)
- [fixture](fixture.md) (1 shared connections)
- [test_room_service.py](test_room_service.py.md) (1 shared connections)

## Source Files

- `server/game/room_service.py`

## Audit Trail

- EXTRACTED: 101 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*