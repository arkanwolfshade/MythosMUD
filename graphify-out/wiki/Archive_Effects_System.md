# Archive Effects System

> 11 nodes

## Key Concepts

- **_apply_stat_change_and_build_result()** (8 connections) — `server/commands/admin_setstat_command.py`
- **_log_admin_set_stat()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_build_set_stat_error_response()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_AdminSetStatLogContext** (5 connections) — `server/commands/admin_setstat_command.py`
- **_AdminSetStatApplyContext** (4 connections) — `server/commands/admin_setstat_command.py`
- **BaseException** (1 connections)
- **Context for logging an admin set-stat command (reduces parameter count).** (1 connections) — `server/commands/admin_setstat_command.py`
- **Context for applying an admin set-stat change (reduces parameter count).** (1 connections) — `server/commands/admin_setstat_command.py`
- **Log admin set stat command.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Log error and admin action failure, return error result dict.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Apply stat change, persist, notify, log; return success result dict.** (1 connections) — `server/commands/admin_setstat_command.py`

## Relationships

- [Combat Messaging Tests](Combat_Messaging_Tests.md) (7 shared connections)
- [Admin Status Commands](Admin_Status_Commands.md) (3 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*