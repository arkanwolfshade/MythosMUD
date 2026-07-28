# Character Stats Model

> 95 nodes · cohesion 0.02

## Key Concepts

- **Stats** (80 connections) — `server/models/game.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **generate_random_stats()** (6 connections) — `server/game/stats_generator.py`
- **.validate_current_vs_max_stats()** (5 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/game.py`
- **test_create_player_with_stats_character_limit()** (4 connections) — `server/tests/unit/game/test_player_service.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
- **._compute_max_dp_if_missing()** (3 connections) — `server/models/game.py`
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **.max_lucidity()** (3 connections) — `server/models/game.py`
- **.max_magic_points()** (3 connections) — `server/models/game.py`
- **test_stats_get_attribute_modifier_different_attribute()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_negative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_none()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_positive()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_get_attribute_modifier_zero()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_corrupted_false()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_corrupted_true()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_delirious_false()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_delirious_true()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_lucid_false()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_is_lucid_true()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_dp_calculation()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- *... and 70 more nodes in this community*

## Relationships

- [Player Combat XP](Player_Combat_XP.md) (35 shared connections)
- [Player Effects API](Player_Effects_API.md) (10 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (8 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (7 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (6 shared connections)
- [API Test Fixtures](API_Test_Fixtures.md) (4 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (3 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (3 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (2 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)
- [Cursor Commands Remediation](Cursor_Commands_Remediation.md) (1 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 281 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*