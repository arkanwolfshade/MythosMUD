# map helpers rationale

> 87 nodes

## Key Concepts

- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_map_helpers.py** (15 connections) — `server/tests/unit/api/test_map_helpers.py`
- **map_helpers.py** (14 connections) — `server/api/map_helpers.py`
- **load_rooms_with_coordinates()** (14 connections) — `server/api/map_helpers.py`
- **load_single_room_with_coordinates()** (11 connections) — `server/api/map_helpers.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **load_room_exits()** (9 connections) — `server/api/map_helpers.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **build_room_dict()** (8 connections) — `server/api/map_helpers.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **TestApplyMinimapFallbackCoordinates** (8 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **build_zone_pattern()** (7 connections) — `server/api/map_helpers.py`
- **_MockResultRows** (7 connections) — `server/tests/unit/api/test_map_helpers.py`
- **TestAppendRoomWithFallbackCoordsIfNeeded** (7 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **TestBuildZonePattern** (5 connections) — `server/tests/unit/api/test_map_helpers.py`
- **Any** (4 connections)
- **Any** (4 connections)
- **TestBuildRoomDict** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_room_exits_attaches_exits_by_stable_id()** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_rooms_with_coordinates_executes_zone_query_and_exits()** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_single_room_with_coordinates_loads_exits()** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **AsyncSession** (3 connections)
- **AsyncSession** (3 connections)
- *... and 62 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (28 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [map services ascii](map_services_ascii.md) (2 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/tests/unit/api/test_map_helpers.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`

## Audit Trail

- EXTRACTED: 310 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*