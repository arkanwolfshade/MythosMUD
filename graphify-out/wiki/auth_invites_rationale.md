# auth invites rationale

> 6 nodes

## Key Concepts

- **broadcast_shutdown_notification()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_success()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_broadcast_shutdown_notification_failure()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Broadcast shutdown notification to all players.      Args:         connection_ma** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test broadcast_shutdown_notification() successfully broadcasts.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test broadcast_shutdown_notification() handles errors.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [shutdown admin command](shutdown_admin_command.md) (6 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*