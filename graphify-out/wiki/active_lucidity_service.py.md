# active_lucidity_service.py

> 254 nodes · cohesion 0.02

## Key Concepts

- **ExplorationService** (80 connections) — `server/services/exploration_service.py`
- **maps.py** (66 connections) — `server/api/maps.py`
- **test_maps.py** (53 connections) — `server/tests/unit/api/test_maps.py`
- **test_exploration_service.py** (44 connections) — `server/tests/unit/services/test_exploration_service.py`
- **asyncio** (27 connections)
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (20 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **MapZoneContext** (18 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **asyncio** (18 connections)
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (12 connections) — `server/api/maps.py`
- **_ensure_current_room_in_minimap_rooms()** (11 connections) — `server/api/map_minimap.py`
- **_ensure_coordinates_generated()** (11 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_run_coordinate_recalculation()** (11 connections) — `server/api/maps.py`
- **maps/__init__.py** (11 connections) — `server/schemas/maps/__init__.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **AsyncSession** (10 connections)
- **_apply_minimap_fallback_coordinates()** (9 connections) — `server/api/map_minimap.py`
- *... and 229 more nodes in this community*

## Relationships

- [useMythosAppActions.ts](useMythosAppActions.ts.md) (51 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (24 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (16 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (14 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (12 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (11 shared connections)
- [Room](Room.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [RoomDataValidator](RoomDataValidator.md) (4 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (4 shared connections)
- [Performance Profiler Subagent](Performance_Profiler_Subagent.md) (4 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (4 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/services/test_exploration_service.py`

## Audit Trail

- EXTRACTED: 632 (87%)
- INFERRED: 96 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*