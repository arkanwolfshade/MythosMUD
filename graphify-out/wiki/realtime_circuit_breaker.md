# realtime circuit breaker

> 46 nodes

## Key Concepts

- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **list_rooms()** (12 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **room.py** (7 connections) — `server/schemas/rooms/room.py`
- **_invalidate_room_cache()** (6 connections) — `server/api/rooms.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **Request** (5 connections)
- **test_update_room_position_room_missing()** (5 connections) — `server/tests/unit/api/test_rooms_api.py`
- **AsyncSession** (4 connections)
- **room_data.py** (4 connections) — `server/schemas/rooms/room_data.py`
- **test_get_room_not_found()** (4 connections) — `server/tests/unit/api/test_rooms_api.py`
- **BaseModel** (3 connections)
- **test_validate_room_position_update_requires_auth()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_update_room_position_in_db_not_found()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_invalidate_room_cache()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_list_rooms_success()** (3 connections) — `server/tests/unit/api/test_rooms_api.py`
- *... and 21 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (25 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (10 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (6 shared connections)
- [player requests schemas](player_requests_schemas.md) (3 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (2 shared connections)
- [postgres adapter infrastructure](postgres_adapter_infrastructure.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_rooms_api.py`

## Audit Trail

- EXTRACTED: 189 (92%)
- INFERRED: 16 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*