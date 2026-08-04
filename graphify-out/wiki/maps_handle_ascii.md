# maps handle ascii

> 65 nodes

## Key Concepts

- **maps.py** (53 connections) — `server/api/maps.py`
- **test_maps.py** (52 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (20 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (16 connections) — `server/api/maps.py`
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
- **UUID** (6 connections)
- **UUID** (6 connections)
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (6 connections) — `server/tests/unit/api/test_maps.py`
- *... and 40 more nodes in this community*

## Relationships

- [corpse lifecycle service](corpse_lifecycle_service.md) (25 shared connections)
- [player requests schemas](player_requests_schemas.md) (25 shared connections)
- [room game service](room_game_service.md) (18 shared connections)
- [Exception Containers](Exception_Containers.md) (10 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (9 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [command handler processing](command_handler_processing.md) (7 shared connections)
- [map helpers rationale](map_helpers_rationale.md) (6 shared connections)
- [player preferences services](player_preferences_services.md) (5 shared connections)
- [coordinate services generator](coordinate_services_generator.md) (5 shared connections)
- [room cache services](room_cache_services.md) (4 shared connections)
- [map services ascii](map_services_ascii.md) (3 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 391 (91%)
- INFERRED: 37 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*