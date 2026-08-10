# Magic Service Bundle

> 469 nodes

## Key Concepts

- **AsyncPersistenceLayer** (185 connections) — `server/async_persistence.py`
- **NPCCombatIntegrationService** (90 connections) — `server/services/npc_combat_integration_service.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **npc_combat_integration_service.py** (51 connections) — `server/services/npc_combat_integration_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **test_npc_combat_integration_service.py** (44 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **NPCCombatUUIDMapping** (39 connections) — `server/services/npc_combat_uuid_mapping.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **movement_service.py** (34 connections) — `server/game/movement_service.py`
- **NPCCombatDataProvider** (30 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatMemory** (29 connections) — `server/services/npc_combat_memory.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **npc_combat_integration_validation_mixin.py** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatRewards** (19 connections) — `server/services/npc_combat_rewards.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **movement_helpers.py** (16 connections) — `server/game/movement_helpers.py`
- **npc_combat_handlers.py** (16 connections) — `server/services/npc_combat_handlers.py`
- *... and 444 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (59 shared connections)
- [Conftest Migration Plan](Conftest_Migration_Plan.md) (47 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (45 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (31 shared connections)
- [Client Event Store](Client_Event_Store.md) (26 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (26 shared connections)
- [Container Data Models](Container_Data_Models.md) (21 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (19 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (17 shared connections)
- [Pre-commit Hook Analysis](Pre-commit_Hook_Analysis.md) (15 shared connections)
- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (15 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (13 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/game/movement_helpers.py`
- `server/game/movement_service.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`
- `server/services/npc_combat_lifecycle.py`
- `server/services/npc_combat_memory.py`
- `server/services/npc_combat_rewards.py`
- `server/services/npc_combat_uuid_mapping.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`

## Audit Trail

- EXTRACTED: 1909 (89%)
- INFERRED: 227 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*