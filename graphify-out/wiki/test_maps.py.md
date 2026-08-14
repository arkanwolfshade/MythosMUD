# test_maps.py

> 77 nodes

## Key Concepts

- **test_maps.py** (53 connections) — `server/tests/unit/api/test_maps.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **asyncio** (18 connections)
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (12 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (11 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **SetOriginRequest** (10 connections) — `server/api/maps.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **AsyncSession** (10 connections)
- **_get_current_room_id()** (9 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **Request** (9 connections)
- **MapOriginSetResponse** (8 connections) — `server/schemas/maps/map.py`
- **_handle_ascii_map_error()** (8 connections) — `server/api/maps.py`
- **_CoordGenCtx** (7 connections) — `server/api/maps.py`
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (7 connections) — `server/tests/unit/api/test_maps.py`
- **Any** (7 connections)
- **_persist_map_origin()** (6 connections) — `server/api/maps.py`
- **test_ensure_coordinates_generated_when_missing()** (6 connections) — `server/tests/unit/api/test_maps.py`
- *... and 52 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (28 shared connections)
- [MapZoneContext](MapZoneContext.md) (15 shared connections)
- [User](User.md) (11 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [ExplorationService](ExplorationService.md) (7 shared connections)
- [maps/__init__.py](maps-__init__.py.md) (6 shared connections)
- [RoomService](RoomService.md) (6 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (4 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (3 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [CoordinateValidator](CoordinateValidator.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/schemas/maps/map.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 259 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*