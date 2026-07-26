# map_minimap.py

> 65 nodes · cohesion 0.04

## Key Concepts

- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **test_ascii_map_renderer_exits.py** (9 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **ascii_map_renderer.py** (8 connections) — `server/services/ascii_map_renderer.py`
- **TestApplyMinimapFallbackCoordinates** (8 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **TestAppendRoomWithFallbackCoordsIfNeeded** (7 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **TestHorizontalExitCharBetween** (7 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **TestResolveExitTarget** (7 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **test_generate_minimap_html_admin_path()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_non_admin_filters_exploration()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **TestGetExitEntriesForRoom** (5 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **test_ascii_map_renderer_grid.py** (5 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **Any** (4 connections)
- **TestBuildGridPlayerMarker** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_grid.py`
- **AsyncSession** (3 connections)
- **test_ensure_current_room_in_minimap_appends_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_when_already_present()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_without_id()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_from_pre_filter_list()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_loads_when_not_in_list()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- *... and 40 more nodes in this community*

## Relationships

- [AsciiMapRenderer](AsciiMapRenderer.md) (24 shared connections)
- [ExplorationService](ExplorationService.md) (23 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/api/map_minimap.py`
- `server/services/ascii_map_renderer.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- `server/tests/unit/services/test_ascii_map_renderer_grid.py`

## Audit Trail

- EXTRACTED: 233 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*