# CombatService

> 180 nodes

## Key Concepts

- **CombatService** (173 connections) — `server/services/combat_service.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (30 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **UUID** (20 connections)
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (11 connections) — `server/services/combat_service_npc.py`
- **resolve_npc_participant_id_in_combat()** (11 connections) — `server/services/combat_service_npc.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **UUID** (10 connections)
- **get_combat_id_for_npc_via_mapping()** (9 connections) — `server/services/combat_service_npc.py`
- **get_participant_current_room()** (9 connections) — `server/services/combat_service_npc.py`
- **sync_npc_participant_dp_after_spell_damage()** (9 connections) — `server/services/combat_service_npc.py`
- **_fallback_find_combat_id_for_npc()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_by_participant()** (8 connections) — `server/services/combat_service_npc.py`
- **get_npc_participant_current_room()** (8 connections) — `server/services/combat_service_npc.py`
- **is_npc_in_combat_sync()** (8 connections) — `server/services/combat_service_npc.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **DataProviderProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **UUIDMappingProtocol** (7 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_string_id_mapping()** (7 connections) — `server/services/combat_service_npc.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **_get_data_provider()** (6 connections) — `server/services/combat_service_npc.py`
- **_iter_active_combats()** (6 connections) — `server/services/combat_service_npc.py`
- **npc_in_combat_by_uuid_lookup()** (6 connections) — `server/services/combat_service_npc.py`
- *... and 155 more nodes in this community*

## Relationships

- [combat_service.py](combat_service.py.md) (47 shared connections)
- [CombatInstance](CombatInstance.md) (34 shared connections)
- [TargetMatch](TargetMatch.md) (26 shared connections)
- [CombatParticipant](CombatParticipant.md) (22 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (10 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (8 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (6 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (3 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_combat_service_npc_helpers.py`

## Audit Trail

- EXTRACTED: 389 (82%)
- INFERRED: 87 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*