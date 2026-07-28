# Server Models (13)

> 60 nodes

## Key Concepts

- **Spell** (84 connections) — `server/models/spell.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **SpellMaterial** (13 connections) — `server/models/spell.py`
- **.load_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- **test_spell_mp_cost_validation_negative()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_lucidity_cost_validation_negative()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_with_materials()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **.get_spell()** (3 connections) — `server/game/magic/spell_registry.py`
- **.get_spell_by_name()** (3 connections) — `server/game/magic/spell_registry.py`
- **.search_spells()** (3 connections) — `server/game/magic/spell_registry.py`
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
- **test_spell_default_values()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_with_effect_data()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **Test SpellTargetType enum contains expected values.** (3 connections) — `server/tests/unit/models/test_spell.py`
- **Test requires_lucidity returns True when lucidity_cost > 0.** (3 connections) — `server/tests/unit/models/test_spell.py`
- **BaseModel** (2 connections)
- *... and 35 more nodes in this community*

## Relationships

- [Server Game (4)](Server_Game_%284%29.md) (26 shared connections)
- [Server Game (2)](Server_Game_%282%29.md) (11 shared connections)
- [Server Game (18)](Server_Game_%2818%29.md) (7 shared connections)
- [Server Game (7)](Server_Game_%287%29.md) (7 shared connections)
- [Server Game (24)](Server_Game_%2824%29.md) (7 shared connections)
- [Server Models (6)](Server_Models_%286%29.md) (6 shared connections)
- [Server Realtime (48)](Server_Realtime_%2848%29.md) (3 shared connections)
- [Server Game (14)](Server_Game_%2814%29.md) (3 shared connections)
- [Server Game (34)](Server_Game_%2834%29.md) (3 shared connections)
- [Server Models (14)](Server_Models_%2814%29.md) (2 shared connections)
- [Server Game (40)](Server_Game_%2840%29.md) (2 shared connections)
- [Server Utils](Server_Utils.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 229 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*