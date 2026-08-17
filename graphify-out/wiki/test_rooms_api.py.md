# test_rooms_api.py

> 52 nodes

## Key Concepts

- **test_rooms_api.py** (24 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **rooms/room.py** (8 connections) — `server/schemas/rooms/room.py`
- **asyncio** (8 connections)
- **RoomPositionUpdateResponse** (7 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (7 connections) — `server/schemas/rooms/room.py`
- **players/player_respawn.py** (7 connections) — `server/schemas/players/player_respawn.py`
- **rooms/__init__.py** (7 connections) — `server/schemas/rooms/__init__.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **RoomData** (6 connections) — `server/schemas/rooms/room_data.py`
- **_invalidate_room_cache()** (6 connections) — `server/api/rooms.py`
- **test_update_room_position_room_missing()** (6 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_get_room_not_found()** (5 connections) — `server/tests/unit/api/test_rooms_api.py`
- **Request** (5 connections)
- **room_data.py** (5 connections) — `server/schemas/rooms/room_data.py`
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- **test_get_room_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_invalidate_room_cache()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_list_rooms_success()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_not_found()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- *... and 27 more nodes in this community*

## Relationships

- [User](User.md) (16 shared connections)
- [ExplorationService](ExplorationService.md) (14 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [BaseCommand](BaseCommand.md) (3 shared connections)
- [players/__init__.py](players-__init__.py.md) (2 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (2 shared connections)
- [PostgresCursor](PostgresCursor.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_rooms_api.py`

## Audit Trail

- EXTRACTED: 133 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*