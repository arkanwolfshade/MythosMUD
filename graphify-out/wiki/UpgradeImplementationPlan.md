# UpgradeImplementationPlan

> 21 nodes

## Key Concepts

- **StatsGenerator** (43 connections) — `server/game/stats_generator.py`
- **test_stats_generator.py** (20 connections) — `server/tests/unit/game/test_stats_generator.py`
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
- **test_generate_random_stats_values_in_range()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_generate_random_stats_with_seed_is_reproducible()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_point_buy_within_bounds()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_unknown_method_falls_back_to_3d6()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_profession_missing_profession_raises()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **asyncio** (1 connections)
- **Generate Stats with random attribute values. Factory function for creating…** (1 connections) — `server/game/stats_generator.py`
- **Service for generating random character statistics.** (1 connections) — `server/game/stats_generator.py`
- **Unit tests for stats generation.** (1 connections) — `server/tests/unit/game/test_stats_generator.py`

## Relationships

- [generate_sql.mjs](generate_sql.mjs.md) (9 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (7 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (6 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [test_enhanced_logging_config.py](test_enhanced_logging_config.py.md) (4 shared connections)
- [Graphify Code Graph](Graphify_Code_Graph.md) (3 shared connections)
- [test_inventory_display_helpers.py](test_inventory_display_helpers.py.md) (2 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [test_parse_exits_json_list](test_parse_exits_json_list.md) (1 shared connections)
- [Cthulhu Dark Ages - 3rd Edition (source summary)](Cthulhu_Dark_Ages_-_3rd_Edition_source_summary.md) (1 shared connections)
- [Dark Young of Shub-Niggurath.md](Dark_Young_of_Shub-Niggurath.md.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/tests/unit/game/test_stats_generator.py`

## Audit Trail

- EXTRACTED: 76 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*