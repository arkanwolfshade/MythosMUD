# Status Effect Model

> 28 nodes · cohesion 0.10

## Key Concepts

- **StatusEffect** (31 connections) — `server/models/game.py`
- **test_game_status_effect.py** (12 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **.add_status_effect()** (3 connections) — `server/models/game.py`
- **.is_active()** (3 connections) — `server/models/game.py`
- **test_status_effect_creation()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_duration_validation_min()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_max()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_min()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_at_duration()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_before_duration()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_permanent()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_with_source()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Check if the status effect is still active.** (1 connections) — `server/models/game.py`
- **Add a status effect to the player.          Args:             effect: StatusEffe** (1 connections) — `server/models/game.py`
- **Get all currently active status effects.          Args:             current_tick** (1 connections) — `server/models/game.py`
- **Represents a status effect applied to a character.** (1 connections) — `server/models/game.py`
- **Unit tests for StatusEffect model.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect can be created with required fields.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect can have optional source.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns True for permanent effects (duration=0).** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns True when current_tick < duration.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns False when current_tick >= duration.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect validates duration is >= 0.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- *... and 3 more nodes in this community*

## Relationships

- [[Player Model Inventory]] (7 shared connections)
- [[Game Magic Spell]] (5 shared connections)
- [[Admin NPC Schemas]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Player Schema Converter]] (2 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Memory Profiler Tools]] (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 94 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
