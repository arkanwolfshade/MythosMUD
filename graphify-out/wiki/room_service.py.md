# room_service.py

> 54 nodes

## Key Concepts

- **room_service.py** (24 connections) — `server/game/room_service.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (21 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **exploration_service.py** (18 connections) — `server/services/exploration_service.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- **_resolve_current_room_for_minimap()** (9 connections) — `server/api/map_minimap.py`
- **_append_room_with_fallback_coords_if_needed()** (8 connections) — `server/api/map_minimap.py`
- **asyncio** (7 connections)
- **TestApplyMinimapFallbackCoordinates** (6 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_admin_path()** (6 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_generate_minimap_html_non_admin_filters_exploration()** (6 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **TestAppendRoomWithFallbackCoordsIfNeeded** (5 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_appends_missing()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_when_already_present()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_ensure_current_room_in_minimap_noop_without_id()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_from_pre_filter_list()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **test_resolve_current_room_loads_when_not_in_list()** (4 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **Any** (4 connections)
- **.test_appends_copy_with_fallback_0_0_when_coords_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_fallback_when_only_one_coord_missing()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_appends_room_unchanged_when_has_coords()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_admin_gets_grid_layout_for_rooms_without_coords()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **.test_fallback_grid_wraps_by_fallback_grid_width()** (3 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- *... and 29 more nodes in this community*

## Relationships

- [ExplorationService](ExplorationService.md) (16 shared connections)
- [BaseCommand](BaseCommand.md) (12 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (6 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (2 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (1 shared connections)

## Source Files

- `server/api/map_minimap.py`
- `server/game/room_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`

## Audit Trail

- EXTRACTED: 147 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*