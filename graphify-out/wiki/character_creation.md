# character creation

> 272 nodes

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **__init__.py** (38 connections) — `server/schemas/players/__init__.py`
- **StatsGenerator** (35 connections) — `server/game/stats_generator.py`
- **player_effects.py** (30 connections) — `server/api/player_effects.py`
- **test_player_requests.py** (29 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_player_effects_endpoints.py** (28 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (20 connections) — `server/schemas/players/player_requests.py`
- **professions.py** (19 connections) — `server/api/professions.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **ProfessionService** (17 connections) — `server/game/profession_service.py`
- **CreateCharacterRequest** (17 connections) — `server/schemas/players/player_requests.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **stats_generator.py** (14 connections) — `server/game/stats_generator.py`
- **player_requests.py** (14 connections) — `server/schemas/players/player_requests.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **apply_lucidity_loss()** (12 connections) — `server/api/player_effects.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- *... and 247 more nodes in this community*

## Relationships

- [APIRouter](APIRouter.md) (77 shared connections)
- [Connection Manager](Connection_Manager.md) (50 shared connections)
- [. init ()](_init_%28%29.md) (46 shared connections)
- [main()](main%28%29.md) (26 shared connections)
- [Any](Any.md) (13 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (11 shared connections)
- [Core character statistics with Lovecraftian](Core_character_statistics_with_Lovecraftian.md) (9 shared connections)
- [BaseUserManager](BaseUserManager.md) (8 shared connections)
- [Request](Request.md) (7 shared connections)
- [AsyncSession](AsyncSession.md) (7 shared connections)
- [get skill repository()](get_skill_repository%28%29.md) (4 shared connections)
- [test character creation service](test_character_creation_service.md) (3 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/player_effects.py`
- `server/api/professions.py`
- `server/commands/admin_shutdown_command.py`
- `server/dependencies.py`
- `server/game/character_creation_service.py`
- `server/game/profession_service.py`
- `server/game/stats_generator.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/schemas/test_player_requests.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 1260 (95%)
- INFERRED: 71 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*