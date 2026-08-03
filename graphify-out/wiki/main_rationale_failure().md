# main rationale failure()

> 13 nodes

## Key Concepts

- **Any** (9 connections)
- **.to_dict()** (7 connections) — `server/services/combat_monitoring_service.py`
- **.get_metrics_history()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_active_alerts()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_all_alerts()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_monitoring_summary()** (4 connections) — `server/services/combat_monitoring_service.py`
- **record_combat_error()** (3 connections) — `server/services/combat_monitoring_service.py`
- **Convert to dictionary.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get metrics history.          Args:             limit: Optional limit on number** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get active alerts.          Returns:             List[Dict[str, Any]]: Active al** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get all alerts.          Returns:             List[Dict[str, Any]]: All alerts** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get monitoring summary.          Returns:             Dict[str, Any]]: Monitorin** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convenience function to record combat error.      Args:         error_type: Type** (1 connections) — `server/services/combat_monitoring_service.py`

## Relationships

- [combat monitoring service](combat_monitoring_service.md) (5 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (2 shared connections)
- [event bus events](event_bus_events.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*