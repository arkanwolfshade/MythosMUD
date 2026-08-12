# CombatCommandHandler

> 178 nodes

## Key Concepts

- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (37 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **CombatValidator** (28 connections) — `server/validators/combat_validator.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **combat_loader.py** (25 connections) — `server/commands/combat_loader.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **get_combat_command_handler()** (19 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (16 connections) — `server/commands/combat_handler.py`
- **asyncio** (12 connections)
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_app_from_request()** (8 connections) — `server/commands/combat_loader.py`
- **_as_app_with_state()** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **handle_kick_command()** (7 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (7 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (7 connections) — `server/commands/combat_loader.py`
- **test_get_player_and_room_no_current_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- *... and 153 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (26 shared connections)
- [get_logger](get_logger.md) (25 shared connections)
- [AliasStorage](AliasStorage.md) (18 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (14 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (12 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (10 shared connections)
- [CombatService](CombatService.md) (9 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (6 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 693 (87%)
- INFERRED: 103 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*