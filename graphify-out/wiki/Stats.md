# Stats

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

- [game.py](game.py.md) (35 shared connections)
- [character_creation.py](character_creation.py.md) (10 shared connections)
- [__init__.py](__init__.py.md) (9 shared connections)
- [test_character_creation_service.py](test_character_creation_service.py.md) (8 shared connections)
- [exceptions.py](exceptions.py.md) (7 shared connections)
- [test_player_service.py](test_player_service.py.md) (4 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [User](User.md) (3 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (2 shared connections)
- [Stats](Stats.md) (1 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

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