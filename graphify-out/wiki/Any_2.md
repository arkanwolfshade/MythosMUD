# Any

> 13 nodes

## Key Concepts

- **Any** (9 connections)
- **.to_dict()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_active_alerts()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_all_alerts()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_metrics_history()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_monitoring_summary()** (3 connections) — `server/services/combat_monitoring_service.py`
- **record_combat_error()** (3 connections) — `server/services/combat_monitoring_service.py`
- **Get metrics history. Args: limit: Optional limit on number of records Returns:…** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get active alerts. Returns: List[Dict[str, Any]]: Active alerts** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get all alerts. Returns: List[Dict[str, Any]]: All alerts** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get monitoring summary. Returns: Dict[str, Any]]: Monitoring summary** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convenience function to record combat error. Args: error_type: Type of error…** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convert to dictionary.** (1 connections) — `server/services/combat_monitoring_service.py`

## Relationships

- [CombatMonitoringService](CombatMonitoringService.md) (5 shared connections)
- [._generate_alert](_generate_alert.md) (2 shared connections)
- [CombatMetrics](CombatMetrics.md) (1 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*