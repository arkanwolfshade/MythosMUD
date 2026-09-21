# RoomService

> 187 nodes

## Key Concepts

- **RoomService** (96 connections) — `server/game/room_service.py`
- **rooms.py** (61 connections) — `server/api/rooms.py`
- **test_rooms_write_api.py** (42 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **Direction** (41 connections) — `server/models/command_base.py`
- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **create_room_exit()** (20 connections) — `server/api/rooms.py`
- **update_room()** (20 connections) — `server/api/rooms.py`
- **update_room_exit()** (19 connections) — `server/api/rooms.py`
- **delete_room_exit()** (17 connections) — `server/api/rooms.py`
- **asyncio** (17 connections)
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **RoomUpdateRequest** (14 connections) — `server/schemas/rooms/room_write.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **_admin_user()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **_bypass_admin_auth()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **Any** (13 connections)
- **rooms/__init__.py** (13 connections) — `server/schemas/rooms/__init__.py`
- **_validate_admin_room_action()** (12 connections) — `server/api/rooms.py`
- **AsyncSession** (12 connections)
- **room_write.py** (12 connections) — `server/schemas/rooms/room_write.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **ExitCreateRequest** (11 connections) — `server/schemas/rooms/room_write.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (10 connections) — `server/api/rooms.py`
- *... and 162 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (24 shared connections)
- [ExplorationService](ExplorationService.md) (23 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (11 shared connections)
- [command.py](command.py.md) (11 shared connections)
- [test_command_exploration.py](test_command_exploration.py.md) (11 shared connections)
- [User](User.md) (11 shared connections)
- [PlayerService](PlayerService.md) (6 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (6 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (6 shared connections)
- [map_minimap.py](map_minimap.py.md) (5 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/models/command_base.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_write.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/api/test_rooms_write_api.py`
- `server/tests/unit/schemas/test_room_write.py`

## Audit Trail

- EXTRACTED: 523 (85%)
- INFERRED: 91 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*