# Community 391

> 45 nodes

## Key Concepts

- **StatsGenerator** (43 connections) — `server/game/stats_generator.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **Stats** (12 connections)
- **generate_random_stats()** (11 connections) — `server/game/stats_generator.py`
- **.roll_stats()** (7 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **._roll_until_profession_requirements_met()** (6 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
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
- *... and 20 more nodes in this community*

## Relationships

- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (8 shared connections)
- [Community 236](Community_236.md) (7 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (6 shared connections)
- [Community 1417](Community_1417.md) (3 shared connections)
- [Community 860](Community_860.md) (2 shared connections)
- [Community 861](Community_861.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)
- [Community 862](Community_862.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/tests/unit/game/test_stats_generator.py`

## Audit Trail

- EXTRACTED: 110 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*