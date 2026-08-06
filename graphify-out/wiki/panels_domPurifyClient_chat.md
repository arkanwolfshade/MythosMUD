# panels domPurifyClient chat

> 164 nodes

## Key Concepts

- **TargetMatch** (158 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (124 connections) — `server/models/spell.py`
- **SpellTargetingService** (32 connections) — `server/game/magic/spell_targeting.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **test_spell_targeting.py** (28 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **UUID** (12 connections)
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_corruption_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **._process_heal()** (8 connections) — `server/game/magic/spell_effects.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- *... and 139 more nodes in this community*

## Relationships

- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (47 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (46 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (46 shared connections)
- [spell game magic](spell_game_magic.md) (37 shared connections)
- [player respawn event](player_respawn_event.md) (19 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (13 shared connections)
- [room renderer functions](room_renderer_functions.md) (12 shared connections)
- [services ascii map](services_ascii_map.md) (9 shared connections)
- [subject nats manager](subject_nats_manager.md) (8 shared connections)
- [combat services turn](combat_services_turn.md) (7 shared connections)
- [command utility models](command_utility_models.md) (7 shared connections)
- [Error Conversion](Error_Conversion.md) (7 shared connections)

## Source Files

- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_targeting.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 909 (93%)
- INFERRED: 64 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*