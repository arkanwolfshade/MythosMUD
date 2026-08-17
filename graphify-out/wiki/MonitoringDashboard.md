# MonitoringDashboard

> 62 nodes

## Key Concepts

- **MonitoringDashboard** (35 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **.check_alerts()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **SystemHealth** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._calculate_performance_score()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **._determine_health_status()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_active_users()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_alert_history()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_disk_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_system_load()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 37 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (16 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [log_with_context](log_with_context.md) (3 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)

## Source Files

- `server/container/bundles/monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 124 (90%)
- INFERRED: 14 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*