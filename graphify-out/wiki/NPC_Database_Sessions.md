# NPC Database Sessions

> 84 nodes

## Key Concepts

- **Stats** (80 connections) — `server/models/game.py`
- **generate_random_stats()** (6 connections) — `server/game/stats_generator.py`
- **.validate_current_vs_max_stats()** (5 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **._compute_max_dp_if_missing()** (3 connections) — `server/models/game.py`
- **.max_magic_points()** (3 connections) — `server/models/game.py`
- **.max_lucidity()** (3 connections) — `server/models/game.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
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
- *... and 59 more nodes in this community*

## Relationships

- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (32 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (9 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (6 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (5 shared connections)
- [Command Factory Creators](Command_Factory_Creators.md) (4 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (2 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (1 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (1 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 243 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*