# RoomService

> 106 nodes

## Key Concepts

- **RoomService** (61 connections) — `server/game/room_service.py`
- **MapZoneContext** (22 connections) — `server/api/map_helpers.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **Any** (13 connections)
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **TestApplyMinimapFallbackCoordinates** (8 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **.get_room()** (8 connections) — `server/game/room_service.py`
- **TestAppendRoomWithFallbackCoordsIfNeeded** (7 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.get_room_info()** (7 connections) — `server/game/room_service.py`
- **asyncio** (7 connections)
- **.filter_rooms_by_exploration()** (6 connections) — `server/game/room_service.py`
- **.get_adjacent_rooms()** (6 connections) — `server/game/room_service.py`
- **.list_rooms()** (5 connections) — `server/game/room_service.py`
- **test_generate_minimap_html_admin_path()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_non_admin_filters_exploration()** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.get_local_chat_scope()** (4 connections) — `server/game/room_service.py`
- **.get_room_exits()** (4 connections) — `server/game/room_service.py`
- *... and 81 more nodes in this community*

## Relationships

- [maps.py](maps.py.md) (21 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (8 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (7 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (7 shared connections)
- [_apply_exploration_filter_if_needed](_apply_exploration_filter_if_needed.md) (7 shared connections)
- [ExplorationService](ExplorationService.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_maps.py](test_maps.py.md) (5 shared connections)
- [ScheduleService](ScheduleService.md) (4 shared connections)
- [StatsGenerator](StatsGenerator.md) (4 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/game/room_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 260 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*