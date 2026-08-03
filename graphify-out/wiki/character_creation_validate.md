# character creation validate

> 72 nodes

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **StatsGenerator** (35 connections) — `server/game/stats_generator.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **RollStatsRequest** (20 connections) — `server/schemas/players/player_requests.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **stats_generator.py** (14 connections) — `server/game/stats_generator.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **ValidateStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **StatSummary** (8 connections) — `server/schemas/players/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- **Any** (6 connections)
- **.test_roll_character_stats_rate_limit()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_profession_not_found()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **Stats** (5 connections)
- **_validate_user_for_stats_roll()** (5 connections) — `server/api/character_creation.py`
- *... and 47 more nodes in this community*

## Relationships

- [Player Stats](Player_Stats.md) (19 shared connections)
- [auth users rationale](auth_users_rationale.md) (17 shared connections)
- [Exception Containers](Exception_Containers.md) (13 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (11 shared connections)
- [stats game generator](stats_game_generator.md) (11 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [game models stats](game_models_stats.md) (7 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (6 shared connections)
- [character creation service](character_creation_service.md) (5 shared connections)
- [player requests schemas](player_requests_schemas.md) (5 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/game/character_creation_service.py`
- `server/game/stats_generator.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 376 (93%)
- INFERRED: 29 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*