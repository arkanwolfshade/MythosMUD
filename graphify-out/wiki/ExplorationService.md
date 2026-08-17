# ExplorationService

> 141 nodes

## Key Concepts

- **ExplorationService** (77 connections) — `server/services/exploration_service.py`
- **RoomService** (75 connections) — `server/game/room_service.py`
- **maps.py** (67 connections) — `server/api/maps.py`
- **test_maps.py** (55 connections) — `server/tests/unit/api/test_maps.py`
- **room_service.py** (23 connections) — `server/game/room_service.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **exploration_service.py** (18 connections) — `server/services/exploration_service.py`
- **asyncio** (18 connections)
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (13 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
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
- *... and 116 more nodes in this community*

## Relationships

- [User](User.md) (37 shared connections)
- [test_exploration_service.py](test_exploration_service.py.md) (37 shared connections)
- [map_minimap.py](map_minimap.py.md) (23 shared connections)
- [Any](Any.md) (19 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [test_rooms_api.py](test_rooms_api.py.md) (14 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (9 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (7 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (5 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (5 shared connections)

## Source Files

- `server/api/maps.py`
- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 484 (83%)
- INFERRED: 101 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*