# TargetMatch

> 134 nodes

## Key Concepts

- **TargetMatch** (158 connections) — `server/schemas/shared/target_resolution.py`
- **SpellEffects** (55 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (47 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **asyncio** (29 connections)
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **SpellEffectsDeps** (20 connections) — `server/game/magic/spell_effects.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- **UUID** (8 connections)
- **._process_corruption_adjust()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_damage_to_npc()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (7 connections) — `server/game/magic/spell_effects.py`
- **test_negative_status_effect_blocked_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **._process_create_object()** (6 connections) — `server/game/magic/spell_effects.py`
- **.process_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_stat_modify()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_status_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_teleport()** (6 connections) — `server/game/magic/spell_effects.py`
- **._spell_player_persistence()** (6 connections) — `server/game/magic/spell_effects.py`
- **test_process_effect_flee_not_in_combat()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_publish_npc_spell_damage_syncs_participant_when_npc_room_missing()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_effects.py`
- *... and 109 more nodes in this community*

## Relationships

- [Spell](Spell.md) (47 shared connections)
- [AliasStorage](AliasStorage.md) (26 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (18 shared connections)
- [SpellEffectType](SpellEffectType.md) (13 shared connections)
- [run_flee_effect](run_flee_effect.md) (11 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (11 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (10 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (9 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (8 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (7 shared connections)
- [SpellRegistry](SpellRegistry.md) (6 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (6 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effects.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 405 (86%)
- INFERRED: 66 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*