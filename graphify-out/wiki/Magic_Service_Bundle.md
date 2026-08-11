# Magic Service Bundle

> 318 nodes

## Key Concepts

- **NPCCombatIntegrationService** (90 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (44 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **NPCCombatUUIDMapping** (39 connections) — `server/services/npc_combat_uuid_mapping.py`
- **NPCCombatDataProvider** (30 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatMemory** (29 connections) — `server/services/npc_combat_memory.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatRewards** (19 connections) — `server/services/npc_combat_rewards.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_handlers.py** (16 connections) — `server/services/npc_combat_handlers.py`
- **CombatResultCtx** (16 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatLifecycle** (16 connections) — `server/services/npc_combat_lifecycle.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **NPCCombatIntegrationValidationMixin** (15 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (8 connections)
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_lifecycle.py** (7 connections) — `server/services/npc_combat_lifecycle.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack_on_player()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.get_data_provider()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.get_uuid_mapping()** (6 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 293 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (64 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (13 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (11 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (8 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (6 shared connections)
- [NATS Docs Review](NATS_Docs_Review.md) (4 shared connections)
- [WebSocket Coverage Gaps](WebSocket_Coverage_Gaps.md) (4 shared connections)
- [Exploration Command Models](Exploration_Command_Models.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (3 shared connections)
- [Combat Disconnect Bug](Combat_Disconnect_Bug.md) (3 shared connections)
- [Health Check Models](Health_Check_Models.md) (2 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/services/player_combat_service_support.py`
- `server/services/room_data_validator.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`
- `server/tests/unit/services/test_npc_combat_memory.py`
- `server/tests/unit/services/test_npc_combat_rewards.py`
- `server/tests/unit/services/test_npc_combat_uuid_mapping.py`

## Audit Trail

- EXTRACTED: 1008 (93%)
- INFERRED: 77 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*