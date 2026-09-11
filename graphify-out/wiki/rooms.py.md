# rooms.py

> 153 nodes

## Key Concepts

- **rooms.py** (60 connections) — `server/api/rooms.py`
- **test_rooms_write_api.py** (42 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **Direction** (41 connections) — `server/models/command_base.py`
- **command_base.py** (26 connections) — `server/models/command_base.py`
- **create_room_exit()** (20 connections) — `server/api/rooms.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **update_room()** (19 connections) — `server/api/rooms.py`
- **update_room_exit()** (19 connections) — `server/api/rooms.py`
- **LookCommand** (18 connections) — `server/models/command_exploration.py`
- **delete_room_exit()** (17 connections) — `server/api/rooms.py`
- **asyncio** (17 connections)
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **RoomUpdateRequest** (13 connections) — `server/schemas/rooms/room_write.py`
- **_admin_user()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **_bypass_admin_auth()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **rooms/__init__.py** (13 connections) — `server/schemas/rooms/__init__.py`
- **_validate_admin_room_action()** (12 connections) — `server/api/rooms.py`
- **AsyncSession** (12 connections)
- **room_write.py** (12 connections) — `server/schemas/rooms/room_write.py`
- **ExitCreateRequest** (11 connections) — `server/schemas/rooms/room_write.py`
- **_invalidate_room_cache()** (10 connections) — `server/api/rooms.py`
- **test_create_room_exit_duplicate_direction_409()** (10 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **Request** (10 connections)
- **ExitUpdateRequest** (9 connections) — `server/schemas/rooms/room_write.py`
- *... and 128 more nodes in this community*

## Relationships

- [RoomService](RoomService.md) (52 shared connections)
- [command.py](command.py.md) (24 shared connections)
- [PlayerService](PlayerService.md) (23 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [User](User.md) (11 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [BaseCommand](BaseCommand.md) (4 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (3 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (1 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/schemas/rooms/room_write.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_write_api.py`
- `server/tests/unit/models/test_command_exploration.py`
- `server/tests/unit/schemas/test_room_write.py`

## Audit Trail

- EXTRACTED: 448 (88%)
- INFERRED: 60 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*