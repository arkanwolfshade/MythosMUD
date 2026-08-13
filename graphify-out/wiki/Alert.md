# Alert

> 7 nodes

## Key Concepts

- **Alert** (5 connections) — `server/services/combat_monitoring_service.py`
- **.to_dict()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.add_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.remove_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **Convert to dictionary.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Add alert callback function. Args: callback: Function to call when alert is…** (1 connections) — `server/services/combat_monitoring_service.py`
- **Remove alert callback function. Args: callback: Function to remove** (1 connections) — `server/services/combat_monitoring_service.py`

## Relationships

- [CombatMonitoringService](CombatMonitoringService.md) (2 shared connections)
- [._generate_alert](_generate_alert.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*