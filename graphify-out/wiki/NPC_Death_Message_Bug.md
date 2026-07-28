# NPC Death Message Bug

> 16 nodes · cohesion 0.12

## Key Concepts

- **test_combat_audit.py** (20 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_init()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_attack()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_end()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_monitoring_alert_high()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_security_event()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_security_event_no_additional_data()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **test_combat_audit_logger_log_combat_validation_failure()** (3 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Unit tests for combat audit logging.  Tests the combat_audit module classes and** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_end() logs combat end.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_security_event() logs security event.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.__init__() initializes logger.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_security_event() handles no additional data.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_validation_failure() logs validation failure.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_monitoring_alert() logs high severity alert.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`
- **Test CombatAuditLogger.log_combat_attack() logs combat attack.** (1 connections) — `server/tests/unit/structured_logging/test_combat_audit.py`

## Relationships

- [Cursor Plans Login](Cursor_Plans_Login.md) (11 shared connections)
- [E 2 E Whisper System](E_2_E_Whisper_System.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Community 1617](Community_1617.md) (1 shared connections)
- [E 2 E Execution Guards](E_2_E_Execution_Guards.md) (1 shared connections)
- [Community 1616](Community_1616.md) (1 shared connections)
- [Player Command Developer](Player_Command_Developer.md) (1 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_combat_audit.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*