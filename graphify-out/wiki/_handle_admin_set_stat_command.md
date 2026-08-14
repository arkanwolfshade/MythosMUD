# _handle_admin_set_stat_command

> 72 nodes

## Key Concepts

- **_handle_admin_set_stat_command()** (32 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command.py** (21 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **asyncio** (18 connections)
- **_apply_stat_change_and_build_result()** (8 connections) — `server/commands/admin_setstat_command.py`
- **Any** (7 connections)
- **_build_set_stat_error_response()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_calculate_stat_warnings()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_log_admin_set_stat()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_AdminSetStatLogContext** (5 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (5 connections) — `server/commands/admin_setstat_command.py`
- **_parse_set_stat_args()** (5 connections) — `server/commands/admin_setstat_command.py`
- **test_handle_admin_set_stat_command_logging()** (5 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **_AdminSetStatApplyContext** (4 connections) — `server/commands/admin_setstat_command.py`
- **_get_app_or_error()** (4 connections) — `server/commands/admin_setstat_command.py`
- **_resolve_admin_services_and_permissions()** (4 connections) — `server/commands/admin_setstat_command.py`
- **_warning_for_cap_stat()** (4 connections) — `server/commands/admin_setstat_command.py`
- **test_handle_admin_set_stat_command_case_insensitive_stat_names()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_dp_above_maximum()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_invalid_stat_name()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_invalid_value()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_stat_name()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_target_player()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_value()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_mp_above_maximum()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_no_app_context()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- *... and 47 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (16 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 137 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*