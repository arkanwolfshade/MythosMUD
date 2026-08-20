# _handle_admin_set_stat_command

> 10 nodes

## Key Concepts

- **_handle_admin_set_stat_command()** (32 connections) — `server/commands/admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_stat_name()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_no_app_context()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_non_admin_denied()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **_validate_set_stat_inputs()** (3 connections) — `server/commands/admin_setstat_command.py`
- **Validate stat name and value inputs.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Handle the admin set command to set a player's statistic. Usage: admin set…** (1 connections) — `server/commands/admin_setstat_command.py`
- **Test non-admin user is denied.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test missing stat name handling.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test handling when app context is not available.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`

## Relationships

- [test_admin_setstat_command.py](test_admin_setstat_command.py.md) (19 shared connections)
- [Any](Any.md) (3 shared connections)
- [_apply_stat_change_and_build_result](_apply_stat_change_and_build_result.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [command_service.py](command_service.py.md) (1 shared connections)
- [_parse_set_stat_args](_parse_set_stat_args.md) (1 shared connections)
- [test_handle_admin_set_stat_command_invalid_stat_name](test_handle_admin_set_stat_command_invalid_stat_name.md) (1 shared connections)
- [test_handle_admin_set_stat_command_success_all_stat_types](test_handle_admin_set_stat_command_success_all_stat_types.md) (1 shared connections)
- [test_handle_admin_set_stat_command_success_str](test_handle_admin_set_stat_command_success_str.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*