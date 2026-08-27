# map_minimap.py

> 97 nodes

## Key Concepts

- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (21 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **test_map_helpers.py** (16 connections) — `server/tests/unit/api/test_map_helpers.py`
- **map_helpers.py** (15 connections) — `server/api/map_helpers.py`
- **load_rooms_with_coordinates()** (14 connections) — `server/api/map_helpers.py`
- **load_single_room_with_coordinates()** (11 connections) — `server/api/map_helpers.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **load_room_exits()** (9 connections) — `server/api/map_helpers.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **ascii_map_renderer.py** (9 connections) — `server/services/ascii_map_renderer.py`
- **build_room_dict()** (8 connections) — `server/api/map_helpers.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **_MockResultRows** (7 connections) — `server/tests/unit/api/test_map_helpers.py`
- **build_zone_pattern()** (7 connections) — `server/api/map_helpers.py`
- **asyncio** (7 connections)
- **TestApplyMinimapFallbackCoordinates** (6 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_admin_path()** (6 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_non_admin_filters_exploration()** (6 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **TestBuildZonePattern** (5 connections) — `server/tests/unit/api/test_map_helpers.py`
- **TestAppendRoomWithFallbackCoordsIfNeeded** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_load_room_exits_attaches_exits_by_stable_id()** (5 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_rooms_with_coordinates_executes_zone_query_and_exits()** (5 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_single_room_with_coordinates_loads_exits()** (5 connections) — `server/tests/unit/api/test_map_helpers.py`
- *... and 72 more nodes in this community*

## Relationships

- [User](User.md) (17 shared connections)
- [RoomService](RoomService.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (3 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [test_ascii_map_renderer_exits.py](test_ascii_map_renderer_exits.py.md) (1 shared connections)
- [test_ascii_map_renderer_grid.py](test_ascii_map_renderer_grid.py.md) (1 shared connections)
- [._get_vertical_exit_char](_get_vertical_exit_char.md) (1 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/services/ascii_map_renderer.py`
- `server/tests/unit/api/test_map_helpers.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`

## Audit Trail

- EXTRACTED: 203 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*