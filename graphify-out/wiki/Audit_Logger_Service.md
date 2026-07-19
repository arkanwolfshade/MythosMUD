# Audit Logger Service

> 38 nodes · cohesion 0.08

## Key Concepts

- **AuditLogger** (19 connections) — `server/utils/audit_logger.py`
- **._write_entry()** (10 connections) — `server/utils/audit_logger.py`
- **test_audit_logger.py** (7 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Any** (6 connections) — `server/utils/audit_logger.py`
- **._get_log_file_path()** (4 connections) — `server/utils/audit_logger.py`
- **.get_recent_entries()** (4 connections) — `server/utils/audit_logger.py`
- **.get_statistics()** (4 connections) — `server/utils/audit_logger.py`
- **.__init__()** (4 connections) — `server/utils/audit_logger.py`
- **.log_command()** (4 connections) — `server/utils/audit_logger.py`
- **.log_container_interaction()** (4 connections) — `server/utils/audit_logger.py`
- **.log_security_event()** (4 connections) — `server/utils/audit_logger.py`
- **.log_alias_expansion()** (3 connections) — `server/utils/audit_logger.py`
- **.log_permission_change()** (3 connections) — `server/utils/audit_logger.py`
- **.log_player_action()** (3 connections) — `server/utils/audit_logger.py`
- **test_audit_logger_get_recent_entries()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_init()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_command()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_permission_change()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_player_action()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **Path** (2 connections) — `server/utils/audit_logger.py`
- **Log permission/role changes.          Args:             admin_name: Admin who ma** (1 connections) — `server/utils/audit_logger.py`
- **Log container interaction events for security and compliance.          Args:** (1 connections) — `server/utils/audit_logger.py`
- **Audit logging for security-sensitive command execution.      Creates structured** (1 connections) — `server/utils/audit_logger.py`
- **Log administrative actions against players.          Args:             admin_nam** (1 connections) — `server/utils/audit_logger.py`
- **Log general security events.          Used for rate limit violations, injection** (1 connections) — `server/utils/audit_logger.py`
- *... and 13 more nodes in this community*

## Relationships

- [[NPC Admin API]] (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_audit_logger.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 114 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
