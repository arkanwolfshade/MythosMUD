# Any

> 11 nodes

## Key Concepts

- **Any** (7 connections)
- **_calculate_stat_warnings()** (6 connections) — `server/commands/admin_setstat_command.py`
- **_get_app_or_error()** (4 connections) — `server/commands/admin_setstat_command.py`
- **_resolve_admin_services_and_permissions()** (4 connections) — `server/commands/admin_setstat_command.py`
- **_warning_for_cap_stat()** (4 connections) — `server/commands/admin_setstat_command.py`
- **_warning_for_stat_range()** (3 connections) — `server/commands/admin_setstat_command.py`
- **Return warning message if value exceeds DP or MP calculated maximum; else empty…** (1 connections) — `server/commands/admin_setstat_command.py`
- **Return warning message if value is outside normal range for stat; else empty…** (1 connections) — `server/commands/admin_setstat_command.py`
- **Calculate warnings for stat values that exceed maximums or normal ranges.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Resolve required services and check admin permissions.** (1 connections) — `server/commands/admin_setstat_command.py`
- **Return (app, None) if request has app, else (None, error_dict).** (1 connections) — `server/commands/admin_setstat_command.py`

## Relationships

- [admin_setstat_command.py](admin_setstat_command.py.md) (7 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (3 shared connections)
- [_parse_set_stat_args](_parse_set_stat_args.md) (1 shared connections)

## Source Files

- `server/commands/admin_setstat_command.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*