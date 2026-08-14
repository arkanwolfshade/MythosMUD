# MapZoneContext

> 60 nodes

## Key Concepts

- **MapZoneContext** (23 connections) — `server/api/map_helpers.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **_build_ascii_map_response()** (9 connections) — `server/api/maps.py`
- **_build_ascii_minimap_response()** (9 connections) — `server/api/maps.py`
- **TestApplyMinimapFallbackCoordinates** (8 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **_MapEndpointDeps** (7 connections) — `server/api/maps.py`
- **TestAppendRoomWithFallbackCoordsIfNeeded** (7 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **asyncio** (7 connections)
- **test_generate_minimap_html_admin_path()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_non_admin_filters_exploration()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **_AsciiMapViewport** (4 connections) — `server/api/maps.py`
- **test_ensure_current_room_in_minimap_appends_missing()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_when_already_present()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_without_id()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_from_pre_filter_list()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_loads_when_not_in_list()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **Any** (4 connections)
- **.test_appends_copy_with_fallback_0_0_when_coords_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_fallback_when_only_one_coord_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- *... and 35 more nodes in this community*

## Relationships

- [test_maps.py](test_maps.py.md) (15 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (7 shared connections)
- [RoomService](RoomService.md) (5 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (4 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)
- [maps/__init__.py](maps-__init__.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`

## Audit Trail

- EXTRACTED: 144 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*