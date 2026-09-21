# admin_setstat_command.py

> 37 nodes

## Key Concepts

- **admin_setstat_command.py** (58 connections) — `server/commands/admin_setstat_command.py`
- **_apply_lucidity_via_service()** (12 connections) — `server/commands/admin_setstat_command.py`
- **_apply_stat_change_and_build_result()** (12 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (11 connections) — `server/commands/admin_setstat_command.py`
- **AdminSetStatApplyContext** (10 connections) — `server/commands/admin_setstat_support.py`
- **_apply_corruption_via_service()** (10 connections) — `server/commands/admin_setstat_command.py`
- **_finish_occult_stat_change()** (9 connections) — `server/commands/admin_setstat_command.py`
- **_execute_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_command.py`
- **calculate_stat_warnings()** (8 connections) — `server/commands/admin_setstat_support.py`
- **log_admin_set_stat()** (8 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatLogContext** (7 connections) — `server/commands/admin_setstat_support.py`
- **AdminSetStatNotifyContext** (7 connections) — `server/commands/admin_setstat_support.py`
- **_maybe_attach_dp_posture_message()** (7 connections) — `server/commands/admin_setstat_command.py`
- **build_set_stat_error_response()** (7 connections) — `server/commands/admin_setstat_support.py`
- **target_player_uuid()** (7 connections) — `server/commands/admin_setstat_support.py`
- **_resolve_admin_id()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_get_catatonia_registry_from_app()** (5 connections) — `server/commands/admin_setstat_command.py`
- **_mutate_player_stat()** (5 connections) — `server/commands/admin_setstat_command.py`
- **stat_change_notification_text()** (3 connections) — `server/commands/admin_setstat_support.py`
- **UUID** (2 connections)
- **BaseException** (1 connections)
- **Admin command to set player statistics. This module provides the handler for…** (1 connections) — `server/commands/admin_setstat_command.py`
- **Apply DP or generic stat mutation; return previous posture when DP changes.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Best-effort admin id for occult service metadata.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Shared notify/log/result for occult service paths (no outer save_player /…** (1 connections) — `server/commands/admin_setstat_command.py`
- *... and 12 more nodes in this community*

## Relationships

- [admin_setstat_support.py](admin_setstat_support.py.md) (26 shared connections)
- [LucidityService](LucidityService.md) (6 shared connections)
- [emit_posture_change](emit_posture_change.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_admin_setstat_command_context.py](test_admin_setstat_command_context.py.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [CorruptionTier](CorruptionTier.md) (3 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (3 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`
- `server/commands/admin_setstat_support.py`

## Audit Trail

- EXTRACTED: 132 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*