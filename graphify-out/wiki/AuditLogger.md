# AuditLogger

> 52 nodes

## Key Concepts

- **AuditLogger** (17 connections) — `server/utils/audit_logger.py`
- **test_audit_logger.py** (16 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **_logger()** (13 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **._write_entry()** (10 connections) — `server/utils/audit_logger.py`
- **._entries_from_log_file()** (7 connections) — `server/utils/audit_logger.py`
- **._matching_entry_from_line()** (6 connections) — `server/utils/audit_logger.py`
- **JsonMap** (6 connections)
- **.get_recent_entries()** (5 connections) — `server/utils/audit_logger.py`
- **._get_log_file_path()** (4 connections) — `server/utils/audit_logger.py`
- **.get_statistics()** (4 connections) — `server/utils/audit_logger.py`
- **.__init__()** (4 connections) — `server/utils/audit_logger.py`
- **test_audit_logger_get_recent_entries()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_get_recent_entries_filters_and_bad_lines()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_get_statistics()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_init()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_command()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_container_interaction()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_permission_change()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_player_action()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **.log_alias_expansion()** (3 connections) — `server/utils/audit_logger.py`
- **.log_command()** (3 connections) — `server/utils/audit_logger.py`
- **.log_container_interaction()** (3 connections) — `server/utils/audit_logger.py`
- **.log_permission_change()** (3 connections) — `server/utils/audit_logger.py`
- **.log_player_action()** (3 connections) — `server/utils/audit_logger.py`
- **.log_security_event()** (3 connections) — `server/utils/audit_logger.py`
- *... and 27 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_audit_logger.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 89 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*