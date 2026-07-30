# . initialize handlers()

> 158 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **UUID** (20 connections)
- **get_combat_id_for_npc()** (13 connections) — `server/services/combat_service_npc.py`
- **UUID** (11 connections)
- **get_npc_participant_current_room()** (11 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (10 connections) — `server/game/magic/spell_effects_internal.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (10 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (9 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **DataProviderProtocol** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_id_for_npc_via_mapping()** (8 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **PlayerLifecycleServices** (8 connections) — `server/services/combat_service_types.py`
- **test_combat_service_npc_in_combat.py** (8 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **.get_uuid_for_string_id()** (7 connections) — `server/services/combat_service_npc.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **combat_room_id_for_npc_spell()** (6 connections) — `server/game/magic/spell_effects_internal.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.get_original_string_id()** (6 connections) — `server/services/combat_service_npc.py`
- *... and 133 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (75 shared connections)
- [. init ()](_init_%28%29.md) (36 shared connections)
- [Any](Any.md) (12 shared connections)
- [CombatService](CombatService.md) (11 shared connections)
- [get health service()](get_health_service%28%29.md) (11 shared connections)
- [message handler factory](message_handler_factory.md) (8 shared connections)
- [test exploration service](test_exploration_service.md) (7 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (6 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (5 shared connections)
- [combat flee](combat_flee.md) (5 shared connections)
- [combat](combat.md) (5 shared connections)
- [test command parser](test_command_parser.md) (4 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 624 (91%)
- INFERRED: 64 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*