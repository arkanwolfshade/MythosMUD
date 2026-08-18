# server api character creation

> 272 nodes

## Key Concepts

- **api/character_creation.py** (67 connections) — `server/api/character_creation.py`
- **player_service.py** (49 connections) — `server/game/player_service.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **PlayerRead** (46 connections) — `server/schemas/players/player.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (24 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **test_player_schemas.py** (23 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player_schema_converter.py** (22 connections) — `server/game/player_schema_converter.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **players/player.py** (21 connections) — `server/schemas/players/player.py`
- **test_player_schema_converter_weapon.py** (20 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- *... and 247 more nodes in this community*

## Relationships

- [server api players](server_api_players.md) (61 shared connections)
- [server api player effects](server_api_player_effects.md) (23 shared connections)
- [computed field](computed_field.md) (20 shared connections)
- [dependsparam](dependsparam.md) (17 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (15 shared connections)
- [server dependencies](server_dependencies.md) (15 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (13 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (12 shared connections)
- [server game player service playerservice](server_game_player_service_playerservice.md) (10 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (10 shared connections)
- [server api admin npc instances](server_api_admin_npc_instances.md) (10 shared connections)
- [server async persistence](server_async_persistence.md) (8 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/combat_handler.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/player_creation_service.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/game/profession_service.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 798 (98%)
- INFERRED: 18 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*