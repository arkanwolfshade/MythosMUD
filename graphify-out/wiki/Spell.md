# Spell

> 128 nodes

## Key Concepts

- **Spell** (136 connections) — `server/models/spell.py`
- **SpellEffectType** (45 connections) — `server/models/spell.py`
- **SpellSchool** (37 connections) — `server/models/spell.py`
- **SpellTargetType** (34 connections) — `server/models/spell.py`
- **SpellRangeType** (32 connections) — `server/models/spell.py`
- **test_spell.py** (32 connections) — `server/tests/unit/models/test_spell.py`
- **spell.py** (29 connections) — `server/models/spell.py`
- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **test_spell_materials.py** (23 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_magic_healing_events.py** (21 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_spell_costs.py** (20 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_spell_registry.py** (19 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **_spell()** (15 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **_spell()** (10 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_get_combat_target_auto_selects_opponent()** (10 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **_spell()** (9 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **self_spell()** (8 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_spell_with_materials()** (8 connections) — `server/tests/unit/models/test_spell.py`
- **asyncio** (8 connections)
- **base_spell()** (7 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **area_spell()** (7 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **entity_spell()** (7 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- *... and 103 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (37 shared connections)
- [PlayerService](PlayerService.md) (32 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (23 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (15 shared connections)
- [TargetType](TargetType.md) (13 shared connections)
- [MagicServiceHealingMixin](MagicServiceHealingMixin.md) (13 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (12 shared connections)
- [SpellLearningService](SpellLearningService.md) (10 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (8 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [get_session_maker](get_session_maker.md) (7 shared connections)

## Source Files

- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/game/magic/test_spell_registry.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 339 (64%)
- INFERRED: 188 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*