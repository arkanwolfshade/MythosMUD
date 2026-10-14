# TargetMatch

> 193 nodes

## Key Concepts

- **TargetMatch** (173 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (141 connections) — `server/models/spell.py`
- **_MagicServiceCore** (44 connections) — `server/game/magic/magic_service.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (21 connections)
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **JsonMap** (12 connections)
- **asyncio** (12 connections)
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (10 connections) — `server/game/magic/magic_service.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (10 connections)
- *... and 168 more nodes in this community*

## Relationships

- [SpellEffects](SpellEffects.md) (70 shared connections)
- [SpellEffectType](SpellEffectType.md) (31 shared connections)
- [TargetType](TargetType.md) (28 shared connections)
- [magic_service.py](magic_service.py.md) (23 shared connections)
- [CombatService](CombatService.md) (22 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (20 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (17 shared connections)
- [run_flee_effect](run_flee_effect.md) (13 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (12 shared connections)
- [SpellLearningService](SpellLearningService.md) (11 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (11 shared connections)
- [get_logger](get_logger.md) (9 shared connections)

## Source Files

- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`

## Audit Trail

- EXTRACTED: 688 (87%)
- INFERRED: 107 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*