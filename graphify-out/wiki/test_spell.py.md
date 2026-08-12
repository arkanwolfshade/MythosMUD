# test_spell.py

> 77 nodes

## Key Concepts

- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_registry.py** (15 connections) — `server/game/magic/spell_registry.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellMaterial** (13 connections) — `server/models/spell.py`
- **SpellEffectType** (10 connections) — `server/models/spell.py`
- **SpellSchool** (8 connections) — `server/models/spell.py`
- **SpellTargetType** (8 connections) — `server/models/spell.py`
- **SpellRangeType** (6 connections) — `server/models/spell.py`
- **.list_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- **self_spell()** (4 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_spell_with_materials()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **StrEnum** (4 connections)
- **.load_spells()** (3 connections) — `server/game/magic/spell_registry.py`
- **mock_target_resolution_service()** (3 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_resolve_spell_target_self_spell_no_target_resolves_self()** (3 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_resolve_spell_target_self_spell_with_target_returns_error()** (3 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_spell_default_values()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_is_mythos_false()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_is_mythos_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_lucidity_cost_validation_negative()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_default()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_false()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_creation()** (3 connections) — `server/tests/unit/models/test_spell.py`
- *... and 52 more nodes in this community*

## Relationships

- [Spell](Spell.md) (19 shared connections)
- [magic_service.py](magic_service.py.md) (19 shared connections)
- [Player](Player.md) (6 shared connections)
- [spell_effects.py](spell_effects.py.md) (3 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (1 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 248 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*