# Stats

> 112 nodes

## Key Concepts

- **Stats** (79 connections) — `server/models/game.py`
- **StatsGenerator** (45 connections) — `server/game/stats_generator.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **stats_generator.py** (22 connections) — `server/game/stats_generator.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **get_stats_generator()** (11 connections) — `server/dependencies.py`
- **generate_random_stats()** (11 connections) — `server/game/stats_generator.py`
- **CoreStatValues** (7 connections) — `server/models/stats_random.py`
- **roll_random_core_stat_values()** (7 connections) — `server/models/stats_random.py`
- **._ensure_core_stats()** (6 connections) — `server/models/game.py`
- **stats_random.py** (6 connections) — `server/models/stats_random.py`
- **TestGetStatsGenerator** (5 connections) — `server/tests/unit/test_dependency_injection.py`
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
- *... and 87 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (15 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (14 shared connections)
- [Stats](Stats.md) (14 shared connections)
- [Player](Player.md) (9 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (8 shared connections)
- [.validate_current_vs_max_stats](validate_current_vs_max_stats.md) (8 shared connections)
- [stats_generator_summary.py](stats_generator_summary.py.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (5 shared connections)
- [test_player_service.py](test_player_service.py.md) (4 shared connections)
- [StatusEffect](StatusEffect.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)

## Source Files

- `server/dependencies.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/models/stats_random.py`
- `server/tests/unit/game/test_stats_generator.py`
- `server/tests/unit/models/test_game_stats_methods.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 277 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*