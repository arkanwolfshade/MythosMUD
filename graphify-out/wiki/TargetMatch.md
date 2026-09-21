# TargetMatch

> 129 nodes

## Key Concepts

- **TargetMatch** (161 connections) — `server/schemas/shared/target_resolution.py`
- **SpellEffects** (58 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (46 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **asyncio** (29 connections)
- **SpellEffectsDeps** (20 connections) — `server/game/magic/spell_effects.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- **UUID** (8 connections)
- **._process_corruption_adjust()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_damage_to_npc()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_heal()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (7 connections) — `server/game/magic/spell_effects.py`
- **test_negative_status_effect_blocked_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **._process_create_object()** (6 connections) — `server/game/magic/spell_effects.py`
- **.process_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_stat_modify()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_status_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_teleport()** (6 connections) — `server/game/magic/spell_effects.py`
- **test_process_effect_flee_not_in_combat()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_publish_npc_spell_damage_syncs_participant_when_npc_room_missing()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- *... and 104 more nodes in this community*

## Relationships

- [Spell](Spell.md) (52 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (22 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (19 shared connections)
- [SpellEffectType](SpellEffectType.md) (17 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (16 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (12 shared connections)
- [run_flee_effect](run_flee_effect.md) (11 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (10 shared connections)
- [magic_service.py](magic_service.py.md) (9 shared connections)
- [get_config](get_config.md) (9 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (8 shared connections)
- [CombatService](CombatService.md) (7 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/combat_taunt.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 405 (87%)
- INFERRED: 63 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*