# TargetMatch

> 155 nodes

## Key Concepts

- **TargetMatch** (121 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (92 connections) — `server/models/spell.py`
- **SpellEffects** (54 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_targeting.py** (20 connections) — `server/game/magic/spell_targeting.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellEffectType** (10 connections) — `server/models/spell.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **spell_materials.py** (10 connections) — `server/game/magic/spell_materials.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **SpellTargetType** (8 connections) — `server/models/spell.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **UUID** (8 connections)
- *... and 130 more nodes in this community*

## Relationships

- [magic_service.py](magic_service.py.md) (59 shared connections)
- [spell_effects_heal.py](spell_effects_heal.py.md) (37 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (26 shared connections)
- [server/models/game.py](server-models-game.py.md) (25 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (23 shared connections)
- [CombatService](CombatService.md) (18 shared connections)
- [test_spell.py](test_spell.py.md) (17 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (17 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (16 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [run_flee_effect](run_flee_effect.md) (11 shared connections)
- [SpellLearningService](SpellLearningService.md) (10 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 906 (95%)
- INFERRED: 49 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*