# Validate that player is in

> 44 nodes

## Key Concepts

- **test_go_command.py** (31 connections) — `server/tests/unit/commands/test_go_command.py`
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **test_setup_go_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_room_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_room_id_mismatch()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_standing()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_sitting()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_lying()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_no_get_stats()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_get_stats_error()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_no_exits()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_target_room_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_failure()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_error_handling()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_execute_movement_fallback_service()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_no_direction()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_setup_failure()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_no_exit()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_handle_go_command_rest_interrupt_still_moves()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _setup_go_command returns None when player not found.** (2 connections) — `server/tests/unit/commands/test_go_command.py`
- **Test _validate_player_posture returns False for sitting player.** (2 connections) — `server/tests/unit/commands/test_go_command.py`
- *... and 19 more nodes in this community*

## Relationships

- [go command](go_command.md) (27 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 127 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*