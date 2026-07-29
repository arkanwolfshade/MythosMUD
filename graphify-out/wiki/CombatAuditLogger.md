# CombatAuditLogger

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

- [test combat audit](test_combat_audit.md) (10 shared connections)
- [combat audit](combat_audit.md) (6 shared connections)
- [.get combat audit summary()](get_combat_audit_summary%28%29.md) (4 shared connections)
- [Test CombatAuditLogger.get combat audit summary()](Test_CombatAuditLogger.get_combat_audit_summary%28%29.md) (1 shared connections)
- [Test CombatAuditLogger. init () initializes](Test_CombatAuditLogger._init_%28%29_initializes.md) (1 shared connections)
- [Test CombatAuditLogger.log combat attack() logs](Test_CombatAuditLogger.log_combat_attack%28%29_logs.md) (1 shared connections)
- [Test CombatAuditLogger.log combat death() logs](Test_CombatAuditLogger.log_combat_death%28%29_logs.md) (1 shared connections)
- [Test CombatAuditLogger.log combat rate limit()](Test_CombatAuditLogger.log_combat_rate_limit%28%29.md) (1 shared connections)
- [Test CombatAuditLogger.log combat security event()](Test_CombatAuditLogger.log_combat_security_event%28%29.md) (1 shared connections)
- [Test CombatAuditLogger.log combat start() logs](Test_CombatAuditLogger.log_combat_start%28%29_logs.md) (1 shared connections)
- [Test global combat audit logger](Test_global_combat_audit_logger.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`
- `server/tests/unit/structured_logging/test_combat_audit.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*