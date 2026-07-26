# CombatAuditLogger

> 10 nodes · cohesion 0.20

## Key Concepts

- **CombatAuditLogger** (30 connections) — `server/structured_logging/combat_audit.py`
- **.__init__()** (3 connections) — `server/structured_logging/combat_audit.py`
- **test_combat_audit_logger_get_combat_audit_summary_with_time_range()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_monitoring_alert_with_player()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_rate_limit()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Specialized logger for combat events and security monitoring.      Provides stru** (1 connections) — `server/structured_logging/combat_audit.py`
- **Initialize the combat audit logger.** (1 connections) — `server/structured_logging/combat_audit.py`
- **Test CombatAuditLogger.log_combat_rate_limit() logs rate limit.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_monitoring_alert() includes player info.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.get_combat_audit_summary() uses time range.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`

## Relationships

- [test_combat_audit.py](test_combat_audit.py.md) (11 shared connections)
- [datetime](datetime.md) (5 shared connections)
- [.log_combat_monitoring_alert](log_combat_monitoring_alert.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_combat_audit_logger_get_combat_audit_summary](test_combat_audit_logger_get_combat_audit_summary.md) (1 shared connections)
- [test_combat_audit_logger_get_combat_audit_summary_with_player](test_combat_audit_logger_get_combat_audit_summary_with_player.md) (1 shared connections)
- [test_combat_audit_logger_log_combat_death](test_combat_audit_logger_log_combat_death.md) (1 shared connections)
- [test_combat_audit_logger_log_combat_monitoring_alert_low](test_combat_audit_logger_log_combat_monitoring_alert_low.md) (1 shared connections)
- [test_combat_audit_logger_log_combat_start](test_combat_audit_logger_log_combat_start.md) (1 shared connections)
- [test_combat_audit_logger_log_combat_start_with_timestamp](test_combat_audit_logger_log_combat_start_with_timestamp.md) (1 shared connections)
- [test_global_combat_audit_logger](test_global_combat_audit_logger.md) (1 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`
- `server/tests/unit/structured_logging/test_combat_audit.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*