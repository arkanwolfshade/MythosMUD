# maps handle ascii

> 57 nodes

## Key Concepts

- **RoomService** (80 connections) — `server/game/room_service.py`
- **test_maps.py** (52 connections) — `server/tests/unit/api/test_maps.py`
- **_prepare_ascii_map_context()** (17 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **get_ascii_map()** (14 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_get_current_room_id()** (10 connections) — `server/api/maps.py`
- **_get_player_and_exploration_service()** (9 connections) — `server/api/maps.py`
- **_ensure_coords_stub()** (9 connections) — `server/tests/unit/api/test_maps.py`
- **AsyncSession** (8 connections)
- **_handle_ascii_map_error()** (8 connections) — `server/api/maps.py`
- **test_prepare_ascii_map_context_applies_exploration_filter()** (8 connections) — `server/tests/unit/api/test_maps.py`
- **Request** (7 connections)
- **Any** (7 connections)
- **_needs_coordinate_generation()** (7 connections) — `server/api/maps.py`
- **UUID** (6 connections)
- **UUID** (6 connections)
- **_two_rooms()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_skips_for_superuser()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_apply_exploration_filter_if_needed_calls_for_normal_user()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_ensure_coordinates_generated_when_missing()** (6 connections) — `server/tests/unit/api/test_maps.py`
- **test_filter_explored_rooms_calls_room_service()** (5 connections) — `server/tests/unit/api/test_maps.py`
- **test_get_ascii_minimap_requires_auth()** (5 connections) — `server/tests/unit/api/test_maps.py`
- *... and 32 more nodes in this community*

## Relationships

- [persistence container rationale](persistence_container_rationale.md) (22 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (20 shared connections)
- [corpse lifecycle service](corpse_lifecycle_service.md) (18 shared connections)
- [player requests schemas](player_requests_schemas.md) (17 shared connections)
- [main rationale failure()](main_rationale_failure%28%29.md) (16 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (11 shared connections)
- [room game service](room_game_service.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [persistence container extended](persistence_container_extended.md) (7 shared connections)
- [room cache services](room_cache_services.md) (6 shared connections)
- [panels monitoringPanelTestFixtures Monit](panels_monitoringPanelTestFixtures_Monit.md) (5 shared connections)
- [map helpers rationale](map_helpers_rationale.md) (3 shared connections)

## Source Files

- `server/api/maps.py`
- `server/game/room_service.py`
- `server/tests/unit/api/test_maps.py`

## Audit Trail

- EXTRACTED: 337 (84%)
- INFERRED: 62 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*