# spell game magic

> 167 nodes

## Key Concepts

- **TargetMatch** (158 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (124 connections) — `server/models/spell.py`
- **SpellEffects** (61 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (45 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **UUID** (12 connections)
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_corruption_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **._process_heal()** (8 connections) — `server/game/magic/spell_effects.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- **._process_teleport()** (8 connections) — `server/game/magic/spell_effects.py`
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **._process_damage_to_npc()** (7 connections) — `server/game/magic/spell_effects.py`
- **._spell_player_persistence()** (6 connections) — `server/game/magic/spell_effects.py`
- **.process_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_status_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_stat_modify()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_create_object()** (6 connections) — `server/game/magic/spell_effects.py`
- *... and 142 more nodes in this community*

## Relationships

- [retry nats handler](retry_nats_handler.md) (42 shared connections)
- [game models player](game_models_player.md) (35 shared connections)
- [target resolution service](target_resolution_service.md) (31 shared connections)
- [NPC Combat](NPC_Combat.md) (29 shared connections)
- [command factories communication](command_factories_communication.md) (21 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (19 shared connections)
- [player respawn event](player_respawn_event.md) (19 shared connections)
- [uuid npc combat](uuid_npc_combat.md) (12 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (11 shared connections)
- [subject nats manager](subject_nats_manager.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [skill service game](skill_service_game.md) (8 shared connections)

## Source Files

- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_support.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 813 (92%)
- INFERRED: 68 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*