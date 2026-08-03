# maps handle ascii

> 49 nodes

## Key Concepts

- **maps.py** (53 connections) — `server/api/maps.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (19 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (13 connections) — `server/api/maps.py`
- **get_ascii_map()** (12 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **_ensure_coords_stub()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **AsyncSession** (8 connections)
- **Request** (7 connections)
- **Any** (7 connections)
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **_get_minimap_player_and_room_id()** (7 connections) — `server/api/maps.py`
- **UUID** (6 connections)
- **_handle_ascii_map_error()** (6 connections) — `server/api/maps.py`
- **SetOriginRequest** (5 connections) — `server/api/maps.py`
- **UUID** (5 connections)
- **test_get_current_room_id_none_when_persistence_errors()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_player_and_exploration_returns_none_when_no_player()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **mock_user_and_player()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **_MapRooms** (3 connections)
- *... and 24 more nodes in this community*

## Relationships

- [corpse lifecycle service](corpse_lifecycle_service.md) (24 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (16 shared connections)
- [command handler processing](command_handler_processing.md) (14 shared connections)
- [room game service](room_game_service.md) (13 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (10 shared connections)
- [Database Config](Database_Config.md) (10 shared connections)
- [map helpers rationale](map_helpers_rationale.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [Exception Containers](Exception_Containers.md) (4 shared connections)
- [admin auth service](admin_auth_service.md) (3 shared connections)
- [map services ascii](map_services_ascii.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 300 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*