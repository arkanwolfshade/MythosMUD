# NPC Combat

> 576 nodes

## Key Concepts

- **NPCCombatIntegrationService** (89 connections) — `server/services/npc_combat_integration_service.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **test_npc_combat_integration_service.py** (44 connections) — `server/tests/unit/services/test_npc_combat_integration_service.py`
- **NPCCombatUUIDMapping** (39 connections) — `server/services/npc_combat_uuid_mapping.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **NPCCombatLucidity** (30 connections) — `server/services/npc_combat_lucidity.py`
- **NPCCombatDataProvider** (29 connections) — `server/services/npc_combat_data_provider.py`
- **NPCCombatMemory** (28 connections) — `server/services/npc_combat_memory.py`
- **CombatEventPublisher** (27 connections) — `server/services/combat_event_publisher.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **test_npc_combat_integration_service_player_attacks.py** (22 connections) — `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`
- **TestNPCCombatUUIDMapping** (22 connections) — `server/tests/unit/services/test_npc_combat_uuid_mapping.py`
- **npc_combat_integration_validation_mixin.py** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **_NPCCombatIntegrationValidationDeps** (19 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **test_npc_combat_integration_service_npc_aggro.py** (19 connections) — `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- **NPCCombatRewards** (18 connections) — `server/services/npc_combat_rewards.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **GameMechanicsService** (17 connections) — `server/game/mechanics.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **NPCCombatHandlers** (16 connections) — `server/services/npc_combat_handlers.py`
- **TestNPCCombatMemory** (16 connections) — `server/tests/unit/services/test_npc_combat_memory.py`
- **npc_combat_handlers.py** (15 connections) — `server/services/npc_combat_handlers.py`
- **NPCCombatIntegrationValidationMixin** (15 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- *... and 551 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (59 shared connections)
- [Item Instances](Item_Instances.md) (59 shared connections)
- [combat commands handler](combat_commands_handler.md) (17 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (14 shared connections)
- [command factories exploration](command_factories_exploration.md) (11 shared connections)
- [Room Broadcast](Room_Broadcast.md) (9 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (9 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (8 shared connections)
- [lucidity active service](lucidity_active_service.md) (7 shared connections)
- [npc combat services](npc_combat_services.md) (6 shared connections)
- [combat flee commands](combat_flee_commands.md) (5 shared connections)
- [combat helpers commands](combat_helpers_commands.md) (5 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/game/mechanics.py`
- `server/services/combat_event_publisher.py`
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
- `server/tests/unit/services/test_npc_combat_data_provider.py`
- `server/tests/unit/services/test_npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_integration_service_npc_aggro.py`
- `server/tests/unit/services/test_npc_combat_integration_service_player_attacks.py`

## Audit Trail

- EXTRACTED: 1855 (93%)
- INFERRED: 147 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*