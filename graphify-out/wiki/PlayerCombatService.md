# PlayerCombatService

> 273 nodes

## Key Concepts

- **PlayerCombatService** (77 connections) — `server/services/player_combat_service.py`
- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **test_player_combat_service.py** (36 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service.py** (32 connections) — `server/services/player_combat_service.py`
- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **get_combat_command_handler()** (23 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (22 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **asyncio** (22 connections)
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **_app_from_request()** (11 connections) — `server/commands/combat_loader.py`
- **CombatCommandHandlerExtras** (9 connections) — `server/commands/combat_handler.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **NPCCombatIntegrationReadApi** (7 connections) — `server/services/player_combat_service_support.py`
- *... and 248 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (20 shared connections)
- [AliasStorage](AliasStorage.md) (12 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (10 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (8 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (6 shared connections)
- [PlayerService](PlayerService.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (6 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (6 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/realtime/connection_manager.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_loader.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/services/test_player_combat_service.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 555 (87%)
- INFERRED: 82 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*