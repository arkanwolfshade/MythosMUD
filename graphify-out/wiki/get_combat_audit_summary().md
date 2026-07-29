# .get combat audit summary()

> 9 nodes

## Key Concepts

- **.log_combat_security_event()** (4 connections) — `server/structured_logging/combat_audit.py`
- **Any** (4 connections)
- **.log_combat_validation_failure()** (4 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_monitoring_alert()** (4 connections) — `server/structured_logging/combat_audit.py`
- **.get_combat_audit_summary()** (3 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat-related security event.          Args:             event_type: Type** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat validation failure.          Args:             player_id: ID of the** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat monitoring alert.          Args:             alert_type: Type of al** (1 connections) — `server/structured_logging/combat_audit.py`
- **Get a summary of combat audit events.          Args:             player_id: ID o** (1 connections) — `server/structured_logging/combat_audit.py`

## Relationships

- [CombatAuditLogger](CombatAuditLogger.md) (4 shared connections)
- [combat audit](combat_audit.md) (3 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*