# profession game service

> 111 nodes

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (20 connections) — `server/schemas/players/player_requests.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **ValidateStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **TestValidateCharacterStats** (9 connections) — `server/tests/unit/api/test_character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **StatSummary** (8 connections) — `server/schemas/players/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- **Any** (6 connections)
- *... and 86 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (29 shared connections)
- [game models stats](game_models_stats.md) (19 shared connections)
- [player requests schemas](player_requests_schemas.md) (18 shared connections)
- [player service game](player_service_game.md) (12 shared connections)
- [Loot Generation](Loot_Generation.md) (9 shared connections)
- [Player Stats](Player_Stats.md) (8 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (7 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (7 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (3 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (3 shared connections)
- [status game spell](status_game_spell.md) (3 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (3 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/game/profession_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 488 (94%)
- INFERRED: 33 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*