# player respawn

> 79 nodes

## Key Concepts

- **rooms.py** (35 connections) — `server/api/rooms.py`
- **player_respawn.py** (24 connections) — `server/api/player_respawn.py`
- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **test_player_respawn_handlers.py** (14 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **list_rooms()** (10 connections) — `server/api/rooms.py`
- **respawn_player_from_delirium()** (9 connections) — `server/api/player_respawn.py`
- **respawn_player()** (9 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (8 connections) — `server/schemas/players/player_respawn.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **_validate_room_position_update()** (7 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (7 connections) — `server/api/rooms.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **room.py** (7 connections) — `server/schemas/rooms/room.py`
- **player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- *... and 54 more nodes in this community*

## Relationships

- [APIRouter](APIRouter.md) (31 shared connections)
- [AsyncSession](AsyncSession.md) (19 shared connections)
- [main()](main%28%29.md) (18 shared connections)
- [. init ()](_init_%28%29.md) (13 shared connections)
- [Request](Request.md) (10 shared connections)
- [Connection Manager](Connection_Manager.md) (5 shared connections)
- [BaseUserManager](BaseUserManager.md) (3 shared connections)
- [character creation](character_creation.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [init](init.md) (1 shared connections)
- [.mock cursor()](mock_cursor%28%29.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/api/rooms.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 366 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*