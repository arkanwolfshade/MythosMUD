# StatsGenerator

> 47 nodes

## Key Concepts

- **StatsGenerator** (43 connections) — `server/game/stats_generator.py`
- **test_stats_generator.py** (20 connections) — `server/tests/unit/game/test_stats_generator.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
- **Stats** (11 connections)
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **test_check_profession_requirements_maps_wisdom_to_power()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_check_profession_requirements_unknown_stat_fails()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_available_classes_filters_by_prerequisites()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_stat_summary_includes_totals()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_profession_no_requirements()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_validation_respects_required_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_fails_occultist()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_passes_investigator()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_unknown_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **.__init__()** (2 connections) — `server/game/stats_generator.py`
- *... and 22 more nodes in this community*

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (9 shared connections)
- [Stats](Stats.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)
- [CharacterCreationService](CharacterCreationService.md) (2 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [.validate_current_vs_max_stats](validate_current_vs_max_stats.md) (1 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/tests/unit/game/test_stats_generator.py`

## Audit Trail

- EXTRACTED: 99 (88%)
- INFERRED: 14 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*