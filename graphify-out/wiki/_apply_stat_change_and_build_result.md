# _apply_stat_change_and_build_result

> 11 nodes

## Key Concepts

- **_apply_stat_change_and_build_result()** (8 connections) — `server/commands/admin_setstat_command.py`
- **_build_set_stat_error_response()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_log_admin_set_stat()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_AdminSetStatLogContext** (5 connections) — `server/commands/admin_setstat_command.py`
- **_AdminSetStatApplyContext** (4 connections) — `server/commands/admin_setstat_command.py`
- **BaseException** (1 connections)
- **Log admin set stat command.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Context for logging an admin set-stat command (reduces parameter count).** (1 connections) — `server/commands/admin_setstat_command.py`
- **Log error and admin action failure, return error result dict.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Apply stat change, persist, notify, log; return success result dict.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Context for applying an admin set-stat change (reduces parameter count).** (1 connections) — `server/commands/admin_setstat_command.py`

## Relationships

- [build_event](build_event.md) (6 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (3 shared connections)
- [Any](Any.md) (1 shared connections)
- [AdminActionsLogger](AdminActionsLogger.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*