# _handle_admin_set_stat_command

> 10 nodes

## Key Concepts

- **_handle_admin_set_stat_command()** (32 connections) — `server/commands/admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_target_player()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_no_player_service()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **_validate_set_stat_inputs()** (3 connections) — `server/commands/admin_setstat_command.py`
- **Validate stat name and value inputs.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Handle the admin set command to set a player's statistic. Usage: admin set…** (1 connections) — `server/commands/admin_setstat_command.py`
- **Test missing target player handling.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test handling when player service is not available.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test handling when persistence layer is not available.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`

## Relationships

- [test_admin_setstat_command.py](test_admin_setstat_command.py.md) (18 shared connections)
- [Any](Any.md) (4 shared connections)
- [_apply_stat_change_and_build_result](_apply_stat_change_and_build_result.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (1 shared connections)
- [test_handle_admin_set_stat_command_dp_above_maximum](test_handle_admin_set_stat_command_dp_above_maximum.md) (1 shared connections)
- [test_handle_admin_set_stat_command_missing_value](test_handle_admin_set_stat_command_missing_value.md) (1 shared connections)
- [test_handle_admin_set_stat_command_no_app_context](test_handle_admin_set_stat_command_no_app_context.md) (1 shared connections)
- [test_handle_admin_set_stat_command_success_all_stat_types](test_handle_admin_set_stat_command_success_all_stat_types.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*