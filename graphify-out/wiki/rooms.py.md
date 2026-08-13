# rooms.py

> 59 nodes

## Key Concepts

- **rooms.py** (35 connections) — `server/api/rooms.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **list_rooms()** (11 connections) — `server/api/rooms.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **rooms/room.py** (7 connections) — `server/schemas/rooms/room.py`
- **players/player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **rooms/__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (5 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **RoomDictList** (5 connections)
- **RoomPositionUpdate** (4 connections) — `server/api/rooms.py`
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- **_invalidate_room_cache()** (4 connections) — `server/api/rooms.py`
- **sample_rooms()** (4 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **AsyncSession** (4 connections)
- *... and 34 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (16 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (13 shared connections)
- [RoomService](RoomService.md) (8 shared connections)
- [ExplorationService](ExplorationService.md) (8 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (5 shared connections)
- [maps.py](maps.py.md) (4 shared connections)
- [players/__init__.py](players-__init__.py.md) (3 shared connections)
- [test_player_respawn_handlers.py](test_player_respawn_handlers.py.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [.get_instance](get_instance.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 170 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*