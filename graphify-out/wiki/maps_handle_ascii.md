# maps handle ascii

> 142 nodes

## Key Concepts

- **RoomService** (80 connections) — `server/game/room_service.py`
- **ExplorationService** (79 connections) — `server/services/exploration_service.py`
- **maps.py** (53 connections) — `server/api/maps.py`
- **test_maps.py** (52 connections) — `server/tests/unit/api/test_maps.py`
- **rooms.py** (36 connections) — `server/api/rooms.py`
- **room_service.py** (22 connections) — `server/game/room_service.py`
- **MapZoneContext** (20 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **_ensure_coordinates_generated()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **get_ascii_map()** (14 connections) — `server/api/maps.py`
- **set_map_origin()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (13 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **test_rooms_exploration_filter.py** (12 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **_ensure_coords_stub()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **AsyncSession** (8 connections)
- **_handle_ascii_map_error()** (8 connections) — `server/api/maps.py`
- *... and 117 more nodes in this community*

## Relationships

- [map helpers rationale](map_helpers_rationale.md) (28 shared connections)
- [player requests schemas](player_requests_schemas.md) (28 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (27 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (25 shared connections)
- [main rationale failure()](main_rationale_failure%28%29.md) (17 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (13 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (13 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (12 shared connections)
- [room cache services](room_cache_services.md) (10 shared connections)
- [playerHandlers eventHandlers healthEvent](playerHandlers_eventHandlers_healthEvent.md) (10 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (8 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/maps/map.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 777 (89%)
- INFERRED: 96 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*