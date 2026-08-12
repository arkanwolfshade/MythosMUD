# Spell

> 70 nodes

## Key Concepts

- **Spell** (92 connections) — `server/models/spell.py`
- **SpellEffects** (54 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **UUID** (8 connections)
- **._process_corruption_adjust()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_damage_to_npc()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_heal()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (7 connections) — `server/game/magic/spell_effects.py`
- **._process_create_object()** (6 connections) — `server/game/magic/spell_effects.py`
- **.process_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_stat_modify()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_status_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_teleport()** (6 connections) — `server/game/magic/spell_effects.py`
- **._spell_player_persistence()** (6 connections) — `server/game/magic/spell_effects.py`
- **_create_object_for_room()** (6 connections) — `server/game/magic/spell_effects_support.py`
- **Any** (6 connections)
- **._resolve_room_for_npc_spell_publish()** (5 connections) — `server/game/magic/spell_effects.py`
- **_build_stat_modifications()** (5 connections) — `server/game/magic/spell_effects_support.py`
- *... and 45 more nodes in this community*

## Relationships

- [magic_service.py](magic_service.py.md) (26 shared connections)
- [spell_effects.py](spell_effects.py.md) (24 shared connections)
- [TargetMatch](TargetMatch.md) (21 shared connections)
- [test_spell.py](test_spell.py.md) (19 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (11 shared connections)
- [SpellLearningService](SpellLearningService.md) (10 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (8 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (5 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [SpellMaterialsService](SpellMaterialsService.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_registry.py`
- `server/models/spell.py`

## Audit Trail

- EXTRACTED: 250 (90%)
- INFERRED: 27 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*