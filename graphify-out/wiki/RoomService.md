# RoomService

> 240 nodes

## Key Concepts

- **RoomService** (96 connections) — `server/game/room_service.py`
- **rooms.py** (61 connections) — `server/api/rooms.py`
- **test_rooms_write_api.py** (42 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **Direction** (41 connections) — `server/models/command_base.py`
- **command_base.py** (27 connections) — `server/models/command_base.py`
- **room_service.py** (23 connections) — `server/game/room_service.py`
- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **create_room_exit()** (20 connections) — `server/api/rooms.py`
- **update_room()** (20 connections) — `server/api/rooms.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **update_room_exit()** (19 connections) — `server/api/rooms.py`
- **LookCommand** (18 connections) — `server/models/command_exploration.py`
- **delete_room_exit()** (17 connections) — `server/api/rooms.py`
- **asyncio** (17 connections)
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **RoomUpdateRequest** (14 connections) — `server/schemas/rooms/room_write.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **_admin_user()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **_bypass_admin_auth()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **Any** (13 connections)
- **rooms/__init__.py** (13 connections) — `server/schemas/rooms/__init__.py`
- **_validate_admin_room_action()** (12 connections) — `server/api/rooms.py`
- **AsyncSession** (12 connections)
- *... and 215 more nodes in this community*

## Relationships

- [ExplorationService](ExplorationService.md) (29 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (24 shared connections)
- [command.py](command.py.md) (21 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (11 shared connections)
- [User](User.md) (11 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (8 shared connections)
- [map_minimap.py](map_minimap.py.md) (7 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (7 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (7 shared connections)
- [BaseCommand](BaseCommand.md) (5 shared connections)
- [test_room_service.py](test_room_service.py.md) (4 shared connections)
- [HolidayService](HolidayService.md) (4 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/schemas/rooms/room_write.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/api/test_rooms_write_api.py`
- `server/tests/unit/models/test_command_exploration.py`
- `server/tests/unit/schemas/test_room_write.py`

## Audit Trail

- EXTRACTED: 638 (87%)
- INFERRED: 93 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*