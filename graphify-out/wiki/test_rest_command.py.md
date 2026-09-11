# test_rest_command.py

> 108 nodes

## Key Concepts

- **test_rest_command.py** (41 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (31 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (25 connections) — `server/commands/rest_command.py`
- **asyncio** (23 connections)
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **MockPersistence** (20 connections) — `server/tests/unit/commands/test_rest_command.py`
- **is_player_resting()** (19 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (13 connections) — `server/commands/rest_command.py`
- **Any** (13 connections)
- **check_player_in_combat()** (11 connections) — `server/commands/rest_command.py`
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (11 connections)
- **_begin_seated_rest_countdown()** (10 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_stand_after_cancelled_rest()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (7 connections) — `server/commands/rest_command.py`
- **._interrupt_rest_for_cast()** (6 connections) — `server/commands/magic_commands.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_delayed_disconnect_player_intentionally()** (5 connections) — `server/commands/rest_command.py`
- **test_check_rest_location_false()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_no_room()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_true()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_disconnect_player_intentionally()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_already_resting()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 83 more nodes in this community*

## Relationships

- [disconnect_grace_period.py](disconnect_grace_period.py.md) (9 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (6 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (6 shared connections)
- [test_go_command.py](test_go_command.py.md) (5 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (4 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [emit_posture_change](emit_posture_change.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (4 shared connections)
- [combat_service.py](combat_service.py.md) (4 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/magic_commands.py`
- `server/commands/rest_command.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 275 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*