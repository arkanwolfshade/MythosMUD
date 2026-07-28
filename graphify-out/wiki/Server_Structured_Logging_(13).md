# Server Structured Logging (13)

> 10 nodes

## Key Concepts

- **CombatAuditLogger** (30 connections) — `server/structured_logging/combat_audit.py`
- **.__init__()** (3 connections) — `server/structured_logging/combat_audit.py`
- **test_combat_audit_logger_log_combat_security_event()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_monitoring_alert_with_player()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_get_combat_audit_summary()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Specialized logger for combat events and security monitoring.      Provides stru** (1 connections) — `server/structured_logging/combat_audit.py`
- **Initialize the combat audit logger.** (1 connections) — `server/structured_logging/combat_audit.py`
- **Test CombatAuditLogger.log_combat_security_event() logs security event.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_monitoring_alert() includes player info.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.get_combat_audit_summary() returns summary.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`

## Relationships

- [Server Structured Logging (12)](Server_Structured_Logging_%2812%29.md) (10 shared connections)
- [Server Structured Logging (11)](Server_Structured_Logging_%2811%29.md) (6 shared connections)
- [Server Structured Logging (14)](Server_Structured_Logging_%2814%29.md) (4 shared connections)
- [Server Structured Logging (22)](Server_Structured_Logging_%2822%29.md) (1 shared connections)
- [Server Structured Logging (18)](Server_Structured_Logging_%2818%29.md) (1 shared connections)
- [Server Structured Logging (24)](Server_Structured_Logging_%2824%29.md) (1 shared connections)
- [Server Structured Logging (25)](Server_Structured_Logging_%2825%29.md) (1 shared connections)
- [Server Structured Logging (20)](Server_Structured_Logging_%2820%29.md) (1 shared connections)
- [Server Structured Logging (19)](Server_Structured_Logging_%2819%29.md) (1 shared connections)
- [Server Structured Logging (21)](Server_Structured_Logging_%2821%29.md) (1 shared connections)
- [Server Structured Logging (23)](Server_Structured_Logging_%2823%29.md) (1 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`
- `server/tests/unit/structured_logging/test_combat_audit.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*