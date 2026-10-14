# StatsGenerator

> 65 nodes

## Key Concepts

- **StatsGenerator** (45 connections) — `server/game/stats_generator.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **Stats** (12 connections)
- **generate_random_stats()** (11 connections) — `server/game/stats_generator.py`
- **stats_generator_summary.py** (9 connections) — `server/game/stats_generator_summary.py`
- **build_stat_summary()** (8 connections) — `server/game/stats_generator_summary.py`
- **.roll_stats()** (7 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **_ProfessionStatRequirementsSource** (6 connections) — `server/game/stats_generator.py`
- **._roll_until_profession_requirements_met()** (6 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._resolve_profession_stat_requirements()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **_build_attribute_summary()** (4 connections) — `server/game/stats_generator_summary.py`
- **_core_stat_values_by_field()** (4 connections) — `server/game/stats_generator_summary.py`
- **_stat_value_for_summary()** (3 connections) — `server/game/stats_generator_summary.py`
- **test_check_profession_requirements_maps_wisdom_to_power()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_check_profession_requirements_unknown_stat_fails()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- *... and 40 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (19 shared connections)
- [Stats](Stats.md) (11 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [ValueError](ValueError.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/game/stats_generator_summary.py`
- `server/tests/unit/game/test_stats_generator.py`

## Audit Trail

- EXTRACTED: 140 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*