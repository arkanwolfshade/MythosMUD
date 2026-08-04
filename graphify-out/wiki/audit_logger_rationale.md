# audit logger rationale

> 26 nodes

## Key Concepts

- **AuditLogger** (15 connections) — `server/utils/audit_logger.py`
- **._write_entry()** (10 connections) — `server/utils/audit_logger.py`
- **Any** (6 connections)
- **.__init__()** (4 connections) — `server/utils/audit_logger.py`
- **._get_log_file_path()** (4 connections) — `server/utils/audit_logger.py`
- **.log_command()** (4 connections) — `server/utils/audit_logger.py`
- **.log_container_interaction()** (4 connections) — `server/utils/audit_logger.py`
- **.log_security_event()** (4 connections) — `server/utils/audit_logger.py`
- **.get_recent_entries()** (4 connections) — `server/utils/audit_logger.py`
- **.get_statistics()** (4 connections) — `server/utils/audit_logger.py`
- **.log_permission_change()** (3 connections) — `server/utils/audit_logger.py`
- **.log_player_action()** (3 connections) — `server/utils/audit_logger.py`
- **.log_alias_expansion()** (3 connections) — `server/utils/audit_logger.py`
- **Path** (2 connections)
- **Audit logging for security-sensitive command execution.      Creates structured** (1 connections) — `server/utils/audit_logger.py`
- **Initialize audit logger.          Args:             log_directory: Optional dire** (1 connections) — `server/utils/audit_logger.py`
- **Get the current audit log file path.          Creates daily log files for easier** (1 connections) — `server/utils/audit_logger.py`
- **Log security-sensitive command execution.          Creates a structured audit lo** (1 connections) — `server/utils/audit_logger.py`
- **Log permission/role changes.          Args:             admin_name: Admin who ma** (1 connections) — `server/utils/audit_logger.py`
- **Log container interaction events for security and compliance.          Args:** (1 connections) — `server/utils/audit_logger.py`
- **Log administrative actions against players.          Args:             admin_nam** (1 connections) — `server/utils/audit_logger.py`
- **Log general security events.          Used for rate limit violations, injection** (1 connections) — `server/utils/audit_logger.py`
- **Log alias expansions for security monitoring.          Tracks alias usage to det** (1 connections) — `server/utils/audit_logger.py`
- **Write audit log entry to file.          Uses JSON Lines format (one JSON object** (1 connections) — `server/utils/audit_logger.py`
- **Retrieve recent audit log entries.          Useful for admin dashboards and inci** (1 connections) — `server/utils/audit_logger.py`
- *... and 1 more nodes in this community*

## Relationships

- [dead letter realtime](dead_letter_realtime.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 82 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*