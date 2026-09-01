# admin_setstat_command.py

> 99 nodes

## Key Concepts

- **admin_setstat_command.py** (39 connections) — `server/commands/admin_setstat_command.py`
- **admin_setstat_support.py** (35 connections) — `server/commands/admin_setstat_support.py`
- **_handle_admin_set_stat_command()** (30 connections) — `server/commands/admin_setstat_command.py`
- **SetStatTargetPlayer** (12 connections) — `server/commands/admin_setstat_support.py`
- **normalize_posture()** (12 connections) — `server/realtime/posture_notify.py`
- **test_admin_setstat_command_context.py** (12 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **_apply_stat_change_and_build_result()** (10 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (10 connections) — `server/commands/admin_setstat_command.py`
- **Protocol** (9 connections)
- **_execute_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_command.py`
- **parse_set_stat_args()** (8 connections) — `server/commands/admin_setstat_support.py`
- **SetStatApp** (7 connections) — `server/commands/admin_setstat_support.py`
- **SetStatRequest** (7 connections) — `server/commands/admin_setstat_support.py`
- **_maybe_attach_dp_posture_message()** (7 connections) — `server/commands/admin_setstat_command.py`
- **build_set_stat_error_response()** (7 connections) — `server/commands/admin_setstat_support.py`
- **get_app_or_error()** (7 connections) — `server/commands/admin_setstat_support.py`
- **log_admin_set_stat()** (7 connections) — `server/commands/admin_setstat_support.py`
- **resolve_admin_services_and_permissions()** (7 connections) — `server/commands/admin_setstat_support.py`
- **asyncio** (7 connections)
- **AdminSetStatApplyContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatLogContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatNotifyContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **SetStatConnectionManager** (6 connections) — `server/commands/admin_setstat_support.py`
- **SetStatPersistence** (6 connections) — `server/commands/admin_setstat_support.py`
- **calculate_stat_warnings()** (6 connections) — `server/commands/admin_setstat_support.py`
- *... and 74 more nodes in this community*

## Relationships

- [test_admin_setstat_command.py](test_admin_setstat_command.py.md) (14 shared connections)
- [build_event](build_event.md) (14 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (3 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/commands/admin_setstat_support.py`
- `server/realtime/posture_notify.py`
- `server/tests/unit/commands/test_admin_setstat_command_context.py`

## Audit Trail

- EXTRACTED: 224 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*