# Structured Logging Combat

> 12 nodes · cohesion 0.17

## Key Concepts

- **CombatAuditLogger** (29 connections) — `server/structured_logging/combat_audit.py`
- **.__init__()** (3 connections) — `server/structured_logging/combat_audit.py`
- **test_combat_audit_logger_get_combat_audit_summary()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_monitoring_alert_with_player()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_security_event()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_security_event_no_additional_data()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Specialized logger for combat events and security monitoring.      Provides stru** (1 connections) — `server/structured_logging/combat_audit.py`
- **Initialize the combat audit logger.** (1 connections) — `server/structured_logging/combat_audit.py`
- **Test CombatAuditLogger.log_combat_security_event() logs security event.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_security_event() handles no additional data.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_monitoring_alert() includes player info.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.get_combat_audit_summary() returns summary.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`

## Relationships

- [[Structured Logging Combat]] (27 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`
- `server/tests/unit/structured_logging/test_combat_audit.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
