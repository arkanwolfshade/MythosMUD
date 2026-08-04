# audit logger rationale

> 46 nodes

## Key Concepts

- **test_audit_logger.py** (15 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **AuditLogger** (15 connections) — `server/utils/audit_logger.py`
- **_logger()** (13 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **._write_entry()** (10 connections) — `server/utils/audit_logger.py`
- **Any** (6 connections)
- **.__init__()** (4 connections) — `server/utils/audit_logger.py`
- **._get_log_file_path()** (4 connections) — `server/utils/audit_logger.py`
- **.log_command()** (4 connections) — `server/utils/audit_logger.py`
- **.log_container_interaction()** (4 connections) — `server/utils/audit_logger.py`
- **.log_security_event()** (4 connections) — `server/utils/audit_logger.py`
- **.get_recent_entries()** (4 connections) — `server/utils/audit_logger.py`
- **.get_statistics()** (4 connections) — `server/utils/audit_logger.py`
- **test_audit_logger_init()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_command()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_permission_change()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_player_action()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_get_recent_entries()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_get_recent_entries_filters_and_bad_lines()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_get_statistics()** (3 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **.log_permission_change()** (3 connections) — `server/utils/audit_logger.py`
- **.log_player_action()** (3 connections) — `server/utils/audit_logger.py`
- **.log_alias_expansion()** (3 connections) — `server/utils/audit_logger.py`
- **test_audit_logger_log_security_event_severity_branches()** (2 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_alias_expansion_cycle()** (2 connections) — `server/tests/unit/utils/test_audit_logger.py`
- **test_audit_logger_log_container_interaction()** (2 connections) — `server/tests/unit/utils/test_audit_logger.py`
- *... and 21 more nodes in this community*

## Relationships

- [task registry app](task_registry_app.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_audit_logger.py`
- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 147 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*