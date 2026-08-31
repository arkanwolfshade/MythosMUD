# TargetMatch

> 140 nodes

## Key Concepts

- **TargetMatch** (161 connections) — `server/schemas/shared/target_resolution.py`
- **SpellEffects** (55 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (47 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_spell_effects_heal.py** (29 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **asyncio** (29 connections)
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectsDeps** (20 connections) — `server/game/magic/spell_effects.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **asyncio** (12 connections)
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- **UUID** (8 connections)
- **_is_heal_other_self_target()** (7 connections) — `server/game/magic/spell_effects_heal.py`
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
- *... and 115 more nodes in this community*

## Relationships

- [spell_effects.py](spell_effects.py.md) (46 shared connections)
- [Spell](Spell.md) (41 shared connections)
- [run_flee_effect](run_flee_effect.md) (19 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (18 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (13 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (12 shared connections)
- [test_spell_effects_support.py](test_spell_effects_support.py.md) (8 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (7 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (7 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (6 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 451 (87%)
- INFERRED: 70 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*