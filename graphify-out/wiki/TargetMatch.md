# TargetMatch

> 227 nodes

## Key Concepts

- **TargetMatch** (161 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (136 connections) — `server/models/spell.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (29 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects_support.py** (14 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **asyncio** (12 connections)
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **process_create_object_effect()** (11 connections) — `server/game/magic/spell_effects_support.py`
- **process_stat_modify_effect()** (11 connections) — `server/game/magic/spell_effects_support.py`
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- *... and 202 more nodes in this community*

## Relationships

- [SpellEffects](SpellEffects.md) (59 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (53 shared connections)
- [SpellEffectType](SpellEffectType.md) (48 shared connections)
- [magic_service.py](magic_service.py.md) (35 shared connections)
- [CombatService](CombatService.md) (31 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (16 shared connections)
- [run_flee_effect](run_flee_effect.md) (15 shared connections)
- [SpellLearningService](SpellLearningService.md) (11 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [Stats](Stats.md) (5 shared connections)
- [StatusEffect](StatusEffect.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_targeting.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_effects_stats.py`
- `server/tests/unit/game/magic/test_spell_effects_support.py`

## Audit Trail

- EXTRACTED: 753 (88%)
- INFERRED: 102 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*