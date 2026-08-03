# maps handle ascii

> 90 nodes

## Key Concepts

- **RoomService** (70 connections) — `server/game/room_service.py`
- **maps.py** (53 connections) — `server/api/maps.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (19 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (13 connections) — `server/api/maps.py`
- **get_ascii_map()** (12 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **set_map_origin()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (10 connections) — `server/api/maps.py`
- **__init__.py** (10 connections) — `server/schemas/maps/__init__.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **map.py** (9 connections) — `server/schemas/maps/map.py`
- **_ensure_coords_stub()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **AsyncSession** (8 connections)
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **Request** (7 connections)
- **Any** (7 connections)
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **_get_minimap_player_and_room_id()** (7 connections) — `server/api/maps.py`
- **BaseModel** (7 connections)
- **AsciiMapResponse** (7 connections) — `server/schemas/maps/map.py`
- *... and 65 more nodes in this community*

## Relationships

- [database helpers infrastructure](database_helpers_infrastructure.md) (25 shared connections)
- [auth users rationale](auth_users_rationale.md) (22 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (16 shared connections)
- [room game service](room_game_service.md) (16 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (8 shared connections)
- [npc populate databases](npc_populate_databases.md) (7 shared connections)
- [map helpers rationale](map_helpers_rationale.md) (6 shared connections)
- [Exception Containers](Exception_Containers.md) (6 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (6 shared connections)
- [admin auth service](admin_auth_service.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (5 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/game/room_service.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/coordinate_validator.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 495 (91%)
- INFERRED: 47 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*