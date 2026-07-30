# . initialize handlers()

> 200 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **UUID** (20 connections)
- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **combat_service_events.py** (14 connections) — `server/services/combat_service_events.py`
- **get_combat_id_for_npc()** (13 connections) — `server/services/combat_service_npc.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **combat_service_end.py** (11 connections) — `server/services/combat_service_end.py`
- **UUID** (11 connections)
- **get_npc_participant_current_room()** (11 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (10 connections) — `server/game/magic/spell_effects_internal.py`
- **validate_melee_or_end_combat()** (10 connections) — `server/services/combat_service_attack.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (10 connections) — `server/services/combat_service_npc.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (9 connections) — `server/services/combat_service_attack.py`
- **resolve_npc_participant_id_in_combat()** (9 connections) — `server/services/combat_service_npc.py`
- **handle_combat_completion()** (8 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (8 connections) — `server/services/combat_service_attack.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc_via_mapping()** (8 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- *... and 175 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (61 shared connections)
- [Any](Any.md) (44 shared connections)
- [. init ()](_init_%28%29.md) (39 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (29 shared connections)
- [CombatService](CombatService.md) (16 shared connections)
- [get health service()](get_health_service%28%29.md) (14 shared connections)
- [test exploration service](test_exploration_service.md) (13 shared connections)
- [message handler factory](message_handler_factory.md) (12 shared connections)
- [world](world.md) (9 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (7 shared connections)
- [combat flee](combat_flee.md) (6 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (5 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/container/bundles/combat.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/aggro_threat.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 916 (93%)
- INFERRED: 72 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*