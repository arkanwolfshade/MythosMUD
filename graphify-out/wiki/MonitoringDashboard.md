# MonitoringDashboard

> 106 nodes

## Key Concepts

- **MonitoringDashboard** (34 connections) — `server/monitoring/monitoring_dashboard.py`
- **MemoryLeakMetricsCollector** (32 connections) — `server/monitoring/memory_leak_metrics.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **Alert** (16 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **LogAggregationStats** (12 connections) — `server/structured_logging/log_aggregator.py`
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **PerformanceStats** (10 connections) — `server/monitoring/performance_monitor.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **SystemHealth** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **__getattr__()** (6 connections) — `server/monitoring/__init__.py`
- *... and 81 more nodes in this community*

## Relationships

- [Any](Any.md) (13 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (13 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [monitoring_models.py](monitoring_models.py.md) (11 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (9 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (9 shared connections)
- [LogAggregator](LogAggregator.md) (7 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (6 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (4 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 294 (92%)
- INFERRED: 24 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*