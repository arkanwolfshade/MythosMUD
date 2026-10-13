# Community 673

> 25 nodes

## Key Concepts

- **AdminActionsLogger** (30 connections) — `server/structured_logging/admin_actions_logger.py`
- **test_admin_actions_logger.py** (21 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **get_admin_actions_logger()** (11 connections) — `server/structured_logging/admin_actions_logger.py`
- **_read_log_entries()** (7 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **Path** (6 connections)
- **admin_logger()** (4 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_get_admin_actions_logger_singleton()** (4 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_teleport_action_success()** (4 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **log_dir()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_admin_logger_init_from_config()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_admin_command()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_admin_command_failure()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_permission_check_denied()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_teleport_action_failure()** (3 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_get_recent_actions_filters()** (2 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_get_recent_actions_read_failure()** (2 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_get_recent_actions_skips_malformed_lines()** (2 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_get_recent_actions_skips_old_entries()** (2 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_get_teleport_statistics()** (2 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_entry_rotates_on_new_day()** (2 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **test_log_entry_write_failure()** (2 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`
- **fixture** (2 connections)
- **Logger for admin actions with structured logging and file persistence. Provides…** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Get the global admin actions logger instance. Returns: AdminActionsLogger…** (1 connections) — `server/structured_logging/admin_actions_logger.py`
- **Unit tests for AdminActionsLogger.** (1 connections) — `server/tests/unit/structured_logging/test_admin_actions_logger.py`

## Relationships

- [Community 651](Community_651.md) (11 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (6 shared connections)
- [Community 438](Community_438.md) (1 shared connections)
- [Community 937](Community_937.md) (1 shared connections)
- [Community 783](Community_783.md) (1 shared connections)

## Source Files

- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/structured_logging/test_admin_actions_logger.py`

## Audit Trail

- EXTRACTED: 60 (83%)
- INFERRED: 12 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*