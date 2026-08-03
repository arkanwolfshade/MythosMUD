# profession game service

> 86 nodes

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **StatsGenerator** (35 connections) — `server/game/stats_generator.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **ProfessionService** (17 connections) — `server/game/profession_service.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **stats_generator.py** (14 connections) — `server/game/stats_generator.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **ValidateStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **StatSummary** (8 connections) — `server/schemas/players/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- **Any** (6 connections)
- **.test_roll_character_stats_rate_limit()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_profession_not_found()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **Stats** (5 connections)
- *... and 61 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (21 shared connections)
- [game models stats](game_models_stats.md) (20 shared connections)
- [command inventory factories](command_inventory_factories.md) (16 shared connections)
- [stats game generator](stats_game_generator.md) (11 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (10 shared connections)
- [command inventory models](command_inventory_models.md) (9 shared connections)
- [schemas unified room](schemas_unified_room.md) (9 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (8 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (6 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [logging file setup](logging_file_setup.md) (4 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (4 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/game/profession_service.py`
- `server/game/stats_generator.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 416 (93%)
- INFERRED: 29 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*