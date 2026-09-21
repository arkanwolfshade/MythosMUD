# TargetMatch

> 132 nodes

## Key Concepts

- **TargetMatch** (161 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (139 connections) — `server/models/spell.py`
- **SpellEffects** (58 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **asyncio** (12 connections)
- **._execute_instant_or_delayed_cast()** (10 connections) — `server/game/magic/magic_service.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **._get_spell_and_validate_target()** (9 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (9 connections) — `server/game/magic/magic_service.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- **UUID** (8 connections)
- **UUID** (8 connections)
- **._handle_instant_cast()** (7 connections) — `server/game/magic/magic_service.py`
- **._validate_spell_casting()** (7 connections) — `server/game/magic/magic_service.py`
- **_is_heal_other_self_target()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **._process_corruption_adjust()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_damage_to_npc()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_heal()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (7 connections) — `server/game/magic/spell_effects.py`
- *... and 107 more nodes in this community*

## Relationships

- [spell_effects.py](spell_effects.py.md) (49 shared connections)
- [SpellEffectType](SpellEffectType.md) (31 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (30 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (29 shared connections)
- [run_flee_effect](run_flee_effect.md) (26 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (22 shared connections)
- [magic_service.py](magic_service.py.md) (20 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (18 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (16 shared connections)
- [CombatInstance](CombatInstance.md) (14 shared connections)
- [SpellCostsService](SpellCostsService.md) (12 shared connections)
- [TargetType](TargetType.md) (11 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 517 (85%)
- INFERRED: 93 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*