# server api character creation apply

> 102 nodes

## Key Concepts

- **LoggedHTTPException** (358 connections) — `server/exceptions.py`
- **api/player_respawn.py** (29 connections) — `server/api/player_respawn.py`
- **test_rooms_api.py** (24 connections) — `server/tests/unit/api/test_rooms_api.py`
- **professions.py** (21 connections) — `server/api/professions.py`
- **test_player_respawn_api.py** (18 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **update_room_position()** (16 connections) — `server/api/rooms.py`
- **test_player_respawn_handlers.py** (16 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **test_professions_endpoints.py** (15 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **get_all_professions()** (11 connections) — `server/api/professions.py`
- **get_profession_by_id()** (11 connections) — `server/api/professions.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **get_room()** (10 connections) — `server/api/rooms.py`
- **_update_room_position_in_db()** (10 connections) — `server/api/rooms.py`
- **_validate_room_position_update()** (10 connections) — `server/api/rooms.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **players/profession.py** (8 connections) — `server/schemas/players/profession.py`
- **asyncio** (8 connections)
- **asyncio** (8 connections)
- **ProfessionListResponse** (7 connections) — `server/schemas/players/profession.py`
- *... and 77 more nodes in this community*

## Relationships

- [claude rules fastapi](claude_rules_fastapi.md) (88 shared connections)
- [maprooms](maprooms.md) (33 shared connections)
- [server api players](server_api_players.md) (33 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (32 shared connections)
- [server api character creation](server_api_character_creation.md) (27 shared connections)
- [characterinfo](characterinfo.md) (27 shared connections)
- [server api monitoring](server_api_monitoring.md) (19 shared connections)
- [server auth dependencies](server_auth_dependencies.md) (19 shared connections)
- [server api metrics](server_api_metrics.md) (15 shared connections)
- [server api container exception handlers](server_api_container_exception_handlers.md) (14 shared connections)
- [server api real time](server_api_real_time.md) (14 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/player_respawn.py`
- `server/api/professions.py`
- `server/api/rooms.py`
- `server/exceptions.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/players/profession.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/api/test_rooms_api.py`

## Audit Trail

- EXTRACTED: 517 (77%)
- INFERRED: 156 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*