# Structured Logging Combat

> 9 nodes · cohesion 0.22

## Key Concepts

- **Any** (4 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_monitoring_alert()** (4 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_security_event()** (4 connections) — `server/structured_logging/combat_audit.py`
- **.log_combat_validation_failure()** (4 connections) — `server/structured_logging/combat_audit.py`
- **.get_combat_audit_summary()** (3 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat-related security event.          Args:             event_type: Type** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat validation failure.          Args:             player_id: ID of the** (1 connections) — `server/structured_logging/combat_audit.py`
- **Log a combat monitoring alert.          Args:             alert_type: Type of al** (1 connections) — `server/structured_logging/combat_audit.py`
- **Get a summary of combat audit events.          Args:             player_id: ID o** (1 connections) — `server/structured_logging/combat_audit.py`

## Relationships

- [[Structured Logging Combat]] (7 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
