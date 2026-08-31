# TargetMatch

> 167 nodes

## Key Concepts

- **TargetMatch** (161 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (136 connections) — `server/models/spell.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (29 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **asyncio** (12 connections)
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **UUID** (10 connections)
- **_add_healing_threat_if_in_combat()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **coerce_effect_int_times_mastery()** (9 connections) — `server/game/magic/spell_effects_internal.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **_steal_life_publish_npc_events()** (8 connections) — `server/game/magic/spell_effects_heal.py`
- **combat_room_id_for_npc_spell()** (8 connections) — `server/game/magic/spell_effects_internal.py`
- *... and 142 more nodes in this community*

## Relationships

- [SpellEffects](SpellEffects.md) (50 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (32 shared connections)
- [SpellEffectType](SpellEffectType.md) (29 shared connections)
- [CombatInstance](CombatInstance.md) (27 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (20 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (19 shared connections)
- [CombatService](CombatService.md) (19 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [server/models/game.py](server-models-game.py.md) (17 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (16 shared connections)
- [run_flee_effect](run_flee_effect.md) (12 shared connections)
- [SpellLearningService](SpellLearningService.md) (10 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`

## Audit Trail

- EXTRACTED: 583 (86%)
- INFERRED: 95 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*