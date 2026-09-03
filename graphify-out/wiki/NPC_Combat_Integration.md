# NPC Combat Integration

> 323 nodes

## Key Concepts

- **npc_combat_integration_service.py** (53 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatDataProvider** (38 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatUUIDMapping** (38 connections) — `server/services/npc_combat_uuid_mapping.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **test_npc_combat_handlers.py** (23 connections) — `server/tests/unit/services/test_npc_combat_handlers.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **_NPCCombatIntegrationValidationDeps** (18 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **test_npc_combat_data_provider.py** (18 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **npc_combat_handlers.py** (16 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatLifecycle** (15 connections) — `server/services/npc_combat_lifecycle.py`
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.connection_manager()** (13 connections) — `server/services/combat_messaging/base.py`
- **CombatResultCtx** (12 connections) — `server/services/npc_combat_handlers.py`
- **TestNPCCombatLifecycle** (12 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **NPCCombatIntegrationValidationMixin** (11 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **.store_npc_xp_mapping_for_mixin()** (10 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatIntegrationCombatMixin** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._init_npc_submodules()** (9 connections) — `server/services/npc_combat_integration_service.py`
- **asyncio** (9 connections)
- *... and 298 more nodes in this community*

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (29 shared connections)
- [Npc Combat Integration Service](Npc_Combat_Integration_Service.md) (18 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (12 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (11 shared connections)
- [Combat Events](Combat_Events.md) (9 shared connections)
- [Test Npc Combat Lucidity](Test_Npc_Combat_Lucidity.md) (7 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (5 shared connections)
- [Test Npc Combat Rewards](Test_Npc_Combat_Rewards.md) (4 shared connections)
- [Npc Combat Grace](Npc_Combat_Grace.md) (4 shared connections)
- [Test Magic Service](Test_Magic_Service.md) (4 shared connections)
- [Test Room Data Validator](Test_Room_Data_Validator.md) (3 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (3 shared connections)

## Source Files

- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging_integration.py`
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
- `server/tests/unit/services/test_npc_combat_handlers.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`
- `server/tests/unit/services/test_npc_combat_memory.py`
- `server/tests/unit/services/test_npc_combat_uuid_mapping.py`

## Audit Trail

- EXTRACTED: 609 (93%)
- INFERRED: 45 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*