# TargetMatch

> 222 nodes

## Key Concepts

- **TargetMatch** (161 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (136 connections) — `server/models/spell.py`
- **SpellEffects** (58 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (53 connections) — `server/game/magic/spell_effects.py`
- **_MagicServiceCore** (44 connections) — `server/game/magic/magic_service.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **UUID** (21 connections)
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **JsonMap** (12 connections)
- **asyncio** (12 connections)
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **process_create_object_effect()** (11 connections) — `server/game/magic/spell_effects_support.py`
- **process_stat_modify_effect()** (11 connections) — `server/game/magic/spell_effects_support.py`
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- *... and 197 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (53 shared connections)
- [SpellEffectType](SpellEffectType.md) (37 shared connections)
- [CombatService](CombatService.md) (35 shared connections)
- [TargetType](TargetType.md) (35 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (31 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (20 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (16 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [SpellLearningService](SpellLearningService.md) (11 shared connections)
- [test_spell_effects_support.py](test_spell_effects_support.py.md) (10 shared connections)
- [TauntCommandHandler](TauntCommandHandler.md) (9 shared connections)
- [.resolve_target](resolve_target.md) (7 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_support.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 755 (86%)
- INFERRED: 124 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*