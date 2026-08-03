# database helpers infrastructure

> 51 nodes

## Key Concepts

- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **TestApplyMinimapFallbackCoordinates** (8 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_admin_path()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **Any** (4 connections)
- **AsyncSession** (3 connections)
- **.test_appends_room_unchanged_when_has_coords()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_copy_with_fallback_0_0_when_coords_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_fallback_when_only_one_coord_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_admin_gets_grid_layout_for_rooms_without_coords()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_fallback_grid_wraps_by_fallback_grid_width()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_non_admin_gets_fallback_only_for_current_room()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_non_admin_uses_stable_id_for_current_room_match()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_from_pre_filter_list()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_loads_when_not_in_list()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_without_id()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_when_already_present()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- *... and 26 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (25 shared connections)
- [NATS Messaging](NATS_Messaging.md) (10 shared connections)
- [map helpers rationale](map_helpers_rationale.md) (6 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (6 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (6 shared connections)
- [map services ascii](map_services_ascii.md) (3 shared connections)
- [respawn player handlers](respawn_player_handlers.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [cache caching service](cache_caching_service.md) (1 shared connections)
- [room game service](room_game_service.md) (1 shared connections)
- [room service game](room_service_game.md) (1 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)

## Source Files

- `server/api/map_minimap.py`
- `server/game/room_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 222 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*