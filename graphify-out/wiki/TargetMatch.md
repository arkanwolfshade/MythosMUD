# TargetMatch

> 359 nodes

## Key Concepts

- **TargetMatch** (158 connections) — `server/schemas/shared/target_resolution.py`
- **SpellEffects** (59 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (46 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **TargetResolutionResult** (40 connections) — `server/schemas/shared/target_resolution.py`
- **asyncio** (29 connections)
- **SpellEffectsDeps** (28 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **test_spell_targeting.py** (28 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **NpcSpellDamageTarget** (18 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectType** (16 connections) — `server/models/spell.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **TargetMetadata** (15 connections) — `server/schemas/shared/target_metadata.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **test_spell_effects_support.py** (13 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **asyncio** (12 connections)
- **PlayerPersistenceSpellPort** (11 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- *... and 334 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (71 shared connections)
- [PlayerService](PlayerService.md) (70 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (50 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (19 shared connections)
- [server/models/game.py](server-models-game.py.md) (18 shared connections)
- [run_flee_effect](run_flee_effect.md) (14 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (9 shared connections)
- [test_target_resolution_service.py](test_target_resolution_service.py.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [MovementService](MovementService.md) (4 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/models/spell.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`
- `server/tests/unit/game/magic/test_spell_effects_stats.py`
- `server/tests/unit/game/magic/test_spell_effects_support.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 971 (95%)
- INFERRED: 47 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*