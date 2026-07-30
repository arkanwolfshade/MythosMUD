# admin setstat command

> 86 nodes

## Key Concepts

- **_handle_admin_set_stat_command()** (33 connections) — `server/commands/admin_setstat_command.py`
- **admin_setstat_command.py** (28 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command.py** (21 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **handle_admin_command()** (14 connections) — `server/commands/admin_commands.py`
- **_handle_admin_status_command()** (9 connections) — `server/commands/admin_commands.py`
- **_apply_stat_change_and_build_result()** (8 connections) — `server/commands/admin_setstat_command.py`
- **Any** (7 connections)
- **_handle_admin_time_command()** (6 connections) — `server/commands/admin_commands.py`
- **_calculate_stat_warnings()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_log_admin_set_stat()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_build_set_stat_error_response()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_AdminSetStatLogContext** (5 connections) — `server/commands/admin_setstat_command.py`
- **_parse_set_stat_args()** (5 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (5 connections) — `server/commands/admin_setstat_command.py`
- **_resolve_admin_services_and_permissions()** (5 connections) — `server/commands/admin_setstat_command.py`
- **_AdminSetStatApplyContext** (4 connections) — `server/commands/admin_setstat_command.py`
- **_warning_for_cap_stat()** (4 connections) — `server/commands/admin_setstat_command.py`
- **_get_app_or_error()** (4 connections) — `server/commands/admin_setstat_command.py`
- **.is_admin()** (4 connections) — `server/commands/communication_commands_support.py`
- **Any** (3 connections)
- **_parse_value_from_args()** (3 connections) — `server/commands/admin_setstat_command.py`
- **_validate_set_stat_inputs()** (3 connections) — `server/commands/admin_setstat_command.py`
- **_warning_for_stat_range()** (3 connections) — `server/commands/admin_setstat_command.py`
- **test_handle_admin_command_status()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_admin_command_time()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- *... and 61 more nodes in this community*

## Relationships

- [test command factories inventory](test_command_factories_inventory.md) (13 shared connections)
- [Any](Any.md) (8 shared connections)
- [real time](real_time.md) (4 shared connections)
- [circuit breaker](circuit_breaker.md) (3 shared connections)
- [Player Position Service](Player_Position_Service.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [admin setlucidity command](admin_setlucidity_command.md) (1 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/commands/admin_setstat_command.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_admin_commands.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 288 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*