# admin_setstat_command.py

> 15 nodes

## Key Concepts

- **admin_setstat_command.py** (28 connections) — `server/commands/admin_setstat_command.py`
- **_apply_stat_change_and_build_result()** (8 connections) — `server/commands/admin_setstat_command.py`
- **_build_set_stat_error_response()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_log_admin_set_stat()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_AdminSetStatLogContext** (5 connections) — `server/commands/admin_setstat_command.py`
- **_notify_player_stat_change()** (5 connections) — `server/commands/admin_setstat_command.py`
- **_AdminSetStatApplyContext** (4 connections) — `server/commands/admin_setstat_command.py`
- **BaseException** (1 connections)
- **Admin command to set player statistics. This module provides the handler for…** (1 connections) — `server/commands/admin_setstat_command.py`
- **Notify target player of stat change and send player update event.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Log admin set stat command.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Context for logging an admin set-stat command (reduces parameter count).** (1 connections) — `server/commands/admin_setstat_command.py`
- **Log error and admin action failure, return error result dict.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Apply stat change, persist, notify, log; return success result dict.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Context for applying an admin set-stat change (reduces parameter count).** (1 connections) — `server/commands/admin_setstat_command.py`

## Relationships

- [Any](Any.md) (7 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [admin_teleport_commands.py](admin_teleport_commands.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [_parse_set_stat_args](_parse_set_stat_args.md) (2 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*