# Validate that player is in

> 69 nodes

## Key Concepts

- **test_go_command.py** (31 connections) — `server/tests/unit/commands/test_go_command.py`
- **handle_go_command()** (19 connections) — `server/commands/go_command.py`
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **Any** (12 connections)
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **_validate_exit()** (9 connections) — `server/commands/go_command.py`
- **_cancel_rest_if_moving()** (7 connections) — `server/commands/go_command.py`
- **_resolve_async_persistence_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **_canonical_room_id_for_go()** (4 connections) — `server/commands/go_command.py`
- **_resolved_direction_for_go_command()** (4 connections) — `server/commands/go_command.py`
- **_connection_manager_from_go_app()** (4 connections) — `server/commands/go_command.py`
- **test_validate_player_posture_get_stats_error()** (4 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_room_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_setup_go_command_room_id_mismatch()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_standing()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_sitting()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_lying()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_player_posture_no_get_stats()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_no_exits()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_direction_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_target_room_not_found()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- **test_validate_exit_success()** (3 connections) — `server/tests/unit/commands/test_go_command.py`
- *... and 44 more nodes in this community*

## Relationships

- [real time](real_time.md) (19 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (2 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (1 shared connections)
- [test magic commands](test_magic_commands.md) (1 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)
- [AuthSlice](AuthSlice.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/commands/go_command.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 221 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*