# maps handle ascii

> 83 nodes

## Key Concepts

- **RoomService** (80 connections) — `server/game/room_service.py`
- **ExplorationService** (79 connections) — `server/services/exploration_service.py`
- **maps.py** (53 connections) — `server/api/maps.py`
- **test_maps.py** (52 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (20 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **get_ascii_map()** (14 connections) — `server/api/maps.py`
- **set_map_origin()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (13 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **_ensure_coords_stub()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **AsyncSession** (8 connections)
- **_handle_ascii_map_error()** (8 connections) — `server/api/maps.py`
- **SetOriginRequest** (8 connections) — `server/api/maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **Request** (7 connections)
- **Any** (7 connections)
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **AsciiMapResponse** (7 connections) — `server/schemas/maps/map.py`
- *... and 58 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (36 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (36 shared connections)
- [room game service](room_game_service.md) (32 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (19 shared connections)
- [player realtime presence](player_realtime_presence.md) (16 shared connections)
- [command handler processing](command_handler_processing.md) (9 shared connections)
- [admin auth service](admin_auth_service.md) (8 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [player service game](player_service_game.md) (7 shared connections)
- [combat services service](combat_services_service.md) (7 shared connections)
- [map helpers rationale](map_helpers_rationale.md) (6 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (5 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/game/room_service.py`
- `server/schemas/maps/map.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 552 (86%)
- INFERRED: 87 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*