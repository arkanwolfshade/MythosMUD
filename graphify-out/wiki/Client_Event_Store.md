# Client Event Store

> 859 nodes

## Key Concepts

- **get_logger()** (509 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (483 connections) — `server/structured_logging/enhanced_logging_config.py`
- **AsyncPersistenceLayer** (185 connections) — `server/async_persistence.py`
- **CombatService** (182 connections) — `server/services/combat_service.py`
- **PlayerService** (141 connections) — `server/game/player_service.py`
- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **async_persistence.py** (74 connections) — `server/async_persistence.py`
- **alias_storage.py** (64 connections) — `server/alias_storage.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **npc_combat_integration_service.py** (51 connections) — `server/services/npc_combat_integration_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **player_service.py** (44 connections) — `server/game/player_service.py`
- **player_respawn_service.py** (41 connections) — `server/services/player_respawn_service.py`
- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **nats_message_handler.py** (39 connections) — `server/realtime/nats_message_handler.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **movement_service.py** (34 connections) — `server/game/movement_service.py`
- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **room.py** (31 connections) — `server/models/room.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- *... and 834 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (194 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (147 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (123 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (110 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (92 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (86 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (83 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (64 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (59 shared connections)
- [Conftest Migration Plan](Conftest_Migration_Plan.md) (52 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (49 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (40 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`
- `schemas/validator.py`
- `server/alias_storage.py`
- `server/api/base.py`
- `server/app/game_tick_processing.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/async_persistence.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/npc_admin/behavior.py`
- `server/commands/npc_admin/monitoring.py`

## Audit Trail

- EXTRACTED: 5318 (93%)
- INFERRED: 377 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*