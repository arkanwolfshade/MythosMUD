# test combat audit

> 13 nodes

## Key Concepts

- **test_combat_audit.py** (20 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_start_with_timestamp()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_end()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_validation_failure()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_monitoring_alert_high()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_monitoring_alert_low()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_get_combat_audit_summary_with_player()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_monitoring_alert() logs high severity alert.** (2 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Unit tests for combat audit logging.  Tests the combat_audit module classes and** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_start() uses provided timestamp.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_end() logs combat end.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_validation_failure() logs validation failure.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.get_combat_audit_summary() filters by player.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`

## Relationships

- [CombatAuditLogger](CombatAuditLogger.md) (10 shared connections)
- [combat audit](combat_audit.md) (1 shared connections)
- [Test CombatAuditLogger.get combat audit summary()](Test_CombatAuditLogger.get_combat_audit_summary%28%29.md) (1 shared connections)
- [Test CombatAuditLogger. init () initializes](Test_CombatAuditLogger._init_%28%29_initializes.md) (1 shared connections)
- [Test CombatAuditLogger.log combat attack() logs](Test_CombatAuditLogger.log_combat_attack%28%29_logs.md) (1 shared connections)
- [Test CombatAuditLogger.log combat death() logs](Test_CombatAuditLogger.log_combat_death%28%29_logs.md) (1 shared connections)
- [Test CombatAuditLogger.log combat rate limit()](Test_CombatAuditLogger.log_combat_rate_limit%28%29.md) (1 shared connections)
- [Test CombatAuditLogger.log combat security event()](Test_CombatAuditLogger.log_combat_security_event%28%29.md) (1 shared connections)
- [Test CombatAuditLogger.log combat start() logs](Test_CombatAuditLogger.log_combat_start%28%29_logs.md) (1 shared connections)
- [Test global combat audit logger](Test_global_combat_audit_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_combat_audit.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*