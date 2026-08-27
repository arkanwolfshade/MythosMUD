# TargetMatch

> 129 nodes

## Key Concepts

- **TargetMatch** (161 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (136 connections) — `server/models/spell.py`
- **test_spell_effects_heal.py** (29 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **asyncio** (12 connections)
- **._execute_instant_or_delayed_cast()** (10 connections) — `server/game/magic/magic_service.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **._get_spell_and_validate_target()** (9 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (9 connections) — `server/game/magic/magic_service.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- **UUID** (8 connections)
- **Any** (8 connections)
- **UUID** (8 connections)
- *... and 104 more nodes in this community*

## Relationships

- [SpellEffects](SpellEffects.md) (84 shared connections)
- [SpellEffectType](SpellEffectType.md) (37 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (29 shared connections)
- [get_username_from_user](get_username_from_user.md) (28 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (17 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (16 shared connections)
- [run_flee_effect](run_flee_effect.md) (13 shared connections)
- [PlayerService](PlayerService.md) (11 shared connections)
- [SpellLearningService](SpellLearningService.md) (11 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (11 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (10 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (9 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_targeting.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 553 (88%)
- INFERRED: 77 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*