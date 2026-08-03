# room cache services

> 40 nodes

## Key Concepts

- **MonitoringDashboard** (31 connections) — `server/monitoring/monitoring_dashboard.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._calculate_performance_score()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_alert_history()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._determine_health_status()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_active_users()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_system_load()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_disk_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (2 connections)
- **Represents a system alert.** (1 connections) — `server/monitoring/monitoring_dashboard.py`
- **Comprehensive monitoring dashboard system.      This class provides a centralize** (1 connections) — `server/monitoring/monitoring_dashboard.py`
- **Get overall system health status.          Returns:             Current system h** (1 connections) — `server/monitoring/monitoring_dashboard.py`
- **Get comprehensive monitoring summary.          Returns:             Complete mon** (1 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 15 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (19 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [command combat models](command_combat_models.md) (2 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (2 shared connections)
- [System Metrics](System_Metrics.md) (1 shared connections)

## Source Files

- `server/monitoring/monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 138 (90%)
- INFERRED: 15 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*