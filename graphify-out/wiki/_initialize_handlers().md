# . initialize handlers()

> 137 nodes

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
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **.get_uuid_for_string_id()** (7 connections) — `server/services/combat_service_npc.py`
- **combat_room_id_for_npc_spell()** (6 connections) — `server/game/magic/spell_effects_internal.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.get_original_string_id()** (6 connections) — `server/services/combat_service_npc.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- **_iter_active_combats()** (6 connections) — `server/services/combat_service_npc.py`
- *... and 112 more nodes in this community*

## Relationships

- [Any](Any.md) (46 shared connections)
- [.end combat()](end_combat%28%29.md) (25 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (20 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (19 shared connections)
- [message handler factory](message_handler_factory.md) (9 shared connections)
- [. init ()](_init_%28%29.md) (8 shared connections)
- [get health service()](get_health_service%28%29.md) (8 shared connections)
- [.model dump()](model_dump%28%29.md) (8 shared connections)
- [combat](combat.md) (7 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (6 shared connections)
- [test command parser](test_command_parser.md) (5 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`

## Audit Trail

- EXTRACTED: 579 (90%)
- INFERRED: 64 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*