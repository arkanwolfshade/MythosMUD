# SpellEffectType

> 96 nodes

## Key Concepts

- **SpellEffectType** (45 connections) — `server/models/spell.py`
- **SpellSchool** (37 connections) — `server/models/spell.py`
- **SpellTargetType** (34 connections) — `server/models/spell.py`
- **SpellRangeType** (32 connections) — `server/models/spell.py`
- **test_spell.py** (32 connections) — `server/tests/unit/models/test_spell.py`
- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **test_spell_materials.py** (23 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_spell_costs.py** (20 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **_spell()** (15 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **_spell()** (10 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_get_combat_target_auto_selects_opponent()** (10 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **_spell()** (9 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **self_spell()** (8 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_spell_with_materials()** (8 connections) — `server/tests/unit/models/test_spell.py`
- **asyncio** (8 connections)
- **base_spell()** (7 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **area_spell()** (7 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **entity_spell()** (7 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_spell_default_values()** (7 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_is_mythos_false()** (7 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_is_mythos_true()** (7 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_lucidity_cost_validation_negative()** (7 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_mp_cost_validation_negative()** (7 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_requires_lucidity_false_default()** (7 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_requires_lucidity_false_zero()** (7 connections) — `server/tests/unit/models/test_spell.py`
- *... and 71 more nodes in this community*

## Relationships

- [magic_service.py](magic_service.py.md) (29 shared connections)
- [TargetMatch](TargetMatch.md) (24 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (11 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (10 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (10 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)

## Source Files

- `server/models/spell.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/game/magic/test_spell_registry.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 219 (66%)
- INFERRED: 111 (34%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*