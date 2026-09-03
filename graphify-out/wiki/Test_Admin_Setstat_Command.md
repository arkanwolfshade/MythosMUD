# Test Admin Setstat Command

> 46 nodes

## Key Concepts

- **_handle_admin_set_stat_command()** (30 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command.py** (18 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **asyncio** (12 connections)
- **asyncio** (7 connections)
- **test_handle_admin_set_stat_command_success_all_stat_types()** (6 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_logging()** (5 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **test_handle_admin_set_stat_command_case_insensitive_stat_names()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **test_handle_admin_set_stat_command_no_app_context()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **test_handle_admin_set_stat_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **test_handle_admin_set_stat_command_no_player_service()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **test_handle_admin_set_stat_command_no_user_manager()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **test_handle_admin_set_stat_command_dp_above_maximum()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_invalid_stat_name()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_invalid_value()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_stat_name()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_target_player()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_missing_value()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_mp_above_maximum()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_non_admin_denied()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_success_str()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_target_player_not_found()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_value_out_of_range()** (4 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **_make_all_stat_types_harness()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **_assert_stat_write_path()** (2 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **patch** (2 connections)
- *... and 21 more nodes in this community*

## Relationships

- [Admin Setstat Support](Admin_Setstat_Support.md) (16 shared connections)
- [Test Admin Commands](Test_Admin_Commands.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command_context.py`

## Audit Trail

- EXTRACTED: 94 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*