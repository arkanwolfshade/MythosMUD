# RoomService

> 114 nodes

## Key Concepts

- **RoomService** (75 connections) — `server/game/room_service.py`
- **rooms.py** (37 connections) — `server/api/rooms.py`
- **room_service.py** (22 connections) — `server/game/room_service.py`
- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **Any** (13 connections)
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **.get_room()** (8 connections) — `server/game/room_service.py`
- **asyncio** (8 connections)
- **RoomPositionUpdateResponse** (7 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (7 connections) — `server/schemas/rooms/room.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **rooms/__init__.py** (7 connections) — `server/schemas/rooms/__init__.py`
- **rooms/room.py** (7 connections) — `server/schemas/rooms/room.py`
- *... and 89 more nodes in this community*

## Relationships

- [ExplorationService](ExplorationService.md) (16 shared connections)
- [maps.py](maps.py.md) (14 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (11 shared connections)
- [map_minimap.py](map_minimap.py.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (5 shared connections)
- [User](User.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [test_room_service.py](test_room_service.py.md) (4 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [players/player_respawn.py](players-player_respawn.py.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (3 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 296 (89%)
- INFERRED: 35 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*