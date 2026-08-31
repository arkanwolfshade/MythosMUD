# StatsGenerator

> 27 nodes

## Key Concepts

- **StatsGenerator** (43 connections) — `server/game/stats_generator.py`
- **test_stats_generator.py** (20 connections) — `server/tests/unit/game/test_stats_generator.py`
- **stats_generator.py** (16 connections) — `server/game/stats_generator.py`
- **character_creation_service.py** (15 connections) — `server/game/character_creation_service.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
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
- **test_generate_random_stats_values_in_range()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_generate_random_stats_with_seed_is_reproducible()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_point_buy_within_bounds()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_unknown_method_falls_back_to_3d6()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_profession_missing_profession_raises()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **asyncio** (1 connections)
- **Character creation service for MythosMUD server. This module handles all…** (1 connections) — `server/game/character_creation_service.py`
- **Stats Generator Service for MythosMUD. This module provides random stat…** (1 connections) — `server/game/stats_generator.py`
- **Generate Stats with random attribute values. Factory function for creating…** (1 connections) — `server/game/stats_generator.py`
- **Service for generating random character statistics.** (1 connections) — `server/game/stats_generator.py`
- *... and 2 more nodes in this community*

## Relationships

- [Stats](Stats.md) (21 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CharacterCreationService](CharacterCreationService.md) (4 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (2 shared connections)
- [.validate_current_vs_max_stats](validate_current_vs_max_stats.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/game/stats_generator.py`
- `server/tests/unit/game/test_stats_generator.py`

## Audit Trail

- EXTRACTED: 103 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*