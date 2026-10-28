# Execution Steps

> 20 nodes · cohesion 0.16

## Key Concepts

- **test_audit_logger.py** (16 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **_logger()** (13 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_get_recent_entries()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_get_recent_entries_filters_and_bad_lines()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_get_statistics()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_init()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_command()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_container_interaction()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_permission_change()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_player_action()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Path** (2 connections)
- **test_audit_logger_log_alias_expansion_cycle()** (2 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_security_event_severity_branches()** (2 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_write_entry_swallows_io_error()** (2 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Unit tests for audit_logger utilities. Tests the AuditLogger class.** (1 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Test AuditLogger initialization.** (1 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Test AuditLogger.log_command() logs command execution.** (1 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Test AuditLogger.log_permission_change() logs permission change.** (1 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Test AuditLogger.log_player_action() logs player action.** (1 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Test AuditLogger.get_recent_entries() retrieves recent entries.** (1 connections) — `server/tests/unit/utils/test_audit_logger.py`

## Relationships

- [test_player_preferences_service.py](test_player_preferences_service.py.md) (2 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_audit_logger.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*