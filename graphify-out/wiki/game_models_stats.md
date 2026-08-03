# game models stats

> 95 nodes

## Key Concepts

- **Stats** (80 connections) — `server/models/game.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **generate_random_stats()** (6 connections) — `server/game/stats_generator.py`
- **.validate_current_vs_max_stats()** (5 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **test_create_player_with_stats_character_limit()** (4 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_with_stats_name_exists()** (4 connections) — `server/tests/unit/game/test_player_service.py`
- **StrEnum** (3 connections)
- **._compute_max_dp_if_missing()** (3 connections) — `server/models/game.py`
- **.max_magic_points()** (3 connections) — `server/models/game.py`
- **.max_lucidity()** (3 connections) — `server/models/game.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **test_create_player_with_stats_success()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_stats_validate_current_vs_max_stats_caps_dp()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_caps_magic_points()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_caps_lucidity()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_allows_valid_values()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_negative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_zero()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_different_attribute()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_dp_calculation()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- *... and 70 more nodes in this community*

## Relationships

- [game models player](game_models_player.md) (11 shared connections)
- [character creation service](character_creation_service.md) (8 shared connections)
- [character creation validate](character_creation_validate.md) (7 shared connections)
- [Player Stats](Player_Stats.md) (6 shared connections)
- [player service game](player_service_game.md) (4 shared connections)
- [world models rationale](world_models_rationale.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [game weapon player](game_weapon_player.md) (3 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (2 shared connections)
- [stats game generator](stats_game_generator.md) (1 shared connections)
- [spell models rationale](spell_models_rationale.md) (1 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 299 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*