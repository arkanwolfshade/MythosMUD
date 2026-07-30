# NPCCombatIntegrationService

> 346 nodes

## Key Concepts

- **ExplorationService** (75 connections) — `server/services/exploration_service.py`
- **RoomService** (70 connections) — `server/game/room_service.py`
- **maps.py** (53 connections) — `server/api/maps.py`
- **test_exploration_service.py** (45 connections) — `server/tests/unit/services/test_exploration_service.py`
- **test_maps.py** (32 connections) — `server/tests/unit/api/test_maps.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **room_service.py** (21 connections) — `server/game/room_service.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **MapZoneContext** (19 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **test_map_helpers.py** (15 connections) — `server/tests/unit/api/test_map_helpers.py`
- **map_helpers.py** (14 connections) — `server/api/map_helpers.py`
- **load_rooms_with_coordinates()** (14 connections) — `server/api/map_helpers.py`
- **_ensure_coordinates_generated()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (13 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **get_ascii_map()** (12 connections) — `server/api/maps.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **load_single_room_with_coordinates()** (11 connections) — `server/api/map_helpers.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **set_map_origin()** (11 connections) — `server/api/maps.py`
- *... and 321 more nodes in this community*

## Relationships

- [metrics](metrics.md) (29 shared connections)
- [real time](real_time.md) (24 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (21 shared connections)
- [. init ()](_init_%28%29.md) (13 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (13 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (7 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (6 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (6 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (5 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (5 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (2 shared connections)
- [test room service](test_room_service.md) (2 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/ascii_map_renderer.py`
- `server/services/coordinate_validator.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_helpers.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 1398 (95%)
- INFERRED: 75 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*