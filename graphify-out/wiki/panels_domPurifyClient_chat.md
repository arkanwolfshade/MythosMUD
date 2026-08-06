# panels domPurifyClient chat

> 137 nodes

## Key Concepts

- **TargetMatch** (158 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (124 connections) — `server/models/spell.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **test_spell_targeting.py** (28 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
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
- **._process_teleport()** (8 connections) — `server/game/magic/spell_effects.py`
- **Any** (8 connections)
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- *... and 112 more nodes in this community*

## Relationships

- [container persistence rationale](container_persistence_rationale.md) (48 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (44 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (42 shared connections)
- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (34 shared connections)
- [player respawn event](player_respawn_event.md) (23 shared connections)
- [cache lru caching](cache_lru_caching.md) (13 shared connections)
- [commands position system](commands_position_system.md) (12 shared connections)
- [Item Instances](Item_Instances.md) (8 shared connections)
- [combat services turn](combat_services_turn.md) (7 shared connections)
- [subject nats manager](subject_nats_manager.md) (7 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (5 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (5 shared connections)

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

- EXTRACTED: 798 (94%)
- INFERRED: 50 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*