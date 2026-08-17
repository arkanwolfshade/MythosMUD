# server api character creation

> 201 nodes

## Key Concepts

- **api/character_creation.py** (67 connections) — `server/api/character_creation.py`
- **player_service.py** (49 connections) — `server/game/player_service.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **PlayerRead** (46 connections) — `server/schemas/players/player.py`
- **test_player_requests.py** (31 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **test_player_schemas.py** (23 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **players/player.py** (21 connections) — `server/schemas/players/player.py`
- **player_requests.py** (16 connections) — `server/schemas/players/player_requests.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **LucidityLossRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **FearRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **HealRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **OccultKnowledgeRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **players/character_creation.py** (11 connections) — `server/schemas/players/character_creation.py`
- *... and 176 more nodes in this community*

## Relationships

- [server api players](server_api_players.md) (43 shared connections)
- [server api player effects](server_api_player_effects.md) (35 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (27 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (26 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (24 shared connections)
- [server api character creation rationale](server_api_character_creation_rationale.md) (15 shared connections)
- [leveluphook](leveluphook.md) (14 shared connections)
- [computed field](computed_field.md) (14 shared connections)
- [server api players get player](server_api_players_get_player.md) (12 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (11 shared connections)
- [server game player creation service](server_game_player_creation_service.md) (9 shared connections)
- [server commands admin shutdown command](server_commands_admin_shutdown_command.md) (8 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/profession_service.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/schemas/test_player_requests.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 664 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*