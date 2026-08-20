# maps.py

> 84 nodes

## Key Concepts

- **maps.py** (67 connections) — `server/api/maps.py`
- **test_maps.py** (55 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (18 connections) — `server/api/map_helpers.py`
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
- **_run_coordinate_recalculation()** (11 connections) — `server/api/maps.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **AsyncSession** (10 connections)
- **SetOriginRequest** (9 connections) — `server/api/maps.py`
- **_build_ascii_map_response()** (9 connections) — `server/api/maps.py`
- **_build_ascii_minimap_response()** (9 connections) — `server/api/maps.py`
- **_get_current_room_id()** (9 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **Request** (9 connections)
- **_handle_ascii_map_error()** (8 connections) — `server/api/maps.py`
- **test_ensure_coordinates_generated_when_missing()** (8 connections) — `server/tests/unit/api/test_maps.py`
- *... and 59 more nodes in this community*

## Relationships

- [ExplorationService](ExplorationService.md) (26 shared connections)
- [get_logger](get_logger.md) (24 shared connections)
- [User](User.md) (22 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [maps/__init__.py](maps-__init__.py.md) (13 shared connections)
- [RoomService](RoomService.md) (12 shared connections)
- [map_minimap.py](map_minimap.py.md) (8 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (6 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (4 shared connections)
- [CoordinateValidator](CoordinateValidator.md) (4 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (3 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (3 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 314 (89%)
- INFERRED: 38 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*