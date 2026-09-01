# test_rest_command.py

> 102 nodes

## Key Concepts

- **test_rest_command.py** (41 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (29 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (25 connections) — `server/commands/rest_command.py`
- **asyncio** (22 connections)
- **handle_rest_command()** (21 connections) — `server/commands/rest_command.py`
- **MockPersistence** (19 connections) — `server/tests/unit/commands/test_rest_command.py`
- **is_player_resting()** (19 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (12 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (10 connections)
- **_begin_seated_rest_countdown()** (9 connections) — `server/commands/rest_command.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_stand_after_cancelled_rest()** (7 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **test_check_rest_location_false()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_no_room()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_true()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_disconnect_player_intentionally()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_already_resting()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_in_combat()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_connection_manager()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 77 more nodes in this community*

## Relationships

- [disconnect_grace_period.py](disconnect_grace_period.py.md) (9 shared connections)
- [test_go_command.py](test_go_command.py.md) (5 shared connections)
- [command_service.py](command_service.py.md) (5 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [FollowService](FollowService.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (3 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 258 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*