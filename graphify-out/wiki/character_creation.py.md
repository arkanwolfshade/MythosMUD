# character_creation.py

> 94 nodes · cohesion 0.04

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
- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
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
- **.test_roll_character_stats_profession_not_found()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_rate_limit()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- *... and 69 more nodes in this community*

## Relationships

- [__init__.py](__init__.py.md) (32 shared connections)
- [Stats](Stats.md) (21 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (17 shared connections)
- [exceptions.py](exceptions.py.md) (15 shared connections)
- [User](User.md) (15 shared connections)
- [test_dependency_injection.py](test_dependency_injection.py.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [ValidationError](ValidationError.md) (8 shared connections)
- [dependencies.py](dependencies.py.md) (5 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (5 shared connections)
- [MythosMUDError](MythosMUDError.md) (4 shared connections)
- [TestCreateCharacterWithStats](TestCreateCharacterWithStats.md) (4 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/game/character_creation_service.py`
- `server/game/profession_service.py`
- `server/game/stats_generator.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 446 (94%)
- INFERRED: 31 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*