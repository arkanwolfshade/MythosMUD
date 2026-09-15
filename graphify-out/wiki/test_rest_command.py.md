# test_rest_command.py

> 84 nodes

## Key Concepts

- **test_rest_command.py** (41 connections) — `server/tests/unit/commands/test_rest_command.py`
- **cancel_rest_countdown()** (25 connections) — `server/commands/rest_command.py`
- **asyncio** (23 connections)
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **MockPersistence** (20 connections) — `server/tests/unit/commands/test_rest_command.py`
- **check_player_in_combat()** (11 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **test_check_rest_location_false()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_no_room()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_true()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_disconnect_player_intentionally()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_already_resting()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_in_combat()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_connection_manager()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_rest_location_instant()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_rest_location_marks_intentional_before_delay()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_starts_countdown()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_start_rest_countdown_creates_task()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_start_rest_countdown_timer_expires()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **fixture** (5 connections)
- **mock_persistence()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_cancels_task()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_not_resting()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 59 more nodes in this community*

## Relationships

- [PlayerPositionService](PlayerPositionService.md) (26 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (7 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (2 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (1 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (1 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 194 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*