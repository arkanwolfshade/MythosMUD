# PlayerCombatService

> 162 nodes

## Key Concepts

- **PlayerCombatService** (73 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (57 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (54 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (30 connections) — `server/commands/combat_loader.py`
- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **get_combat_command_handler()** (26 connections) — `server/commands/combat_loader.py`
- **player_combat_service.py** (26 connections) — `server/services/player_combat_service.py`
- **commands/combat.py** (23 connections) — `server/commands/combat.py`
- **test_combat_loader.py** (22 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **player_combat_service_support.py** (17 connections) — `server/services/player_combat_service_support.py`
- **.event_bus()** (14 connections) — `server/realtime/connection_manager.py`
- **_app_from_request()** (13 connections) — `server/commands/combat_loader.py`
- **.__init__()** (12 connections) — `server/commands/combat_handler.py`
- **CombatCommandHandlerExtras** (10 connections) — `server/commands/combat_handler.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_assist_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_protect_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **._init_quest_service()** (7 connections) — `server/container/bundles/game.py`
- *... and 137 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (21 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (21 shared connections)
- [AliasStorage](AliasStorage.md) (19 shared connections)
- [CombatService](CombatService.md) (15 shared connections)
- [command_parser.py](command_parser.py.md) (12 shared connections)
- [UUID](UUID.md) (11 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (10 shared connections)
- [EventBus](EventBus.md) (9 shared connections)
- [TargetType](TargetType.md) (8 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (7 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (7 shared connections)
- [PlayerCombatState](PlayerCombatState.md) (7 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/container/bundles/game.py`
- `server/realtime/connection_manager.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/commands/test_assist_wiring.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_loader.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/services/test_player_combat_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 428 (82%)
- INFERRED: 93 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*