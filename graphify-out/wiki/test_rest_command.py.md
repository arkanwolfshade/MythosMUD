# test_rest_command.py

> 82 nodes

## Key Concepts

- **test_rest_command.py** (41 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (28 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (25 connections) — `server/commands/rest_command.py`
- **asyncio** (22 connections)
- **handle_rest_command()** (21 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (19 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (12 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (10 connections)
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_stand_after_cancelled_rest()** (6 connections) — `server/commands/rest_command.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **test_cancel_rest_countdown_cancels_task()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_not_resting()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_restores_standing()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_false()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_no_service()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_true()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_false()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 57 more nodes in this community*

## Relationships

- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (9 shared connections)
- [MockPersistence](MockPersistence.md) (6 shared connections)
- [test_go_command.py](test_go_command.py.md) (5 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (3 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 224 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*