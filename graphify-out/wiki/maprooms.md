# maprooms

> 288 nodes

## Key Concepts

- **RoomService** (75 connections) — `server/game/room_service.py`
- **maps.py** (67 connections) — `server/api/maps.py`
- **test_maps.py** (55 connections) — `server/tests/unit/api/test_maps.py`
- **room_service.py** (23 connections) — `server/game/room_service.py`
- **map_minimap.py** (21 connections) — `server/api/map_minimap.py`
- **test_map_minimap_helpers.py** (21 connections) — `server/tests/unit/api/test_map_minimap_helpers.py`
- **MapZoneContext** (18 connections) — `server/api/map_helpers.py`
- **_prepare_ascii_map_context()** (18 connections) — `server/api/maps.py`
- **exploration_service.py** (18 connections) — `server/services/exploration_service.py`
- **asyncio** (18 connections)
- **generate_minimap_html()** (16 connections) — `server/api/map_minimap.py`
- **get_ascii_map()** (16 connections) — `server/api/maps.py`
- **get_ascii_minimap()** (16 connections) — `server/api/maps.py`
- **test_map_helpers.py** (16 connections) — `server/tests/unit/api/test_map_helpers.py`
- **map_helpers.py** (15 connections) — `server/api/map_helpers.py`
- **load_rooms_with_coordinates()** (14 connections) — `server/api/map_helpers.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/maps.py`
- **_run_set_map_origin()** (13 connections) — `server/api/maps.py`
- **set_map_origin()** (13 connections) — `server/api/maps.py`
- **_apply_exploration_filter_if_needed()** (13 connections) — `server/api/rooms.py`
- **list_rooms()** (13 connections) — `server/api/rooms.py`
- **Any** (13 connections)
- **test_rooms_exploration_filter.py** (13 connections) — `server/tests/unit/api/test_rooms_exploration_filter.py`
- **recalculate_coordinates()** (12 connections) — `server/api/maps.py`
- **CoordinateValidator** (11 connections) — `server/services/coordinate_validator.py`
- *... and 263 more nodes in this community*

## Relationships

- [claude rules fastapi](claude_rules_fastapi.md) (44 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (33 shared connections)
- [server services exploration service explorationservice](server_services_exploration_service_explorationservice.md) (29 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (28 shared connections)
- [leveluphook](leveluphook.md) (8 shared connections)
- [server api players get player](server_api_players_get_player.md) (6 shared connections)
- [characterinfo](characterinfo.md) (6 shared connections)
- [server services ascii map renderer](server_services_ascii_map_renderer.md) (6 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (5 shared connections)
- [server services coordinate generator coordinategenerator](server_services_coordinate_generator_coordinategenerator.md) (4 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (3 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (2 shared connections)

## Source Files

- `server/api/map_helpers.py`
- `server/api/map_minimap.py`
- `server/api/maps.py`
- `server/api/rooms.py`
- `server/game/room_service.py`
- `server/schemas/maps/__init__.py`
- `server/schemas/maps/map.py`
- `server/services/coordinate_validator.py`
- `server/services/exploration_service.py`
- `server/tests/unit/api/test_map_helpers.py`
- `server/tests/unit/api/test_map_minimap_helpers.py`
- `server/tests/unit/api/test_maps.py`
- `server/tests/unit/api/test_rooms_api.py`
- `server/tests/unit/api/test_rooms_exploration_filter.py`

## Audit Trail

- EXTRACTED: 728 (91%)
- INFERRED: 69 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*