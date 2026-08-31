# CombatCommandHandler

> 159 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **combat_handler.py** (47 connections) — `server/commands/combat_handler.py`
- **test_flee_command.py** (29 connections) — `server/tests/unit/commands/test_flee_command.py`
- **CombatValidator** (26 connections) — `server/validators/combat_validator.py`
- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (23 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **_app_from_request()** (11 connections) — `server/commands/combat_loader.py`
- **FleeHandlerDeps** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_request_with_persistence()** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **CombatCommandHandlerExtras** (9 connections) — `server/commands/combat_handler.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **test_flee_no_exits_returns_no_escape()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_fails_returns_failure_and_uses_action()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_succeeds_returns_success()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **._get_random_error_message()** (8 connections) — `server/validators/combat_validator.py`
- **.validate_combat_command()** (7 connections) — `server/validators/combat_validator.py`
- *... and 134 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (20 shared connections)
- [CombatInstance](CombatInstance.md) (10 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (9 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (7 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (6 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [event_types.py](event_types.py.md) (5 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_loader.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/validators/combat_validator.py`

## Audit Trail

- EXTRACTED: 375 (91%)
- INFERRED: 37 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*