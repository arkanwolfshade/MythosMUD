# RoomService

> 120 nodes

## Key Concepts

- **RoomService** (96 connections) — `server/game/room_service.py`
- **rooms.py** (61 connections) — `server/api/rooms.py`
- **room_service.py** (24 connections) — `server/game/room_service.py`
- **test_rooms_api.py** (24 connections) — `server/tests/unit/api/test_rooms_api.py`
- **exploration_service.py** (18 connections) — `server/services/exploration_service.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **Any** (13 connections)
- **rooms/__init__.py** (13 connections) — `server/schemas/rooms/__init__.py`
- **test_rooms_exploration_filter.py** (13 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_validate_admin_room_action()** (12 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_invalidate_room_cache()** (10 connections) — `server/api/rooms.py`
- **Request** (10 connections)
- **_update_room_position_in_db()** (9 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (9 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **.get_room()** (8 connections) — `server/game/room_service.py`
- **rooms/room.py** (8 connections) — `server/schemas/rooms/room.py`
- **asyncio** (8 connections)
- **RoomPositionUpdateResponse** (7 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (7 connections) — `server/schemas/rooms/room.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (7 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- *... and 95 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (67 shared connections)
- [User](User.md) (37 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (22 shared connections)
- [DatabaseError](DatabaseError.md) (9 shared connections)
- [map_minimap.py](map_minimap.py.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_room_service.py](test_room_service.py.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [time_event_consumer.py](time_event_consumer.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (2 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 366 (88%)
- INFERRED: 48 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*