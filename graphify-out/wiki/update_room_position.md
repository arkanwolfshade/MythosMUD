# update_room_position

> 49 nodes

## Key Concepts

- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (11 connections) — `server/api/rooms.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (7 connections) — `server/api/rooms.py`
- **rooms/room.py** (7 connections) — `server/schemas/rooms/room.py`
- **rooms/__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **RoomDictList** (5 connections)
- **Request** (5 connections)
- **RoomPositionUpdate** (4 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (4 connections) — `server/api/rooms.py`
- **sample_rooms()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **AsyncSession** (4 connections)
- **room_data.py** (4 connections) — `server/schemas/rooms/room_data.py`
- **asyncio** (4 connections)
- **BaseModel** (3 connections)
- **get** (2 connections)
- *... and 24 more nodes in this community*

## Relationships

- [database.py](database.py.md) (13 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [RoomService](RoomService.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (4 shared connections)
- [User](User.md) (3 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)
- [PostgresCursor](PostgresCursor.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 173 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*