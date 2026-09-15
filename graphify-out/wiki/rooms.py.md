# rooms.py

> 83 nodes

## Key Concepts

- **rooms.py** (60 connections) — `server/api/rooms.py`
- **test_rooms_write_api.py** (42 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **create_room_exit()** (20 connections) — `server/api/rooms.py`
- **update_room()** (19 connections) — `server/api/rooms.py`
- **update_room_exit()** (19 connections) — `server/api/rooms.py`
- **delete_room_exit()** (17 connections) — `server/api/rooms.py`
- **asyncio** (17 connections)
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
- **test_create_room_exit_source_room_missing_404()** (9 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **test_create_room_exit_target_room_missing_404()** (9 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **test_update_room_exit_not_found_404()** (9 connections) — `server/tests/unit/api/test_rooms_write_api.py`
- **test_room_write.py** (9 connections) — `server/tests/unit/schemas/test_room_write.py`
- **ExitResponse** (8 connections) — `server/schemas/rooms/room_write.py`
- **_apply_room_exit_to_memory()** (8 connections) — `server/api/rooms.py`
- *... and 58 more nodes in this community*

## Relationships

- [test_rooms_api.py](test_rooms_api.py.md) (27 shared connections)
- [RoomService](RoomService.md) (23 shared connections)
- [BaseCommand](BaseCommand.md) (16 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (15 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (9 shared connections)
- [User](User.md) (7 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (5 shared connections)
- [ExplorationService](ExplorationService.md) (4 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room_write.py`
- `server/tests/unit/api/test_rooms_write_api.py`
- `server/tests/unit/schemas/test_room_write.py`

## Audit Trail

- EXTRACTED: 299 (88%)
- INFERRED: 41 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*