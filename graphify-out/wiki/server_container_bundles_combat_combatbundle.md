# server container bundles combat combatbundle

> 154 nodes

## Key Concepts

- **CombatService** (148 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (31 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **UUID** (20 connections)
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **UUID** (10 connections)
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (9 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **combat_room_id_for_npc_spell()** (8 connections) — `server/game/magic/spell_effects_internal.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (8 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (8 connections) — `server/services/combat_service_npc.py`
- **test_spell_effects_internal.py** (8 connections) — `server/tests/unit/game/magic/test_spell_effects_internal.py`
- **DataProviderProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **npc_in_combat_by_string_id_mapping()** (7 connections) — `server/services/combat_service_npc.py`
- **coerce_effect_float_times_mastery_as_int()** (6 connections) — `server/game/magic/spell_effects_internal.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- *... and 129 more nodes in this community*

## Relationships

- [server app game tick counter](server_app_game_tick_counter.md) (32 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (29 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (25 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (16 shared connections)
- [server events combat events](server_events_combat_events.md) (11 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (8 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (8 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (6 shared connections)
- [server models combat combatresult](server_models_combat_combatresult.md) (6 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (5 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (4 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (4 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`

## Audit Trail

- EXTRACTED: 356 (83%)
- INFERRED: 75 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*