# PlayerCombatService

> 438 nodes

## Key Concepts

- **PlayerCombatService** (77 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (37 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **test_target_resolution_service.py** (27 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **asyncio** (22 connections)
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **asyncio** (20 connections)
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (16 connections) — `server/commands/combat_handler.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **asyncio** (12 connections)
- **TargetMetadata** (11 connections) — `server/schemas/shared/target_metadata.py`
- *... and 413 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (38 shared connections)
- [EventBus](EventBus.md) (29 shared connections)
- [AliasStorage](AliasStorage.md) (20 shared connections)
- [PlayerService](PlayerService.md) (20 shared connections)
- [CombatService](CombatService.md) (16 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (12 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (12 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (12 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (11 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (10 shared connections)
- [get_username_from_user](get_username_from_user.md) (9 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/services/test_player_combat_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 925 (89%)
- INFERRED: 114 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*