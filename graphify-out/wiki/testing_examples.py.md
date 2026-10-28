# testing_examples.py

> 103 nodes · cohesion 0.03

## Key Concepts

- **Stats** (79 connections) — `server/models/game.py`
- **StatsGenerator** (45 connections) — `server/game/stats_generator.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **stats_generator.py** (21 connections) — `server/game/stats_generator.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **character_creation_service.py** (14 connections) — `server/game/character_creation_service.py`
- **generate_random_stats()** (11 connections) — `server/game/stats_generator.py`
- **CoreStatValues** (7 connections) — `server/models/stats_random.py`
- **roll_random_core_stat_values()** (7 connections) — `server/models/stats_random.py`
- **._ensure_core_stats()** (6 connections) — `server/models/game.py`
- **stats_random.py** (5 connections) — `server/models/stats_random.py`
- **_merge_random_core_stats()** (4 connections) — `server/models/game.py`
- **_needs_random_core_stats()** (3 connections) — `server/models/game.py`
- **test_check_profession_requirements_maps_wisdom_to_power()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_check_profession_requirements_unknown_stat_fails()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_available_classes_filters_by_prerequisites()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_stat_summary_includes_totals()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_profession_no_requirements()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_validation_respects_required_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_fails_occultist()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_passes_investigator()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_unknown_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_stats_get_attribute_modifier_different_attribute()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_negative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_none()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- *... and 78 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (33 shared connections)
- [test_rate_limiter.py](test_rate_limiter.py.md) (14 shared connections)
- [Movement Subsystem Design](Movement_Subsystem_Design.md) (8 shared connections)
- [Transaction Boundaries Audit](Transaction_Boundaries_Audit.md) (6 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (5 shared connections)
- [Room](Room.md) (4 shared connections)
- [test_inventory_mutation_guard_error_handling.py](test_inventory_mutation_guard_error_handling.py.md) (4 shared connections)
- [SchemaValidator](SchemaValidator.md) (4 shared connections)
- [Improve Layout Systematically](Improve_Layout_Systematically.md) (3 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (2 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/models/stats_random.py`
- `server/tests/unit/game/test_stats_generator.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 256 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*