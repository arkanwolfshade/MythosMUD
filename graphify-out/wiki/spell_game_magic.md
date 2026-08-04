# spell game magic

> 154 nodes

## Key Concepts

- **TargetMatch** (158 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (124 connections) — `server/models/spell.py`
- **SpellTargetingService** (32 connections) — `server/game/magic/spell_targeting.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **test_spell_targeting.py** (28 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectPlayer** (14 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (12 connections)
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_corruption_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **._process_heal()** (8 connections) — `server/game/magic/spell_effects.py`
- **._process_teleport()** (8 connections) — `server/game/magic/spell_effects.py`
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **UUID** (8 connections)
- **._process_damage_to_npc()** (7 connections) — `server/game/magic/spell_effects.py`
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._match_combat_opponent()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._spell_player_persistence()** (6 connections) — `server/game/magic/spell_effects.py`
- **.process_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **._process_status_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- *... and 129 more nodes in this community*

## Relationships

- [coercion int inventory](coercion_int_inventory.md) (93 shared connections)
- [target resolution service](target_resolution_service.md) (31 shared connections)
- [retry nats handler](retry_nats_handler.md) (27 shared connections)
- [command factories communication](command_factories_communication.md) (19 shared connections)
- [player respawn event](player_respawn_event.md) (19 shared connections)
- [game models player](game_models_player.md) (15 shared connections)
- [NPC Combat](NPC_Combat.md) (12 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (12 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (10 shared connections)
- [subject nats manager](subject_nats_manager.md) (8 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (6 shared connections)
- [Item Instances](Item_Instances.md) (5 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 753 (92%)
- INFERRED: 68 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*