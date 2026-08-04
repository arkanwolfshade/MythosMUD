# event connection helpers

> 24 nodes

## Key Concepts

- **StatsGenerator** (48 connections) — `server/game/stats_generator.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **stats_generator.py** (15 connections) — `server/game/stats_generator.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
- **test_roll_stats_unknown_method_falls_back_to_3d6()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_passes_investigator()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_fails_occultist()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_validate_class_prerequisites_unknown_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_available_classes_filters_by_prerequisites()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_validation_respects_required_class()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_check_profession_requirements_maps_wisdom_to_power()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_check_profession_requirements_unknown_stat_fails()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_get_stat_summary_includes_totals()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_profession_no_requirements()** (3 connections) — `server/tests/unit/game/test_stats_generator.py`
- **.__init__()** (2 connections) — `server/game/stats_generator.py`
- **test_generate_random_stats_with_seed_is_reproducible()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_generate_random_stats_values_in_range()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_point_buy_within_bounds()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_roll_stats_with_profession_missing_profession_raises()** (2 connections) — `server/tests/unit/game/test_stats_generator.py`
- **Stats Generator Service for MythosMUD.  This module provides random stat generat** (1 connections) — `server/game/stats_generator.py`
- **Generate Stats with random attribute values.      Factory function for creating** (1 connections) — `server/game/stats_generator.py`
- **Service for generating random character statistics.** (1 connections) — `server/game/stats_generator.py`
- **Initialize the stats generator.** (1 connections) — `server/game/stats_generator.py`
- **Unit tests for stats generation.** (1 connections) — `server/tests/unit/game/test_stats_generator.py`

## Relationships

- [nats services service](nats_services_service.md) (13 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (11 shared connections)
- [player service game](player_service_game.md) (10 shared connections)
- [profession game service](profession_game_service.md) (7 shared connections)
- [commands inventory put](commands_inventory_put.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [command factories communication](command_factories_communication.md) (2 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (1 shared connections)
- [service combat services](service_combat_services.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/tests/unit/game/test_stats_generator.py`

## Audit Trail

- EXTRACTED: 129 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*