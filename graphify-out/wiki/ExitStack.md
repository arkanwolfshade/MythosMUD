# ExitStack

> 70 nodes

## Key Concepts

- **ExplorationService** (75 connections) — `server/services/exploration_service.py`
- **RoomService** (70 connections) — `server/game/room_service.py`
- **maps.py** (53 connections) — `server/api/maps.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (19 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (13 connections) — `server/api/maps.py`
- **get_ascii_map()** (12 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **set_map_origin()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (10 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **_ensure_coords_stub()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **AsyncSession** (8 connections)
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **Request** (7 connections)
- **Any** (7 connections)
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **_get_minimap_player_and_room_id()** (7 connections) — `server/api/maps.py`
- **CoordinateValidator** (7 connections) — `server/services/coordinate_validator.py`
- **UUID** (6 connections)
- **_handle_ascii_map_error()** (6 connections) — `server/api/maps.py`
- *... and 45 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (36 shared connections)
- [Connection Manager](Connection_Manager.md) (20 shared connections)
- [Formatter](Formatter.md) (19 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (17 shared connections)
- [fetch schedule entries()](fetch_schedule_entries%28%29.md) (16 shared connections)
- [close db()](close_db%28%29.md) (12 shared connections)
- [real time](real_time.md) (12 shared connections)
- [. init ()](_init_%28%29.md) (11 shared connections)
- [test format player location invalid()](test_format_player_location_invalid%28%29.md) (8 shared connections)
- [get game status()](get_game_status%28%29.md) (7 shared connections)
- [test movement monitor](test_movement_monitor.md) (6 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (6 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/game/room_service.py`
- `server/services/coordinate_validator.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 477 (89%)
- INFERRED: 56 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*