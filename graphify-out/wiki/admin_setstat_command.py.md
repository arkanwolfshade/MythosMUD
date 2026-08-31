# admin_setstat_command.py

> 66 nodes

## Key Concepts

- **admin_setstat_command.py** (38 connections) — `server/commands/admin_setstat_command.py`
- **admin_setstat_support.py** (35 connections) — `server/commands/admin_setstat_support.py`
- **SetStatTargetPlayer** (11 connections) — `server/commands/admin_setstat_support.py`
- **_apply_stat_change_and_build_result()** (10 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (10 connections) — `server/commands/admin_setstat_command.py`
- **Protocol** (9 connections)
- **_execute_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_command.py`
- **parse_set_stat_args()** (8 connections) — `server/commands/admin_setstat_support.py`
- **_maybe_attach_dp_posture_message()** (7 connections) — `server/commands/admin_setstat_command.py`
- **build_set_stat_error_response()** (7 connections) — `server/commands/admin_setstat_support.py`
- **log_admin_set_stat()** (7 connections) — `server/commands/admin_setstat_support.py`
- **resolve_admin_services_and_permissions()** (7 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatApplyContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatLogContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatNotifyContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **SetStatApp** (6 connections) — `server/commands/admin_setstat_support.py`
- **calculate_stat_warnings()** (6 connections) — `server/commands/admin_setstat_support.py`
- **test_notify_player_stat_change_dp_attaches_posture_message()** (6 connections) — `server/tests/unit/commands/test_admin_setstat_command.py`
- **SetStatConnectionManager** (5 connections) — `server/commands/admin_setstat_support.py`
- **SetStatPersistence** (5 connections) — `server/commands/admin_setstat_support.py`
- **_mutate_player_stat()** (5 connections) — `server/commands/admin_setstat_command.py`
- **target_player_uuid()** (5 connections) — `server/commands/admin_setstat_support.py`
- **validate_set_stat_inputs()** (4 connections) — `server/commands/admin_setstat_support.py`
- **_warning_for_cap_stat()** (4 connections) — `server/commands/admin_setstat_support.py`
- **UUID** (4 connections)
- *... and 41 more nodes in this community*

## Relationships

- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (15 shared connections)
- [emit_posture_change](emit_posture_change.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/commands/admin_setstat_support.py`
- `server/tests/unit/commands/test_admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 156 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*