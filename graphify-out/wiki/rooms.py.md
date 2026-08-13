# rooms.py

> 59 nodes

## Key Concepts

- **rooms.py** (35 connections) — `server/api/rooms.py`
- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (11 connections) — `server/api/rooms.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (7 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (7 connections) — `server/api/rooms.py`
- **rooms/room.py** (7 connections) — `server/schemas/rooms/room.py`
- **players/player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **rooms/__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **RoomDictList** (5 connections)
- **Request** (5 connections)
- **RoomPositionUpdate** (4 connections) — `server/api/rooms.py`
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- **_invalidate_room_cache()** (4 connections) — `server/api/rooms.py`
- **sample_rooms()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **AsyncSession** (4 connections)
- *... and 34 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (9 shared connections)
- [User](User.md) (8 shared connections)
- [RoomService](RoomService.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [ExplorationService](ExplorationService.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [players/__init__.py](players-__init__.py.md) (2 shared connections)
- [PostgresCursor](PostgresCursor.md) (1 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 143 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*