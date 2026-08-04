# room game service

> 112 nodes

## Key Concepts

- **RoomService** (80 connections) — `server/game/room_service.py`
- **rooms.py** (36 connections) — `server/api/rooms.py`
- **room_service.py** (22 connections) — `server/game/room_service.py`
- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (12 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **.get_room()** (11 connections) — `server/game/room_service.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **Any** (10 connections)
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **room.py** (7 connections) — `server/schemas/rooms/room.py`
- **_invalidate_room_cache()** (6 connections) — `server/api/rooms.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- *... and 87 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (18 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (14 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (12 shared connections)
- [Exception Containers](Exception_Containers.md) (11 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [player requests schemas](player_requests_schemas.md) (7 shared connections)
- [player preferences services](player_preferences_services.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (5 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (4 shared connections)
- [room service game](room_service_game.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)

## Source Files

- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/rooms/__init__.py`
- `server/schemas/rooms/room.py`
- `server/schemas/rooms/room_data.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 482 (90%)
- INFERRED: 53 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*