# spell registry

> 70 nodes

## Key Concepts

- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_registry.py** (15 connections) — `server/game/magic/spell_registry.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellMaterial** (13 connections) — `server/models/spell.py`
- **SpellEffectType** (9 connections) — `server/models/spell.py`
- **SpellSchool** (8 connections) — `server/models/spell.py`
- **SpellTargetType** (6 connections) — `server/models/spell.py`
- **SpellRangeType** (6 connections) — `server/models/spell.py`
- **.load_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- **.list_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- **StrEnum** (4 connections)
- **test_spell_mp_cost_validation_negative()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_lucidity_cost_validation_negative()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_with_materials()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **self_spell()** (3 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_spell_material_creation()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_default()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_false()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_is_mythos_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_is_mythos_false()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_requires_lucidity_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_requires_lucidity_false_zero()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_requires_lucidity_false_default()** (3 connections) — `server/tests/unit/models/test_spell.py`
- *... and 45 more nodes in this community*

## Relationships

- [Spell Targeting](Spell_Targeting.md) (26 shared connections)
- [. init ()](_init_%28%29.md) (19 shared connections)
- [Base](Base.md) (6 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [Any](Any.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)
- [combat taunt](combat_taunt.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 239 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*