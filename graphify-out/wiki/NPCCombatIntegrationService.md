# NPCCombatIntegrationService

> 170 nodes

## Key Concepts

- **NPCCombatIntegrationService** (86 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (47 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **NPCCombatUUIDMapping** (38 connections) — `server/services/npc_combat_uuid_mapping.py`
- **asyncio** (25 connections)
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_uuid_mapping.py** (8 connections) — `server/services/npc_combat_uuid_mapping.py`
- **integration_service()** (7 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **UUID** (7 connections)
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **_StubConfigRoot** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._init_persistence_and_event_bus()** (5 connections) — `server/services/npc_combat_integration_service.py`
- **test_validate_combat_location_limbo_cross_room_uses_debug()** (5 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **._complete_player_attack_on_npc_after_grace()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_player_attack_on_npc()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **._init_combat_service()** (4 connections) — `server/services/npc_combat_integration_service.py`
- **.convert_to_uuid()** (4 connections) — `server/services/npc_combat_uuid_mapping.py`
- **test_end_combat_if_participant_in_combat_ends_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_in_combat_no_combat()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_end_combat_if_participant_skips_when_player_id_unparseable()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_get_integration_config()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_delegates_to_handle_npc_attack_on_player()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_false_when_npc_dead()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **test_handle_npc_attack_on_player_false_without_combat_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- *... and 145 more nodes in this community*

## Relationships

- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (16 shared connections)
- [test_npc_combat_integration_service_player_attacks.py](test_npc_combat_integration_service_player_attacks.py.md) (11 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (10 shared connections)
- [EventBus](EventBus.md) (9 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (4 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [CombatMessagingService](CombatMessagingService.md) (2 shared connections)

## Source Files

- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_uuid_mapping.py`

## Audit Trail

- EXTRACTED: 293 (85%)
- INFERRED: 52 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*