# ._generate_alert

> 15 nodes

## Key Concepts

- **._generate_alert()** (9 connections) — `server/services/combat_monitoring_service.py`
- **Alert** (5 connections) — `server/services/combat_monitoring_service.py`
- **._check_resource_thresholds()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.to_dict()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.add_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._check_performance_threshold()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.remove_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.update_resource_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **Convert to dictionary.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Update resource usage metrics. Args: memory_mb: Memory usage in MB cpu_percent:…** (1 connections) — `server/services/combat_monitoring_service.py`
- **Add alert callback function. Args: callback: Function to call when alert is…** (1 connections) — `server/services/combat_monitoring_service.py`
- **Remove alert callback function. Args: callback: Function to remove** (1 connections) — `server/services/combat_monitoring_service.py`
- **Check resource usage thresholds.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Check if performance threshold has been exceeded.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Generate and dispatch an alert.** (1 connections) — `server/services/combat_monitoring_service.py`

## Relationships

- [CombatMonitoringService](CombatMonitoringService.md) (7 shared connections)
- [Any](Any.md) (2 shared connections)
- [AlertType](AlertType.md) (2 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*