# NPC Combat Lifecycle

> 312 nodes · cohesion 0.01

## Key Concepts

- **NPCCombatDataProvider** (62 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatUUIDMapping** (52 connections) — `server/services/npc_combat_uuid_mapping.py`
- **npc_combat_integration_service.py** (43 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatLucidity** (43 connections) — `server/services/npc_combat_lucidity.py`
- **NPCCombatMemory** (43 connections) — `server/services/npc_combat_memory.py`
- **NPCCombatRewards** (31 connections) — `server/services/npc_combat_rewards.py`
- **NPCCombatLifecycle** (30 connections) — `server/services/npc_combat_lifecycle.py`
- **NPCCombatHandlers** (27 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatIntegrationValidationMixin** (26 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **RoomDataValidator** (25 connections) — `server/services/room_data_validator.py`
- **NPCCombatIntegrationCombatMixin** (22 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **npc_combat_integration_validation_mixin.py** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **npc_combat_data_provider.py** (16 connections) — `server/services/npc_combat_data_provider.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **AsyncPersistenceLayer** (15 connections) — `server/services/npc_combat_integration_service.py`
- **CombatService** (15 connections) — `server/services/npc_combat_integration_service.py`
- **UUID** (15 connections) — `server/services/npc_combat_integration_service.py`
- **npc_combat_integration_combat_mixin.py** (15 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **CombatMessagingIntegration** (14 connections) — `server/services/npc_combat_integration_service.py`
- **ConnectionManager** (14 connections) — `server/services/npc_combat_integration_service.py`
- **EventBus** (14 connections) — `server/services/npc_combat_integration_service.py`
- **NPCCombatDataProvider** (14 connections) — `server/services/npc_combat_integration_service.py`
- *... and 287 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (72 shared connections)
- [[NPC Admin API]] (31 shared connections)
- [[Combat Command Handler]] (25 shared connections)
- [[Combat Attack Service]] (15 shared connections)
- [[Active Lucidity Service]] (7 shared connections)
- [[Combat Taunt Tests]] (6 shared connections)
- [[NPC Occupant Verification]] (4 shared connections)
- [[Look Command Helpers]] (4 shared connections)
- [[Services Npc Combat]] (4 shared connections)
- [[NPC Combat Rewards Tests]] (4 shared connections)
- [[Room Data Fixer]] (4 shared connections)
- [[Room Occupant Events]] (3 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_lucidity.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/services/room_data_validator.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_memory.py`
- `server/tests/unit/services/test_npc_combat_uuid_mapping.py`

## Audit Trail

- EXTRACTED: 1028 (72%)
- INFERRED: 392 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
