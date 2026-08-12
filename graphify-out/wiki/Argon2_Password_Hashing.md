# Argon2 Password Hashing

> 426 nodes

## Key Concepts

- **NPCCombatIntegrationService** (90 connections) — `server/services/npc_combat_integration_service.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **npc_combat_integration_service.py** (51 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (44 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **NPCCombatUUIDMapping** (39 connections) — `server/services/npc_combat_uuid_mapping.py`
- **NPCCombatDataProvider** (30 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatMemory** (29 connections) — `server/services/npc_combat_memory.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **npc_combat_integration_validation_mixin.py** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **NPCCombatRewards** (19 connections) — `server/services/npc_combat_rewards.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatHandlers** (18 connections) — `server/services/npc_combat_handlers.py`
- **RoomDataValidator** (18 connections) — `server/services/room_data_validator.py`
- **GameMechanicsService** (17 connections) — `server/game/mechanics.py`
- **npc_combat_handlers.py** (16 connections) — `server/services/npc_combat_handlers.py`
- **CombatResultCtx** (16 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatLifecycle** (16 connections) — `server/services/npc_combat_lifecycle.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **npc_combat_integration_combat_mixin.py** (15 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **NPCCombatIntegrationValidationMixin** (15 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **UUID** (15 connections)
- **_NPCCombatIntegrationDeps** (14 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- *... and 401 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (53 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (46 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (29 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (18 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (13 shared connections)
- [Async Persistence Core](Async_Persistence_Core.md) (12 shared connections)
- [Async Persistence Migration](Async_Persistence_Migration.md) (11 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (10 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (9 shared connections)
- [Test Value Distribution](Test_Value_Distribution.md) (8 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)

## Source Files

- `server/game/magic/spell_targeting.py`
- `server/game/mechanics.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
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
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/services/room_data_validator.py`

## Audit Trail

- EXTRACTED: 1553 (93%)
- INFERRED: 120 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*