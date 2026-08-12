# test_rest_command.py

> 89 nodes

## Key Concepts

- **test_rest_command.py** (39 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (21 connections) — `server/commands/rest_command.py`
- **asyncio** (21 connections)
- **is_player_resting()** (19 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **Any** (11 connections)
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **fixture** (5 connections)
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **mock_persistence()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_cancels_task()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_not_resting()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_false()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_no_service()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_true()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_false()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 64 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (10 shared connections)
- [is_player_in_grace_period](is_player_in_grace_period.md) (9 shared connections)
- [go_command.py](go_command.py.md) (5 shared connections)
- [combat_service.py](combat_service.py.md) (5 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (4 shared connections)
- [rest_countdown_task.py](rest_countdown_task.py.md) (3 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (2 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (2 shared connections)
- [MockPersistence](MockPersistence.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 392 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*