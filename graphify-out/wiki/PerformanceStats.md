# PerformanceStats

> 50 nodes

## Key Concepts

- **MonitoringDashboard** (31 connections) — `server/monitoring/monitoring_dashboard.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **SystemHealth** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
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
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_alert_history()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._determine_health_status()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_active_users()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_system_load()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_disk_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 25 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (19 shared connections)
- [Test exception tracking functionality.](Test_exception_tracking_functionality.md) (4 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (4 shared connections)
- [.initialize()](initialize%28%29.md) (2 shared connections)
- [Lock](Lock.md) (2 shared connections)
- [aggregate log entry()](aggregate_log_entry%28%29.md) (2 shared connections)
- [lifespan](lifespan.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 171 (85%)
- INFERRED: 31 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*