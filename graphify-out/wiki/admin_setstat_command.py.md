# admin_setstat_command.py

> 91 nodes

## Key Concepts

- **admin_setstat_command.py** (58 connections) — `server/commands/admin_setstat_command.py`
- **admin_setstat_support.py** (35 connections) — `server/commands/admin_setstat_support.py`
- **SetStatTargetPlayer** (12 connections) — `server/commands/admin_setstat_support.py`
- **_apply_lucidity_via_service()** (12 connections) — `server/commands/admin_setstat_command.py`
- **_apply_stat_change_and_build_result()** (12 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (11 connections) — `server/commands/admin_setstat_command.py`
- **test_admin_setstat_command_context.py** (11 connections) — `server/tests/unit/commands/test_admin_setstat_command_context.py`
- **AdminSetStatApplyContext** (10 connections) — `server/commands/admin_setstat_support.py`
- **_apply_corruption_via_service()** (10 connections) — `server/commands/admin_setstat_command.py`
- **_finish_occult_stat_change()** (9 connections) — `server/commands/admin_setstat_command.py`
- **Protocol** (9 connections)
- **_execute_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_command.py`
- **calculate_stat_warnings()** (8 connections) — `server/commands/admin_setstat_support.py`
- **log_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_support.py`
- **parse_set_stat_args()** (8 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatLogContext** (7 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatNotifyContext** (7 connections) — `server/commands/admin_setstat_support.py`
- **SetStatApp** (7 connections) — `server/commands/admin_setstat_support.py`
- **SetStatRequest** (7 connections) — `server/commands/admin_setstat_support.py`
- **_maybe_attach_dp_posture_message()** (7 connections) — `server/commands/admin_setstat_command.py`
- **build_set_stat_error_response()** (7 connections) — `server/commands/admin_setstat_support.py`
- **get_app_or_error()** (7 connections) — `server/commands/admin_setstat_support.py`
- **resolve_admin_services_and_permissions()** (7 connections) — `server/commands/admin_setstat_support.py`
- **target_player_uuid()** (7 connections) — `server/commands/admin_setstat_support.py`
- **SetStatConnectionManager** (6 connections) — `server/commands/admin_setstat_support.py`
- *... and 66 more nodes in this community*

## Relationships

- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (16 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [LucidityService](LucidityService.md) (6 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (6 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (3 shared connections)
- [CorruptionService](CorruptionService.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/commands/admin_setstat_support.py`
- `server/tests/unit/commands/test_admin_setstat_command_context.py`

## Audit Trail

- EXTRACTED: 223 (94%)
- INFERRED: 15 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*