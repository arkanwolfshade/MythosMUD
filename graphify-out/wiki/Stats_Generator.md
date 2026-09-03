# Stats Generator

> 74 nodes

## Key Concepts

- **Stats** (93 connections) — `server/models/game.py`
- **StatsGenerator** (45 connections) — `server/game/stats_generator.py`
- **stats_generator.py** (20 connections) — `server/game/stats_generator.py`
- **test_stats_generator.py** (20 connections) — `server/tests/unit/game/test_stats_generator.py`
- **character_creation_service.py** (15 connections) — `server/game/character_creation_service.py`
- **generate_random_stats()** (10 connections) — `server/game/stats_generator.py`
- **stats_generator_summary.py** (9 connections) — `server/game/stats_generator_summary.py`
- **build_stat_summary()** (8 connections) — `server/game/stats_generator_summary.py`
- **.roll_stats()** (7 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **_ProfessionStatRequirementsSource** (6 connections) — `server/game/stats_generator.py`
- **._roll_until_profession_requirements_met()** (6 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **._resolve_profession_stat_requirements()** (4 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **_build_attribute_summary()** (4 connections) — `server/game/stats_generator_summary.py`
- **_core_stat_values_by_field()** (4 connections) — `server/game/stats_generator_summary.py`
- **_stat_value_for_summary()** (3 connections) — `server/game/stats_generator_summary.py`
- *... and 49 more nodes in this community*

## Relationships

- [Test Game Stats Methods](Test_Game_Stats_Methods.md) (28 shared connections)
- [Game](Game.md) (15 shared connections)
- [Character Creation API](Character_Creation_API.md) (11 shared connections)
- [Test Character Creation Service](Test_Character_Creation_Service.md) (8 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (7 shared connections)
- [Test Player Schemas](Test_Player_Schemas.md) (5 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)
- [Test Player Service](Test_Player_Service.md) (4 shared connections)
- [Test Game Player](Test_Game_Player.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Test Game Enums](Test_Game_Enums.md) (3 shared connections)
- [Players](Players.md) (2 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/game/stats_generator.py`
- `server/game/stats_generator_summary.py`
- `server/models/game.py`
- `server/tests/unit/game/test_stats_generator.py`

## Audit Trail

- EXTRACTED: 239 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*