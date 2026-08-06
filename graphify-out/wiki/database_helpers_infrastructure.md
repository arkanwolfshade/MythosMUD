# database helpers infrastructure

> 58 nodes

## Key Concepts

- **room_service.py** (22 connections) — `server/game/room_service.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **MapZoneContext** (20 connections) — `server/api/map_helpers.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **TestApplyMinimapFallbackCoordinates** (8 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **TestAppendRoomWithFallbackCoordsIfNeeded** (7 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_admin_path()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_non_admin_filters_exploration()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
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
- *... and 33 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (20 shared connections)
- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (8 shared connections)
- [map helpers rationale](map_helpers_rationale.md) (7 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (7 shared connections)
- [panels monitoringPanelTestFixtures Monit](panels_monitoringPanelTestFixtures_Monit.md) (6 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [map services ascii](map_services_ascii.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [room cache services](room_cache_services.md) (1 shared connections)
- [player event handlers](player_event_handlers.md) (1 shared connections)
- [startup npc service](startup_npc_service.md) (1 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/game/room_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 253 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*