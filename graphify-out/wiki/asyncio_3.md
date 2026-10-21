# asyncio

> 81 nodes · cohesion 0.04

## Key Concepts

- **test_rest_command.py** (45 connections) — `server/tests/unit/commands/test_rest_command.py`
- **asyncio** (26 connections)
- **handle_rest_command()** (23 connections) — `server/commands/rest_command.py`
- **MockPersistence** (21 connections) — `server/tests/unit/commands/test_rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **fixture** (5 connections)
- **test_check_rest_location_false()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_no_room()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_true()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_disconnect_player_intentionally()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_already_resting()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_in_combat()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_connection_manager()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_player_not_found()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_rejected_while_channeling_ground()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_rest_location_instant()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_rest_location_marks_intentional_before_delay()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_starts_countdown()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_start_rest_countdown_creates_task()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_start_rest_countdown_timer_expires()** (5 connections) — `server/tests/unit/commands/test_rest_command.py`
- **mock_persistence()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_cancels_task()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_not_resting()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_restores_standing()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_false()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 56 more nodes in this community*

## Relationships

- [test_follow_commands.py](test_follow_commands.py.md) (28 shared connections)
- [test_look_npc_helpers.py](test_look_npc_helpers.py.md) (5 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)

## Source Files

- `server/commands/rest_command.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 174 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*