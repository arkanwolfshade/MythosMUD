# TargetMatch

> 255 nodes

## Key Concepts

- **TargetMatch** (161 connections) — `server/schemas/shared/target_resolution.py`
- **SpellEffects** (58 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (53 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (46 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **asyncio** (29 connections)
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
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
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **UUID** (10 connections)
- *... and 230 more nodes in this community*

## Relationships

- [Spell](Spell.md) (54 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (30 shared connections)
- [CombatService](CombatService.md) (26 shared connections)
- [run_flee_effect](run_flee_effect.md) (24 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (15 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (13 shared connections)
- [magic_service.py](magic_service.py.md) (12 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (11 shared connections)
- [combat_service.py](combat_service.py.md) (8 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (6 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 711 (87%)
- INFERRED: 109 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*