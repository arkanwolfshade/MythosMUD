# room game service

> 104 nodes

## Key Concepts

- **RoomService** (70 connections) — `server/game/room_service.py`
- **rooms.py** (35 connections) — `server/api/rooms.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **update_room_position()** (14 connections) — `server/api/rooms.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **.get_room()** (11 connections) — `server/game/room_service.py`
- **list_rooms()** (10 connections) — `server/api/rooms.py`
- **Any** (10 connections)
- **RoomListResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomPositionUpdateResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomResponse** (8 connections) — `server/schemas/rooms/room.py`
- **RoomData** (8 connections) — `server/schemas/rooms/room_data.py`
- **_validate_room_position_update()** (7 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (7 connections) — `server/api/rooms.py`
- **get_room()** (7 connections) — `server/api/rooms.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **room.py** (7 connections) — `server/schemas/rooms/room.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **player_respawn.py** (6 connections) — `server/schemas/players/player_respawn.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- *... and 79 more nodes in this community*

## Relationships

- [corpse lifecycle service](corpse_lifecycle_service.md) (15 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (13 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (10 shared connections)
- [command inventory factories](command_inventory_factories.md) (9 shared connections)
- [admin auth service](admin_auth_service.md) (9 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (7 shared connections)
- [Exception Containers](Exception_Containers.md) (6 shared connections)
- [Database Config](Database_Config.md) (5 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (5 shared connections)
- [time service rationale](time_service_rationale.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [room service game](room_service_game.md) (3 shared connections)

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

- EXTRACTED: 427 (92%)
- INFERRED: 35 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*