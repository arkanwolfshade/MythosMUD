# NPC Database Sessions

> 92 nodes

## Key Concepts

- **Stats** (80 connections) — `server/models/game.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
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
- **test_stats_max_dp_calculation_alternative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_dp_with_none()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- *... and 67 more nodes in this community*

## Relationships

- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (8 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (4 shared connections)
- [Command Factory Creators](Command_Factory_Creators.md) (4 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (3 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (3 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (2 shared connections)
- [Real-Time Architecture Docs](Real-Time_Architecture_Docs.md) (2 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (2 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (2 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 279 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*