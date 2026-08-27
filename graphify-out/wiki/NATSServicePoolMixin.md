# NATSServicePoolMixin

> 184 nodes

## Key Concepts

- **User** (255 connections) — `server/models/user.py`
- **ExplorationService** (76 connections) — `server/services/exploration_service.py`
- **maps.py** (67 connections) — `server/api/maps.py`
- **test_maps.py** (55 connections) — `server/tests/unit/api/test_maps.py`
- **MapZoneContext** (18 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **asyncio** (18 connections)
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **test_endpoints_invites.py** (15 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **recalculate_coordinates()** (12 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (11 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_run_coordinate_recalculation()** (11 connections) — `server/api/maps.py`
- **maps/__init__.py** (11 connections) — `server/schemas/maps/__init__.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **AsyncSession** (10 connections)
- **map.py** (10 connections) — `server/schemas/maps/map.py`
- **SetOriginRequest** (9 connections) — `server/api/maps.py`
- **_build_ascii_map_response()** (9 connections) — `server/api/maps.py`
- **_build_ascii_minimap_response()** (9 connections) — `server/api/maps.py`
- *... and 159 more nodes in this community*

## Relationships

- [NPCSpawningService](NPCSpawningService.md) (44 shared connections)
- [server/commands/__init__.py](server-commands-__init__.py.md) (35 shared connections)
- [maps.py](maps.py.md) (28 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (24 shared connections)
- [EldritchIcon.tsx](EldritchIcon.tsx.md) (23 shared connections)
- [models/container.py](models-container.py.md) (21 shared connections)
- [ContainerComponent](ContainerComponent.md) (17 shared connections)
- [catatonia_check.py](catatonia_check.py.md) (16 shared connections)
- [ChatService](ChatService.md) (16 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (14 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (12 shared connections)
- [test_player_position_service.py](test_player_position_service.py.md) (12 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/maps.py`
- `server/models/user.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/exploration_service.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 648 (82%)
- INFERRED: 138 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*