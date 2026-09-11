# RoomService

> 426 nodes

## Key Concepts

- **RoomService** (96 connections) — `server/game/room_service.py`
- **async_persistence.py** (94 connections) — `server/async_persistence.py`
- **ExplorationService** (76 connections) — `server/services/exploration_service.py`
- **maps.py** (66 connections) — `server/api/maps.py`
- **test_maps.py** (53 connections) — `server/tests/unit/api/test_maps.py`
- **test_exploration_service.py** (44 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **asyncio** (27 connections)
- **room_service.py** (23 connections) — `server/game/room_service.py`
- **asyncio** (23 connections)
- **test_rooms_api.py** (22 connections) — `server/tests/unit/api/test_rooms_api.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **MapZoneContext** (18 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **asyncio** (18 connections)
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- *... and 401 more nodes in this community*

## Relationships

- [rooms.py](rooms.py.md) (52 shared connections)
- [get_logger](get_logger.md) (52 shared connections)
- [User](User.md) (35 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (24 shared connections)
- [Player](Player.md) (17 shared connections)
- [PlayerService](PlayerService.md) (15 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (13 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (12 shared connections)
- [Room](Room.md) (9 shared connections)
- [Profession](Profession.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (7 shared connections)
- [GameBundle](GameBundle.md) (6 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/api/rooms.py`
- `server/async_persistence.py`
- `server/game/room_service.py`
- `server/models/profession.py`
- `server/persistence/container_create_params.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/ascii_map_renderer.py`
- `server/services/coordinate_validator.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/services/test_coordinate_validator.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 1066 (88%)
- INFERRED: 139 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*