# test_rooms_api.py

> 40 nodes

## Key Concepts

- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (9 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (9 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **asyncio** (8 connections)
- **RoomPositionUpdateResponse** (7 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (7 connections) — `server/schemas/rooms/room.py`
- **rooms/room.py** (7 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **RoomData** (6 connections) — `server/schemas/rooms/room_data.py`
- **test_update_room_position_room_missing()** (6 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_get_room_not_found()** (5 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_get_room_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_invalidate_room_cache()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_list_rooms_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_not_found()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_validate_room_position_update_requires_auth()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **room_data.py** (4 connections) — `server/schemas/rooms/room_data.py`
- **test_update_room_position_in_db_success()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **BaseModel** (3 connections)
- **test_validate_room_position_update_delegates_to_auth_service()** (2 connections) — `server/tests/unit/api/test_rooms_api.py`
- **get** (2 connections)
- *... and 15 more nodes in this community*

## Relationships

- [rooms.py](rooms.py.md) (27 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [RoomService](RoomService.md) (9 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [test_player_respawn_api.py](test_player_respawn_api.py.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (1 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_rooms_api.py`

## Audit Trail

- EXTRACTED: 113 (91%)
- INFERRED: 11 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*