# test_maps.py

> 37 nodes

## Key Concepts

- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (9 connections) — `server/api/maps.py`
- **_get_current_room_id()** (9 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **asyncio** (8 connections)
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (7 connections) — `server/tests/unit/api/test_maps.py`
- **Any** (7 connections)
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **_CoordGenCtx** (5 connections) — `server/api/maps.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **test_filter_explored_rooms_calls_room_service()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_current_room_id_none_when_persistence_errors()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **UUID** (4 connections)
- **_ensure_coords_stub()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **mock_user_and_player()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_current_room_id_from_player()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_current_room_id_from_query_param()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_player_and_exploration_returns_none_when_no_player()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **UUID** (3 connections)
- **mock_request()** (2 connections) — `server/tests/unit/api/test_maps.py`
- *... and 12 more nodes in this community*

## Relationships

- [maps.py](maps.py.md) (21 shared connections)
- [User](User.md) (6 shared connections)
- [ExplorationService](ExplorationService.md) (5 shared connections)
- [RoomService](RoomService.md) (4 shared connections)
- [test_map_helpers.py](test_map_helpers.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/api/maps.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 119 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*