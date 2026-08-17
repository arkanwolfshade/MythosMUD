# StatusEffect

> 22 nodes

## Key Concepts

- **StatusEffect** (31 connections) — `server/models/game.py`
- **test_game_status_effect.py** (15 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_creation()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_duration_validation_min()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_max()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_intensity_validation_min()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_at_duration()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_before_duration()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_is_active_permanent()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_status_effect_with_source()** (3 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Represents a status effect applied to a character.** (1 connections) — `server/models/game.py`
- **Unit tests for StatusEffect model.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect can be created with required fields.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect can have optional source.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns True for permanent effects (duration=0).** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns True when current_tick < duration.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test is_active returns False when current_tick >= duration.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect validates duration is >= 0.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect validates intensity is >= 1.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect validates intensity is <= 10.** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **Test StatusEffect rejects unknown fields (extra='forbid').** (1 connections) — `server/tests/unit/models/test_game_status_effect.py`

## Relationships

- [Player](Player.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (3 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (2 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*