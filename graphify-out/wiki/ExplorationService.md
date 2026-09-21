# ExplorationService

> 231 nodes

## Key Concepts

- **ExplorationService** (76 connections) — `server/services/exploration_service.py`
- **maps.py** (66 connections) — `server/api/maps.py`
- **test_maps.py** (53 connections) — `server/tests/unit/api/test_maps.py`
- **test_exploration_service.py** (44 connections) — `server/tests/unit/services/test_exploration_service.py`
- **asyncio** (27 connections)
- **MapZoneContext** (18 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **asyncio** (18 connections)
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **CoordinateValidator** (13 connections) — `server/services/coordinate_validator.py`
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
- **SetOriginRequest** (9 connections) — `server/api/maps.py`
- **_build_ascii_map_response()** (9 connections) — `server/api/maps.py`
- **_build_ascii_minimap_response()** (9 connections) — `server/api/maps.py`
- *... and 206 more nodes in this community*

## Relationships

- [RoomService](RoomService.md) (29 shared connections)
- [User](User.md) (25 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [DatabaseError](DatabaseError.md) (15 shared connections)
- [map_minimap.py](map_minimap.py.md) (11 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (6 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (4 shared connections)
- [DatabaseManager](DatabaseManager.md) (4 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (3 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/coordinate_validator.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/services/test_coordinate_validator.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 571 (86%)
- INFERRED: 91 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*