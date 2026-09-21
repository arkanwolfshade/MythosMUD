# _handle_admin_set_stat_command

> 37 nodes

## Key Concepts

- **_handle_admin_set_stat_command()** (32 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command.py** (20 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **asyncio** (14 connections)
- **test_handle_admin_set_stat_command_success_all_stat_types()** (7 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **_make_all_stat_types_harness()** (6 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_lucidity_routes_through_service()** (6 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_corruption_routes_through_service()** (5 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
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
- **_async_session_gen()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **_assert_stat_write_path()** (2 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Handle admin set <stat_name> <target_player> <value>.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Unit tests for admin set stat command handler. Tests the admin set command…** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test successful setting of STR stat.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **Test successful setting of various stat types.** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **#816: Corruption uses CorruptionService with permanence-floor bypass, not…** (1 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- *... and 12 more nodes in this community*

## Relationships

- [test_admin_setstat_command_context.py](test_admin_setstat_command_context.py.md) (7 shared connections)
- [admin_setstat_support.py](admin_setstat_support.py.md) (4 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (3 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [test_support_helpers.py](test_support_helpers.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 85 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*