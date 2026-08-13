# test_rest_command.py

> 102 nodes

## Key Concepts

- **test_rest_command.py** (40 connections) — `server/tests/unit/commands/test_rest_command.py`
- **go_command.py** (28 connections) — `server/commands/go_command.py`
- **rest_command.py** (27 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (25 connections) — `server/commands/rest_command.py`
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **asyncio** (22 connections)
- **is_player_resting()** (19 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (12 connections)
- **rest_countdown_task.py** (12 connections) — `server/commands/rest_countdown_task.py`
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (10 connections)
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_rest_interrupt_payload_if_moving()** (7 connections) — `server/commands/go_command.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **._interrupt_rest_for_cast()** (6 connections) — `server/commands/magic_commands.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_stand_after_cancelled_rest()** (6 connections) — `server/commands/rest_command.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **UUID** (6 connections)
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- *... and 77 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (17 shared connections)
- [AliasStorage](AliasStorage.md) (16 shared connections)
- [test_go_command.py](test_go_command.py.md) (11 shared connections)
- [is_player_in_grace_period](is_player_in_grace_period.md) (9 shared connections)
- [MockPersistence](MockPersistence.md) (6 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (3 shared connections)
- [.check_and_interrupt_rest](check_and_interrupt_rest.md) (2 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/commands/magic_commands.py`
- `server/commands/rest_command.py`
- `server/commands/rest_countdown_task.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 284 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*