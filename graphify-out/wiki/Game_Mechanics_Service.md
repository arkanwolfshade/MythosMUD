# Game Mechanics Service

> 348 nodes

## Key Concepts

- **Stats** (80 connections) — `server/models/game.py`
- **character_creation.py** (54 connections) — `server/api/character_creation.py`
- **SkillService** (37 connections) — `server/game/skill_service.py`
- **StatsGenerator** (36 connections) — `server/game/stats_generator.py`
- **test_character_creation_service.py** (31 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **RollStatsRequest** (22 connections) — `server/schemas/players/player_requests.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **roll_character_stats()** (21 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (21 connections) — `server/schemas/players/player_requests.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **create_character_with_stats()** (17 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (15 connections) — `server/api/character_creation.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **stats_generator.py** (14 connections) — `server/game/stats_generator.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **Any** (10 connections)
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **Any** (10 connections)
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- *... and 323 more nodes in this community*

## Relationships

- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (50 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (31 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (28 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (26 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (25 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (17 shared connections)
- [Character Creation API](Character_Creation_API.md) (12 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (11 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (10 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (10 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (8 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (7 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/game/character_creation_service.py`
- `server/game/profession_service.py`
- `server/game/skill_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/models/test_game_stats_methods.py`
- `server/tests/unit/test_dependency_injection.py`
- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 1310 (93%)
- INFERRED: 93 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*