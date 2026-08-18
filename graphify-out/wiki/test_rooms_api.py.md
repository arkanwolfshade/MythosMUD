# test_rooms_api.py

> 31 nodes

## Key Concepts

- **test_rooms_api.py** (24 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **asyncio** (8 connections)
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (6 connections) — `server/api/rooms.py`
- **test_update_room_position_room_missing()** (6 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_get_room_not_found()** (5 connections) — `server/tests/unit/api/test_rooms_api.py`
- **Request** (5 connections)
- **test_get_room_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_invalidate_room_cache()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_list_rooms_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_not_found()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_validate_room_position_update_requires_auth()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **AsyncSession** (4 connections)
- **test_update_room_position_in_db_success()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_validate_room_position_update_delegates_to_auth_service()** (2 connections) — `server/tests/unit/api/test_rooms_api.py`
- **get** (2 connections)
- **BaseModel** (1 connections)
- **post** (1 connections)
- **Update room position in database and verify the update succeeded.** (1 connections) — `server/api/rooms.py`
- **Invalidate room cache to force reload.** (1 connections) — `server/api/rooms.py`
- *... and 6 more nodes in this community*

## Relationships

- [RoomService](RoomService.md) (12 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (9 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (3 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (1 shared connections)
- [PostgresCursor](PostgresCursor.md) (1 shared connections)
- [room_service.py](room_service.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/tests/unit/api/test_rooms_api.py`

## Audit Trail

- EXTRACTED: 91 (89%)
- INFERRED: 11 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*