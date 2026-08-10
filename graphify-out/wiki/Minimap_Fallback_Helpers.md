# Minimap Fallback Helpers

> 52 nodes

## Key Concepts

- **MapZoneContext** (22 connections) — `server/api/map_helpers.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
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
- **test_resolve_current_room_loads_when_not_in_list()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_without_id()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_when_already_present()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- *... and 27 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (23 shared connections)
- [Map Room Helpers](Map_Room_Helpers.md) (7 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (7 shared connections)
- [ASCII Map Renderer](ASCII_Map_Renderer.md) (2 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`

## Audit Trail

- EXTRACTED: 199 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*