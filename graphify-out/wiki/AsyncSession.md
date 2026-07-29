# AsyncSession

> 44 nodes

## Key Concepts

- **ExplorationService** (75 connections) — `server/services/exploration_service.py`
- **RoomService** (70 connections) — `server/game/room_service.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **get_ascii_map()** (12 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **_ensure_coords_stub()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **AsyncSession** (8 connections)
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **Any** (7 connections)
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **UUID** (6 connections)
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **UUID** (5 connections)
- **test_filter_explored_rooms_calls_room_service()** (5 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_player_and_exploration_returns_none_when_no_player()** (4 connections) — `server/tests/unit/api/test_maps.py`
- **.test_get_room_service_success()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **mock_user_and_player()** (3 connections) — `server/tests/unit/api/test_maps.py`
- **_MapRooms** (3 connections)
- **.__init__()** (2 connections) — `server/game/room_service.py`
- *... and 19 more nodes in this community*

## Relationships

- [test exploration service](test_exploration_service.md) (36 shared connections)
- [maps](maps.md) (25 shared connections)
- [Any](Any.md) (22 shared connections)
- [player respawn](player_respawn.md) (19 shared connections)
- [MapZoneContext](MapZoneContext.md) (15 shared connections)
- [APIRouter](APIRouter.md) (12 shared connections)
- [main()](main%28%29.md) (11 shared connections)
- [character creation](character_creation.md) (7 shared connections)
- [.get explored rooms()](get_explored_rooms%28%29.md) (7 shared connections)
- [map helpers](map_helpers.md) (3 shared connections)
- [test room service](test_room_service.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)

## Source Files

- `server/api/maps.py`
- `server/game/room_service.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 317 (87%)
- INFERRED: 49 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*