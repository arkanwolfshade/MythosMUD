# map helpers rationale

> 44 nodes

## Key Concepts

- **test_map_helpers.py** (15 connections) — `server/tests/unit/api/test_map_helpers.py`
- **map_helpers.py** (14 connections) — `server/api/map_helpers.py`
- **load_rooms_with_coordinates()** (14 connections) — `server/api/map_helpers.py`
- **load_single_room_with_coordinates()** (11 connections) — `server/api/map_helpers.py`
- **load_room_exits()** (9 connections) — `server/api/map_helpers.py`
- **build_room_dict()** (8 connections) — `server/api/map_helpers.py`
- **build_zone_pattern()** (7 connections) — `server/api/map_helpers.py`
- **_MockResultRows** (7 connections) — `server/tests/unit/api/test_map_helpers.py`
- **TestBuildZonePattern** (5 connections) — `server/tests/unit/api/test_map_helpers.py`
- **Any** (4 connections)
- **TestBuildRoomDict** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_room_exits_attaches_exits_by_stable_id()** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_rooms_with_coordinates_executes_zone_query_and_exits()** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_single_room_with_coordinates_loads_exits()** (4 connections) — `server/tests/unit/api/test_map_helpers.py`
- **AsyncSession** (3 connections)
- **.test_plane_zone_only()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **.test_plane_zone_sub_zone()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **.test_empty_sub_zone_treated_as_none()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **.test_full_row()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **.test_null_map_coords()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_room_exits_no_rooms_no_query()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **test_load_single_room_with_coordinates_none_when_missing()** (3 connections) — `server/tests/unit/api/test_map_helpers.py`
- **Map API helpers: room loading and zone pattern utilities.  Extracted from maps.p** (1 connections) — `server/api/map_helpers.py`
- **Build zone pattern for room query.      Args:         plane: Plane name** (1 connections) — `server/api/map_helpers.py`
- **Build room dictionary from database row.      Args:         row: Database row re** (1 connections) — `server/api/map_helpers.py`
- *... and 19 more nodes in this community*

## Relationships

- [maps handle ascii](maps_handle_ascii.md) (6 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/tests/unit/api/test_map_helpers.py`

## Audit Trail

- EXTRACTED: 156 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*