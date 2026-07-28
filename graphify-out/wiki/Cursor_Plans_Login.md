# Cursor Plans Login

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

- [NPC Death Message Bug](NPC_Death_Message_Bug.md) (11 shared connections)
- [Structured Logging Combat](Structured_Logging_Combat.md) (9 shared connections)
- [E 2 E Whisper System](E_2_E_Whisper_System.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Community 1617](Community_1617.md) (1 shared connections)
- [E 2 E Execution Guards](E_2_E_Execution_Guards.md) (1 shared connections)
- [Community 1616](Community_1616.md) (1 shared connections)
- [Player Command Developer](Player_Command_Developer.md) (1 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`
- `server/tests/unit/structured_logging/test_combat_audit.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*