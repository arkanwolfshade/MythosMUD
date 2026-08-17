# MonitoringDashboard

> 79 nodes

## Key Concepts

- **MonitoringDashboard** (35 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **ExceptionStats** (10 connections) — `server/monitoring/exception_tracker.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **PerformanceStats** (9 connections) — `server/monitoring/performance_monitor.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **.check_alerts()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **MonitoringSummary** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **SystemHealth** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._calculate_performance_score()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_stats()** (3 connections) — `server/monitoring/exception_tracker.py`
- *... and 54 more nodes in this community*

## Relationships

- [PerformanceMonitor](PerformanceMonitor.md) (9 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (8 shared connections)
- [LogAggregator](LogAggregator.md) (6 shared connections)
- [get_monitoring_dashboard](get_monitoring_dashboard.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (2 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (1 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 165 (89%)
- INFERRED: 21 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*