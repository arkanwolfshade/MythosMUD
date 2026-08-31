# admin_setstat_command.py

> 77 nodes

## Key Concepts

- **admin_setstat_command.py** (39 connections) — `server/commands/admin_setstat_command.py`
- **admin_setstat_support.py** (35 connections) — `server/commands/admin_setstat_support.py`
- **SetStatTargetPlayer** (12 connections) — `server/commands/admin_setstat_support.py`
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
- **AdminSetStatApplyContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatLogContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatNotifyContext** (6 connections) — `server/commands/admin_setstat_support.py`
- **SetStatConnectionManager** (6 connections) — `server/commands/admin_setstat_support.py`
- **SetStatPersistence** (6 connections) — `server/commands/admin_setstat_support.py`
- **calculate_stat_warnings()** (6 connections) — `server/commands/admin_setstat_support.py`
- **_mutate_player_stat()** (5 connections) — `server/commands/admin_setstat_command.py`
- **target_player_uuid()** (5 connections) — `server/commands/admin_setstat_support.py`
- **ResolvedAdminPlayer** (4 connections) — `server/commands/admin_setstat_support.py`
- **SetStatPlayerService** (4 connections) — `server/commands/admin_setstat_support.py`
- *... and 52 more nodes in this community*

## Relationships

- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (11 shared connections)
- [player_event_handlers_state.py](player_event_handlers_state.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/commands/admin_setstat_support.py`

## Audit Trail

- EXTRACTED: 166 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*