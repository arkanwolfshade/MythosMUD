# ExplorationService

> 330 nodes

## Key Concepts

- **ExplorationService** (77 connections) — `server/services/exploration_service.py`
- **RoomService** (75 connections) — `server/game/room_service.py`
- **maps.py** (67 connections) — `server/api/maps.py`
- **test_maps.py** (55 connections) — `server/tests/unit/api/test_maps.py`
- **test_exploration_service.py** (46 connections) — `server/tests/unit/services/test_exploration_service.py`
- **asyncio** (28 connections)
- **room_service.py** (23 connections) — `server/game/room_service.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (21 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **MapZoneContext** (18 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **exploration_service.py** (18 connections) — `server/services/exploration_service.py`
- **asyncio** (18 connections)
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **Any** (13 connections)
- **test_rooms_exploration_filter.py** (13 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **recalculate_coordinates()** (12 connections) — `server/api/maps.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_ensure_coordinates_generated()** (11 connections) — `server/api/maps.py`
- *... and 305 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (74 shared connections)
- [DatabaseError](DatabaseError.md) (15 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (12 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (9 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (4 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (4 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (4 shared connections)
- [CoordinateValidator](CoordinateValidator.md) (4 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (4 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 785 (88%)
- INFERRED: 110 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*