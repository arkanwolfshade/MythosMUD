# dependsparam

> 161 nodes

## Key Concepts

- **User** (293 connections) — `server/models/user.py`
- **maps.py** (67 connections) — `server/api/maps.py`
- **test_maps.py** (55 connections) — `server/tests/unit/api/test_maps.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **asyncio** (18 connections)
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **test_users_current_user_logging.py** (13 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **recalculate_coordinates()** (12 connections) — `server/api/maps.py`
- **_ensure_coordinates_generated()** (11 connections) — `server/api/maps.py`
- **_filter_explored_rooms()** (11 connections) — `server/api/maps.py`
- **_run_coordinate_recalculation()** (11 connections) — `server/api/maps.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **maps/__init__.py** (11 connections) — `server/schemas/maps/__init__.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **_get_minimap_player_and_room_id()** (10 connections) — `server/api/maps.py`
- **AsyncSession** (10 connections)
- **map.py** (10 connections) — `server/schemas/maps/map.py`
- **SetOriginRequest** (9 connections) — `server/api/maps.py`
- **_build_ascii_map_response()** (9 connections) — `server/api/maps.py`
- **_build_ascii_minimap_response()** (9 connections) — `server/api/maps.py`
- **_get_current_room_id()** (9 connections) — `server/api/maps.py`
- *... and 136 more nodes in this community*

## Relationships

- [server api players](server_api_players.md) (42 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (41 shared connections)
- [baseusermanager](baseusermanager.md) (36 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (21 shared connections)
- [roomdictlist](roomdictlist.md) (20 shared connections)
- [authenticationbackend](authenticationbackend.md) (19 shared connections)
- [server api character creation](server_api_character_creation.md) (17 shared connections)
- [server services exploration service explorationservice](server_services_exploration_service_explorationservice.md) (17 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (15 shared connections)
- [server api metrics](server_api_metrics.md) (14 shared connections)
- [server api map helpers mapzonecontext](server_api_map_helpers_mapzonecontext.md) (13 shared connections)
- [server api admin npc definitions](server_api_admin_npc_definitions.md) (12 shared connections)

## Source Files

- `server/api/maps.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/auth/test_users_current_user_logging.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 617 (84%)
- INFERRED: 114 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*