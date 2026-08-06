# command models admin

> 72 nodes

## Key Concepts

- **_handle_admin_set_stat_command()** (33 connections) — `server/commands/admin_setstat_command.py`
- **admin_setstat_command.py** (28 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command.py** (21 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **_apply_stat_change_and_build_result()** (8 connections) — `server/commands/admin_setstat_command.py`
- **Any** (7 connections)
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
- **_parse_value_from_args()** (3 connections) — `server/commands/admin_setstat_command.py`
- **_validate_set_stat_inputs()** (3 connections) — `server/commands/admin_setstat_command.py`
- **_warning_for_stat_range()** (3 connections) — `server/commands/admin_setstat_command.py`
- **test_handle_admin_set_stat_command_success_str()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_success_all_stat_types()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_invalid_stat_name()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_invalid_value()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_value_out_of_range()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_dp_above_maximum()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **test_handle_admin_set_stat_command_mp_above_maximum()** (3 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- *... and 47 more nodes in this community*

## Relationships

- [commands admin mute](commands_admin_mute.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [admin structured logging](admin_structured_logging.md) (3 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 244 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*