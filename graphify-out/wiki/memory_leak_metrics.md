# memory leak metrics

> 54 nodes

## Key Concepts

- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **list_rooms()** (10 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **_validate_room_position_update()** (7 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (7 connections) — `server/api/rooms.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **room.py** (7 connections) — `server/schemas/rooms/room.py`
- **player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Request** (5 connections)
- **RoomDictList** (5 connections)
- **AsyncSession** (4 connections)
- **_invalidate_room_cache()** (4 connections) — `server/api/rooms.py`
- **RoomPositionUpdate** (4 connections) — `server/api/rooms.py`
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- **room_data.py** (4 connections) — `server/schemas/rooms/room_data.py`
- *... and 29 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (18 shared connections)
- [ExitStack](ExitStack.md) (17 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (5 shared connections)
- [Connection Manager](Connection_Manager.md) (4 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (2 shared connections)
- [command processor()](command_processor%28%29.md) (2 shared connections)
- [.mock cursor()](mock_cursor%28%29.md) (1 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 194 (93%)
- INFERRED: 15 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*