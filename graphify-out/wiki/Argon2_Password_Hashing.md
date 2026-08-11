# Argon2 Password Hashing

> 140 nodes

## Key Concepts

- **NPCCombatIntegrationService** (90 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_integration_service.py** (51 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatDataProvider** (30 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatMemory** (29 connections) — `server/services/npc_combat_memory.py`
- **npc_combat_integration_validation_mixin.py** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatRewards** (19 connections) — `server/services/npc_combat_rewards.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_handlers.py** (16 connections) — `server/services/npc_combat_handlers.py`
- **CombatResultCtx** (16 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatLifecycle** (16 connections) — `server/services/npc_combat_lifecycle.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **npc_combat_integration_combat_mixin.py** (15 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCCombatIntegrationValidationMixin** (15 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.__init__()** (12 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatIntegrationCombatMixin** (11 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **npc_combat_rewards.py** (10 connections) — `server/services/npc_combat_rewards.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_uuid_mapping.py** (8 connections) — `server/services/npc_combat_uuid_mapping.py`
- **.__init__()** (7 connections) — `server/services/npc_combat_handlers.py`
- **._handle_npc_death_on_combat_end()** (7 connections) — `server/services/npc_combat_handlers.py`
- **npc_combat_lifecycle.py** (7 connections) — `server/services/npc_combat_lifecycle.py`
- **npc_combat_memory.py** (7 connections) — `server/services/npc_combat_memory.py`
- **._init_messaging_handlers_and_publisher()** (6 connections) — `server/services/npc_combat_integration_service.py`
- **.handle_npc_attack_on_player()** (6 connections) — `server/services/npc_combat_integration_service.py`
- *... and 115 more nodes in this community*

## Relationships

- [MP Regeneration Service](MP_Regeneration_Service.md) (37 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (19 shared connections)
- [Health Check Models](Health_Check_Models.md) (17 shared connections)
- [Command Testing Guide](Command_Testing_Guide.md) (12 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (11 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (10 shared connections)
- [Combat Command Models](Combat_Command_Models.md) (9 shared connections)
- [E2E Suite Spec Helpers](E2E_Suite_Spec_Helpers.md) (8 shared connections)
- [Test Value Distribution](Test_Value_Distribution.md) (8 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (7 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (6 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (6 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`
- `server/tests/unit/services/test_npc_combat_memory.py`
- `server/tests/unit/services/test_npc_combat_rewards.py`

## Audit Trail

- EXTRACTED: 610 (90%)
- INFERRED: 65 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*