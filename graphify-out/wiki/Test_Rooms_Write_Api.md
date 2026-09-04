# Test Rooms Write Api

> 90 nodes

## Key Concepts

- **test_rooms_write_api.py** (44 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **Direction** (37 connections) — `server/models/command_base.py`
- **create_room_exit()** (20 connections) — `server/api/rooms.py`
- **update_room()** (19 connections) — `server/api/rooms.py`
- **update_room_exit()** (19 connections) — `server/api/rooms.py`
- **delete_room_exit()** (17 connections) — `server/api/rooms.py`
- **asyncio** (17 connections)
- **_admin_user()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **_bypass_admin_auth()** (13 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **rooms/__init__.py** (13 connections) — `server/schemas/rooms/__init__.py`
- **RoomUpdateRequest** (12 connections) — `server/schemas/rooms/room_write.py`
- **_validate_admin_room_action()** (12 connections) — `server/api/rooms.py`
- **AsyncSession** (12 connections)
- **room_write.py** (12 connections) — `server/schemas/rooms/room_write.py`
- **RoomService** (11 connections)
- **test_room_write.py** (11 connections) — `server/tests/unit/schemas/test_room_write.py`
- **ExitCreateRequest** (10 connections) — `server/schemas/rooms/room_write.py`
- **test_create_room_exit_duplicate_direction_409()** (10 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **Request** (10 connections)
- **test_create_room_exit_source_room_missing_404()** (9 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **test_create_room_exit_target_room_missing_404()** (9 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **test_update_room_exit_not_found_404()** (9 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **User** (9 connections)
- **ExitUpdateRequest** (8 connections) — `server/schemas/rooms/room_write.py`
- **_apply_room_exit_to_memory()** (8 connections) — `server/api/rooms.py`
- *... and 65 more nodes in this community*

## Relationships

- [Rooms](Rooms.md) (40 shared connections)
- [Room Service](Room_Service.md) (15 shared connections)
- [Test Command Exploration](Test_Command_Exploration.md) (11 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (8 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (8 shared connections)
- [Command Aliases](Command_Aliases.md) (7 shared connections)
- [Test Command Admin](Test_Command_Admin.md) (5 shared connections)
- [Test Command Base](Test_Command_Base.md) (5 shared connections)
- [Players](Players.md) (5 shared connections)
- [Room](Room.md) (4 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (3 shared connections)
- [Npc Admin](Npc_Admin.md) (2 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room_write.py`
- `server/tests/unit/api/test_rooms_write_api.py`
- `server/tests/unit/schemas/test_room_write.py`

## Audit Trail

- EXTRACTED: 277 (81%)
- INFERRED: 63 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*