# CombatCommandHandler

> 140 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **test_flee_command.py** (29 connections) — `server/tests/unit/commands/test_flee_command.py`
- **combat_loader.py** (26 connections) — `server/commands/combat_loader.py`
- **test_combat_loader.py** (23 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **get_combat_command_handler()** (22 connections) — `server/commands/combat_loader.py`
- **commands/combat.py** (19 connections) — `server/commands/combat.py`
- **_app_from_request()** (12 connections) — `server/commands/combat_loader.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **FleeHandlerDeps** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_request_with_persistence()** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **CombatCommandHandlerExtras** (9 connections) — `server/commands/combat_handler.py`
- **handle_kick_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_punch_command()** (9 connections) — `server/commands/combat_loader.py`
- **handle_strike_command()** (9 connections) — `server/commands/combat_loader.py`
- **test_flee_no_exits_returns_no_escape()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_fails_returns_failure_and_uses_action()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_succeeds_returns_success()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **handle_attack_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_flee_command()** (8 connections) — `server/commands/combat_loader.py`
- **handle_taunt_command()** (8 connections) — `server/commands/combat_loader.py`
- **_mock_app_with_container()** (8 connections) — `server/tests/unit/commands/test_combat_loader.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **format_combat_status()** (6 connections) — `server/commands/combat_helpers.py`
- **get_combat_target()** (6 connections) — `server/commands/combat_helpers.py`
- *... and 115 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (11 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (6 shared connections)
- [test_combat_handler.py](test_combat_handler.py.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (4 shared connections)
- [test_combat_grace_period.py](test_combat_grace_period.py.md) (4 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (4 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)

## Source Files

- `server/commands/combat.py`
- `server/commands/combat_handler.py`
- `server/commands/combat_helpers.py`
- `server/commands/combat_loader.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_combat_helpers.py`
- `server/tests/unit/commands/test_combat_loader.py`
- `server/tests/unit/commands/test_flee_command.py`

## Audit Trail

- EXTRACTED: 295 (86%)
- INFERRED: 48 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*