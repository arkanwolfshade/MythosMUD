# Player Stats

> 160 nodes

## Key Concepts

- **players.py** (66 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (54 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **get_player_quests()** (17 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_processing.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **select_character()** (14 connections) — `server/api/players.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **get_player_skills()** (12 connections) — `server/api/players.py`
- **delete_player()** (12 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- **get_player()** (11 connections) — `server/api/players.py`
- **delete_character()** (11 connections) — `server/api/players.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- **get_user_characters()** (10 connections) — `server/api/players.py`
- *... and 135 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (34 shared connections)
- [player requests schemas](player_requests_schemas.md) (25 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (24 shared connections)
- [Loot Generation](Loot_Generation.md) (20 shared connections)
- [game models stats](game_models_stats.md) (11 shared connections)
- [command factories communication](command_factories_communication.md) (11 shared connections)
- [command commands handler](command_commands_handler.md) (11 shared connections)
- [profession game service](profession_game_service.md) (8 shared connections)
- [command utility models](command_utility_models.md) (8 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (8 shared connections)
- [player service game](player_service_game.md) (5 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (4 shared connections)

## Source Files

- `server/api/players.py`
- `server/api/skills.py`
- `server/app/game_tick_processing.py`
- `server/game/player_search_service.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 815 (95%)
- INFERRED: 46 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*