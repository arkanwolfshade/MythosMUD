# Server Structured Logging (14)

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

- [Server Structured Logging (13)](Server_Structured_Logging_%2813%29.md) (4 shared connections)
- [Server Structured Logging (11)](Server_Structured_Logging_%2811%29.md) (3 shared connections)

## Source Files

- `server/structured_logging/combat_audit.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*