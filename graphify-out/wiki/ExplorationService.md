# ExplorationService

> 129 nodes

## Key Concepts

- **ExplorationService** (76 connections) — `server/services/exploration_service.py`
- **maps.py** (67 connections) — `server/api/maps.py`
- **test_maps.py** (55 connections) — `server/tests/unit/api/test_maps.py`
- **room_service.py** (24 connections) — `server/game/room_service.py`
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
- **maps/__init__.py** (11 connections) — `server/schemas/maps/__init__.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **AsyncSession** (10 connections)
- **map.py** (10 connections) — `server/schemas/maps/map.py`
- **SetOriginRequest** (9 connections) — `server/api/maps.py`
- **_build_ascii_map_response()** (9 connections) — `server/api/maps.py`
- **_build_ascii_minimap_response()** (9 connections) — `server/api/maps.py`
- **_get_current_room_id()** (9 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- *... and 104 more nodes in this community*

## Relationships

- [test_exploration_service.py](test_exploration_service.py.md) (35 shared connections)
- [User](User.md) (29 shared connections)
- [pydantic.md](pydantic.md.md) (24 shared connections)
- [get_logger](get_logger.md) (24 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [map_minimap.py](map_minimap.py.md) (13 shared connections)
- [_apply_exploration_filter_if_needed](_apply_exploration_filter_if_needed.md) (7 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (6 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (5 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (4 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (4 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/game/room_service.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 426 (84%)
- INFERRED: 84 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*