# schemas unified room

> 103 nodes

## Key Concepts

- **Stats** (80 connections) — `server/models/game.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **generate_random_stats()** (6 connections) — `server/game/stats_generator.py`
- **.validate_current_vs_max_stats()** (5 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **._compute_max_dp_if_missing()** (3 connections) — `server/models/game.py`
- **.max_magic_points()** (3 connections) — `server/models/game.py`
- **.max_lucidity()** (3 connections) — `server/models/game.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
- **test_roll_character_stats_with_profession()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_with_class()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_without_class_or_profession()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_class_not_available()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_profession_meets_requirements_false()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_stats_validate_current_vs_max_stats_caps_dp()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_caps_magic_points()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_caps_lucidity()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_allows_valid_values()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_negative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_zero()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_different_attribute()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_dp_calculation()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- *... and 78 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (16 shared connections)
- [profession game service](profession_game_service.md) (9 shared connections)
- [command inventory models](command_inventory_models.md) (9 shared connections)
- [player service game](player_service_game.md) (4 shared connections)
- [command factories communication](command_factories_communication.md) (3 shared connections)
- [Exception Containers](Exception_Containers.md) (3 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [movement monitor game](movement_monitor_game.md) (2 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (2 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (2 shared connections)
- [game models stats](game_models_stats.md) (2 shared connections)
- [stats game generator](stats_game_generator.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 320 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*