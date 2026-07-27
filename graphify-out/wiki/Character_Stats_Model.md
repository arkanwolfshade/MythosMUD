# Character Stats Model

> 75 nodes · cohesion 0.04

## Key Concepts

- **Stats** (73 connections) — `server/models/game.py`
- **test_game_stats_methods.py** (30 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **.validate_current_vs_max_stats()** (5 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
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
- **test_stats_max_dp_calculation_alternative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_dp_with_none()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_lucidity_calculation()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_max_lucidity_calculation_alternative()** (3 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- *... and 50 more nodes in this community*

## Relationships

- [[NPC Admin API]] (9 shared connections)
- [[Character Creation API]] (5 shared connections)
- [[Player Service Tests]] (4 shared connections)
- [[Player Schema Models]] (4 shared connections)
- [[Character Creation Service]] (3 shared connections)
- [[Player Model Inventory]] (3 shared connections)
- [[Admin NPC Schemas]] (2 shared connections)
- [[Player Schema Converter]] (2 shared connections)
- [[Game . Compute Max]] (2 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Memory Profiler Tools]] (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 256 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
