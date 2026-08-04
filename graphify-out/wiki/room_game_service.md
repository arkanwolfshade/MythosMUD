# room game service

> 97 nodes

## Key Concepts

- **RoomService** (80 connections) — `server/game/room_service.py`
- **rooms.py** (36 connections) — `server/api/rooms.py`
- **room_service.py** (22 connections) — `server/game/room_service.py`
- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (12 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **room.py** (7 connections) — `server/schemas/rooms/room.py`
- **TestGetPlayerService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetPlayerServiceForTesting** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetRoomService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetStatsGenerator** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **_invalidate_room_cache()** (6 connections) — `server/api/rooms.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- *... and 72 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (28 shared connections)
- [player realtime presence](player_realtime_presence.md) (17 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (16 shared connections)
- [Loot Generation](Loot_Generation.md) (12 shared connections)
- [Exception Containers](Exception_Containers.md) (11 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (9 shared connections)
- [player service game](player_service_game.md) (9 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (9 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (8 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (6 shared connections)
- [player requests schemas](player_requests_schemas.md) (6 shared connections)
- [room service game](room_service_game.md) (4 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 431 (86%)
- INFERRED: 69 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*