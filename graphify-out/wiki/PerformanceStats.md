# PerformanceStats

> 42 nodes

## Key Concepts

- **MonitoringDashboard** (31 connections) — `server/monitoring/monitoring_dashboard.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._calculate_performance_score()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
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
- *... and 17 more nodes in this community*

## Relationships

- [.shutdown()](shutdown%28%29.md) (19 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [fastapi integration](fastapi_integration.md) (3 shared connections)
- [aggregate log entry()](aggregate_log_entry%28%29.md) (3 shared connections)
- [Lock](Lock.md) (2 shared connections)

## Source Files

- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 150 (89%)
- INFERRED: 18 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*