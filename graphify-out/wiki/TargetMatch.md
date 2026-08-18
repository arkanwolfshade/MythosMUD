# TargetMatch

> 229 nodes

## Key Concepts

- **TargetMatch** (158 connections) — `server/schemas/shared/target_resolution.py`
- **SpellEffects** (55 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (47 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (29 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **asyncio** (29 connections)
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectsDeps** (20 connections) — `server/game/magic/spell_effects.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **asyncio** (12 connections)
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **UUID** (10 connections)
- **_add_healing_threat_if_in_combat()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **coerce_effect_int_times_mastery()** (9 connections) — `server/game/magic/spell_effects_internal.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- *... and 204 more nodes in this community*

## Relationships

- [Spell](Spell.md) (52 shared connections)
- [CombatService](CombatService.md) (28 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (25 shared connections)
- [TargetType](TargetType.md) (16 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (15 shared connections)
- [run_flee_effect](run_flee_effect.md) (13 shared connections)
- [server/models/game.py](server-models-game.py.md) (13 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (11 shared connections)
- [magic_service.py](magic_service.py.md) (10 shared connections)
- [CombatParticipant](CombatParticipant.md) (10 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (10 shared connections)
- [get_logger](get_logger.md) (8 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 639 (87%)
- INFERRED: 94 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*