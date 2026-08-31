# RoomService

> 143 nodes

## Key Concepts

- **RoomService** (96 connections) — `server/game/room_service.py`
- **rooms.py** (61 connections) — `server/api/rooms.py`
- **test_rooms_write_api.py** (44 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **test_rooms_api.py** (24 connections) — `server/tests/unit/api/test_rooms_api.py`
- **create_room_exit()** (20 connections) — `server/api/rooms.py`
- **update_room()** (19 connections) — `server/api/rooms.py`
- **update_room_exit()** (19 connections) — `server/api/rooms.py`
- **delete_room_exit()** (17 connections) — `server/api/rooms.py`
- **asyncio** (17 connections)
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **_admin_user()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **_bypass_admin_auth()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **rooms/__init__.py** (13 connections) — `server/schemas/rooms/__init__.py`
- **test_rooms_exploration_filter.py** (13 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_validate_admin_room_action()** (12 connections) — `server/api/rooms.py`
- **AsyncSession** (12 connections)
- **RoomUpdateRequest** (11 connections) — `server/schemas/rooms/room_write.py`
- **ExitCreateRequest** (10 connections) — `server/schemas/rooms/room_write.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (10 connections) — `server/api/rooms.py`
- **test_create_room_exit_duplicate_direction_409()** (10 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **Request** (10 connections)
- **room_write.py** (10 connections) — `server/schemas/rooms/room_write.py`
- *... and 118 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (40 shared connections)
- [BaseCommand](BaseCommand.md) (19 shared connections)
- [get_logger](get_logger.md) (18 shared connections)
- [Any](Any.md) (18 shared connections)
- [maps.py](maps.py.md) (15 shared connections)
- [ExplorationService](ExplorationService.md) (8 shared connections)
- [map_minimap.py](map_minimap.py.md) (5 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (4 shared connections)
- [RoomData](RoomData.md) (3 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_write.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/api/test_rooms_write_api.py`

## Audit Trail

- EXTRACTED: 457 (86%)
- INFERRED: 74 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*