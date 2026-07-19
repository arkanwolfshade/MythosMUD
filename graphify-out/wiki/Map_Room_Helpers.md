# Map Room Helpers

> 58 nodes · cohesion 0.05

## Key Concepts

- **map_minimap.py** (20 connections) — `server/api/map_minimap.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **load_rooms_with_coordinates()** (14 connections) — `server/api/map_helpers.py`
- **test_map_helpers.py** (14 connections) — `server/tests/unit/api/test_map_helpers.py`
- **map_helpers.py** (11 connections) — `server/api/map_helpers.py`
- **load_single_room_with_coordinates()** (11 connections) — `server/api/map_helpers.py`
- **load_room_exits()** (9 connections) — `server/api/map_helpers.py`
- **build_room_dict()** (8 connections) — `server/api/map_helpers.py`
- **build_zone_pattern()** (7 connections) — `server/api/map_helpers.py`
- **_MockResultRows** (7 connections) — `server/tests/unit/api/test_map_helpers.py`
- **ascii_map_renderer.py** (6 connections) — `server/services/ascii_map_renderer.py`
- **TestBuildZonePattern** (5 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_room_exits_attaches_exits_by_stable_id()** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_rooms_with_coordinates_executes_zone_query_and_exits()** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_single_room_with_coordinates_loads_exits()** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **TestBuildRoomDict** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_generate_minimap_html_admin_path()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_non_admin_filters_exploration()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **Any** (4 connections) — `server/api/map_helpers.py`
- **test_load_room_exits_no_rooms_no_query()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_single_room_with_coordinates_none_when_missing()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **.test_full_row()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **.test_null_map_coords()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **.test_empty_sub_zone_treated_as_none()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **.test_plane_zone_only()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- *... and 33 more nodes in this community*

## Relationships

- [[ASCII Map API]] (16 shared connections)
- [[Minimap Fallback Helpers]] (11 shared connections)
- [[NPC Admin API]] (8 shared connections)
- [[ASCII Map Renderer]] (3 shared connections)
- [[Maps API Endpoints]] (1 shared connections)
- [[Services Exploration Service]] (1 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/services/ascii_map_renderer.py`
- `server/tests/unit/api/test_map_helpers.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`

## Audit Trail

- EXTRACTED: 211 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
