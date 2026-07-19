# Minimap Fallback Helpers

> 40 nodes · cohesion 0.07

## Key Concepts

- **test_map_minimap_helpers.py** (17 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **TestApplyMinimapFallbackCoordinates** (8 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **TestAppendRoomWithFallbackCoordsIfNeeded** (7 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **Any** (5 connections) — `server/api/map_minimap.py`
- **AsyncSession** (4 connections) — `server/api/map_minimap.py`
- **test_ensure_current_room_in_minimap_appends_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_when_already_present()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_without_id()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_from_pre_filter_list()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_loads_when_not_in_list()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_copy_with_fallback_0_0_when_coords_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_fallback_when_only_one_coord_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_room_unchanged_when_has_coords()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_admin_gets_grid_layout_for_rooms_without_coords()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_fallback_grid_wraps_by_fallback_grid_width()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_non_admin_gets_fallback_only_for_current_room()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_non_admin_uses_stable_id_for_current_room_match()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **Get current room from pre-filter list or load by stable_id. Returns None if not** (1 connections) — `server/api/map_minimap.py`
- **Append room to list; use fallback map_x/map_y=0 if room has None coords. Mutates** (1 connections) — `server/api/map_minimap.py`
- **If current_room_id is missing from rooms, re-add it from rooms_before_filter or** (1 connections) — `server/api/map_minimap.py`
- **Set fallback map_x/map_y for rooms that have None. Admins get a grid layout;** (1 connections) — `server/api/map_minimap.py`
- *... and 15 more nodes in this community*

## Relationships

- [[Map Room Helpers]] (11 shared connections)
- [[ASCII Map API]] (5 shared connections)
- [[Maps API Endpoints]] (3 shared connections)

## Source Files

- `server/api/map_minimap.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`

## Audit Trail

- EXTRACTED: 127 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
