# TargetMatch

> 455 nodes

## Key Concepts

- **TargetMatch** (158 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (136 connections) — `server/models/spell.py`
- **SpellEffects** (55 connections) — `server/game/magic/spell_effects.py`
- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (47 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **SpellEffectType** (45 connections) — `server/models/spell.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellSchool** (37 connections) — `server/models/spell.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **SpellTargetType** (34 connections) — `server/models/spell.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **SpellRangeType** (32 connections) — `server/models/spell.py`
- **test_spell.py** (32 connections) — `server/tests/unit/models/test_spell.py`
- **spell.py** (29 connections) — `server/models/spell.py`
- **test_spell_effects_heal.py** (29 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **asyncio** (29 connections)
- **test_spell_targeting.py** (29 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **test_magic_healing_events.py** (21 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **SpellEffectsDeps** (20 connections) — `server/game/magic/spell_effects.py`
- **test_spell_costs.py** (20 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- *... and 430 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (50 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (50 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (34 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (32 shared connections)
- [run_flee_effect](run_flee_effect.md) (32 shared connections)
- [SpellMaterial](SpellMaterial.md) (31 shared connections)
- [SpellLearningService](SpellLearningService.md) (28 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (20 shared connections)
- [PlayerSpellRepository](PlayerSpellRepository.md) (14 shared connections)
- [PlayerService](PlayerService.md) (11 shared connections)
- [Player](Player.md) (11 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`

## Audit Trail

- EXTRACTED: 1225 (81%)
- INFERRED: 284 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*