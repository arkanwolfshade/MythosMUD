# Test Admin Shutdown Command

> 8 nodes

## Key Concepts

- **calculate_notification_times()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **test_calculate_notification_times_long()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_calculate_notification_times_short()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_calculate_notification_times_sorted()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Calculate notification times for countdown. Notifications occur: - Every 10…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test calculate_notification_times() for short countdown.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test calculate_notification_times() for long countdown.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test calculate_notification_times() returns sorted descending.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [Test Admin Shutdown Command](Test_Admin_Shutdown_Command.md) (4 shared connections)
- [Admin Shutdown Command](Admin_Shutdown_Command.md) (2 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*