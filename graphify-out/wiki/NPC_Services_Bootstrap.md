# NPC Services Bootstrap

> 335 nodes

## Key Concepts

- **PlayerCombatService** (78 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **TargetResolutionService** (53 connections) — `server/services/target_resolution_service.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (42 connections) — `server/schemas/shared/target_resolution.py`
- **test_target_resolution_service.py** (40 connections) — `server/tests/unit/services/test_target_resolution_service.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (22 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat.py** (19 connections) — `server/commands/combat.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **TargetMetadata** (16 connections) — `server/schemas/shared/target_metadata.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **_app_from_request()** (11 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (11 connections) — `server/commands/combat_loader.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- *... and 310 more nodes in this community*

## Relationships

- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (47 shared connections)
- [startup npc services](startup_npc_services.md) (27 shared connections)
- [Error Conversion](Error_Conversion.md) (25 shared connections)
- [countdown rest task](countdown_rest_task.md) (16 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (15 shared connections)
- [mythosApp appLazyScreens mythosAppViewMo](mythosApp_appLazyScreens_mythosAppViewMo.md) (12 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (10 shared connections)
- [player event realtime](player_event_realtime.md) (10 shared connections)
- [container helpers loot](container_helpers_loot.md) (9 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (9 shared connections)
- [services ascii map](services_ascii_map.md) (9 shared connections)
- [combat flee commands](combat_flee_commands.md) (8 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_loader.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/services/test_player_combat_service.py`
- `server/tests/unit/services/test_target_resolution_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 1238 (90%)
- INFERRED: 140 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*