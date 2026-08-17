# ExplorationService

> 85 nodes

## Key Concepts

- **ExplorationService** (77 connections) — `server/services/exploration_service.py`
- **RoomService** (75 connections) — `server/game/room_service.py`
- **maps.py** (67 connections) — `server/api/maps.py`
- **test_maps.py** (55 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (18 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **asyncio** (18 connections)
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (11 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **_build_ascii_map_response()** (9 connections) — `server/api/maps.py`
- **_build_ascii_minimap_response()** (9 connections) — `server/api/maps.py`
- **_get_current_room_id()** (9 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **_handle_ascii_map_error()** (8 connections) — `server/api/maps.py`
- **test_ensure_coordinates_generated_when_missing()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **_CoordGenCtx** (7 connections) — `server/api/maps.py`
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (7 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (7 connections) — `server/tests/unit/api/test_maps.py`
- **Any** (7 connections)
- *... and 60 more nodes in this community*

## Relationships

- [test_exploration_service.py](test_exploration_service.py.md) (36 shared connections)
- [_run_set_map_origin](_run_set_map_origin.md) (35 shared connections)
- [get_logger](get_logger.md) (33 shared connections)
- [test_rooms_api.py](test_rooms_api.py.md) (21 shared connections)
- [User](User.md) (19 shared connections)
- [Any](Any.md) (18 shared connections)
- [map_minimap.py](map_minimap.py.md) (15 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (11 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (7 shared connections)
- [._get_room_uuid_by_stable_id](_get_room_uuid_by_stable_id.md) (7 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (6 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/game/room_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 341 (77%)
- INFERRED: 100 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*