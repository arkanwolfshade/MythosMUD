# Structured Logging Combat

> 71 nodes

## Key Concepts

- **CombatAuditLogger** (30 connections) — `server/structured_logging/combat_audit.py`
- **test_combat_audit.py** (25 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **combat_audit.py** (11 connections) — `server/structured_logging/combat_audit.py`
- **_ts()** (10 connections) — `server/structured_logging/combat_audit.py`
- **CombatParties** (8 connections) — `server/structured_logging/combat_audit.py`
- **CombatMonitoringAlert** (7 connections) — `server/structured_logging/combat_audit.py`
- **datetime** (7 connections)
- **_parties()** (7 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **CombatSecurityEvent** (6 connections) — `server/structured_logging/combat_audit.py`
- **CombatAttackDetails** (5 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_start()** (5 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_death()** (5 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_end()** (5 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_validation_failure()** (5 connections) — `server/structured_logging/combat_audit.py`
- **test_combat_audit_logger_log_combat_attack()** (5 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **.log_combat_attack()** (4 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_security_event()** (4 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_rate_limit()** (4 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_monitoring_alert()** (4 connections) — `server/structured_logging/combat_audit.py`
- **test_combat_audit_logger_log_combat_start()** (4 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_start_with_timestamp()** (4 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_death()** (4 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_end()** (4 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_security_event()** (4 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_security_event_no_additional_data()** (4 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- *... and 46 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (3 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`
- `server/tests/unit/structured_logging/test_combat_audit.py`

## Audit Trail

- EXTRACTED: 253 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*