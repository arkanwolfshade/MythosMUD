# room game service

> 67 nodes

## Key Concepts

- **rooms.py** (36 connections) — `server/api/rooms.py`
- **room_service.py** (22 connections) — `server/game/room_service.py`
- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
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
- **_invalidate_room_cache()** (6 connections) — `server/api/rooms.py`
- **RoomPositionUpdate** (6 connections) — `server/api/rooms.py`
- **__init__.py** (6 connections) — `server/schemas/rooms/__init__.py`
- **test_apply_exploration_filter_superuser_bypasses_filter()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_non_admin_uses_room_service_intersection()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **test_apply_exploration_filter_no_player_returns_unfiltered()** (6 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **Request** (5 connections)
- **test_update_room_position_room_missing()** (5 connections) — `server/tests/unit/api/test_rooms_api.py`
- *... and 42 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (32 shared connections)
- [Exception Containers](Exception_Containers.md) (16 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [admin auth service](admin_auth_service.md) (7 shared connections)
- [profession game service](profession_game_service.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (3 shared connections)
- [combat npc services](combat_npc_services.md) (2 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [postgres adapter infrastructure](postgres_adapter_infrastructure.md) (1 shared connections)

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

- EXTRACTED: 317 (93%)
- INFERRED: 24 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*