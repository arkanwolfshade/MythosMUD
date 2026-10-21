# test_player_preferences_service.py

> 32 nodes · cohesion 0.10

## Key Concepts

- **AuditLogger** (17 connections) — `server/utils/audit_logger.py`
- **._write_entry()** (10 connections) — `server/utils/audit_logger.py`
- **._entries_from_log_file()** (7 connections) — `server/utils/audit_logger.py`
- **._matching_entry_from_line()** (6 connections) — `server/utils/audit_logger.py`
- **JsonMap** (6 connections)
- **.get_recent_entries()** (5 connections) — `server/utils/audit_logger.py`
- **._get_log_file_path()** (4 connections) — `server/utils/audit_logger.py`
- **.get_statistics()** (4 connections) — `server/utils/audit_logger.py`
- **.__init__()** (4 connections) — `server/utils/audit_logger.py`
- **_json_map_from_line()** (4 connections) — `server/utils/audit_logger.py`
- **.log_alias_expansion()** (3 connections) — `server/utils/audit_logger.py`
- **.log_command()** (3 connections) — `server/utils/audit_logger.py`
- **.log_container_interaction()** (3 connections) — `server/utils/audit_logger.py`
- **.log_permission_change()** (3 connections) — `server/utils/audit_logger.py`
- **.log_player_action()** (3 connections) — `server/utils/audit_logger.py`
- **.log_security_event()** (3 connections) — `server/utils/audit_logger.py`
- **datetime** (3 connections)
- **Path** (3 connections)
- **Get the current audit log file path. Creates daily log files for easier…** (1 connections) — `server/utils/audit_logger.py`
- **Log security-sensitive command execution. Creates a structured audit log entry…** (1 connections) — `server/utils/audit_logger.py`
- **Log permission/role changes. Args: admin_name: Admin who made the change…** (1 connections) — `server/utils/audit_logger.py`
- **Log container interaction events for security and compliance. Args: event: The…** (1 connections) — `server/utils/audit_logger.py`
- **Log administrative actions against players. Args: admin_name: Admin who…** (1 connections) — `server/utils/audit_logger.py`
- **Log general security events. Used for rate limit violations, injection…** (1 connections) — `server/utils/audit_logger.py`
- **Log alias expansions for security monitoring. Tracks alias usage to detect…** (1 connections) — `server/utils/audit_logger.py`
- *... and 7 more nodes in this community*

## Relationships

- [Room](Room.md) (3 shared connections)
- [Execution Steps](Execution_Steps.md) (2 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/utils/audit_logger.py`

## Audit Trail

- EXTRACTED: 55 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*