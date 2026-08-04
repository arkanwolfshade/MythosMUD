# player service game

> 69 nodes

## Key Concepts

- **Stats** (88 connections) — `server/models/game.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_create_player_with_stats_character_limit()** (4 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_with_stats_success()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_stats_validate_current_vs_max_stats_caps_dp()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_caps_magic_points()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_caps_lucidity()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_validate_current_vs_max_stats_allows_valid_values()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_negative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_zero()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_different_attribute()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_dp_calculation()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_dp_calculation_alternative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_dp_with_none()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_magic_points_calculation()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_magic_points_calculation_alternative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_lucidity_calculation()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_lucidity_calculation_alternative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_lucid_true()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_lucid_false()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_corrupted_true()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_corrupted_false()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_delirious_true()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_delirious_false()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_positive()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- *... and 44 more nodes in this community*

## Relationships

- [command factories communication](command_factories_communication.md) (10 shared connections)
- [event connection helpers](event_connection_helpers.md) (10 shared connections)
- [services passive lucidity](services_passive_lucidity.md) (6 shared connections)
- [Player Stats](Player_Stats.md) (6 shared connections)
- [npc rationale extract](npc_rationale_extract.md) (6 shared connections)
- [profession game service](profession_game_service.md) (5 shared connections)
- [commands inventory put](commands_inventory_put.md) (3 shared connections)
- [player event state](player_event_state.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [service combat services](service_combat_services.md) (2 shared connections)
- [npc idle movement](npc_idle_movement.md) (2 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (2 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 239 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*