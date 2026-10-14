# RoomService

> 356 nodes

## Key Concepts

- **RoomService** (104 connections) — `server/game/room_service.py`
- **ExplorationService** (80 connections) — `server/services/exploration_service.py`
- **maps.py** (66 connections) — `server/api/maps.py`
- **test_maps.py** (53 connections) — `server/tests/unit/api/test_maps.py`
- **test_exploration_service.py** (44 connections) — `server/tests/unit/services/test_exploration_service.py`
- **asyncio** (27 connections)
- **room_service.py** (26 connections) — `server/game/room_service.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **MapZoneContext** (18 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **exploration_service.py** (18 connections) — `server/services/exploration_service.py`
- **asyncio** (18 connections)
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **ascii_map_renderer.py** (16 connections) — `server/services/ascii_map_renderer.py`
- **test_rooms_helpers_fetch_room_list.py** (16 connections) — `server/tests/unit/api/test_rooms_helpers_fetch_room_list.py`
- **map_helpers.py** (14 connections) — `server/api/map_helpers.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms_helpers.py`
- **Any** (13 connections)
- **recalculate_coordinates()** (12 connections) — `server/api/maps.py`
- *... and 331 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (125 shared connections)
- [get_logger](get_logger.md) (44 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (16 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (13 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (6 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (4 shared connections)
- [CoordinateValidator](CoordinateValidator.md) (4 shared connections)
- [ValueError](ValueError.md) (4 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [test_room_service.py](test_room_service.py.md) (2 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/api/rooms_helpers.py`
- `server/game/room_service.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/ascii_map_renderer.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/api/test_rooms_helpers_fetch_room_list.py`
- `server/tests/unit/api/test_rooms_write_api.py`
- `server/tests/unit/services/test_exploration_service.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 864 (87%)
- INFERRED: 134 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*