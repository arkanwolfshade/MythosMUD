# MonitoringDashboard

> 135 nodes

## Key Concepts

- **MonitoringDashboard** (35 connections) — `server/monitoring/monitoring_dashboard.py`
- **MemoryLeakMetricsCollector** (30 connections) — `server/monitoring/memory_leak_metrics.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **exception_tracker.py** (21 connections) — `server/monitoring/exception_tracker.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
- **get_exception_tracker()** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **ExceptionStats** (10 connections) — `server/monitoring/exception_tracker.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **Any** (10 connections)
- **PerformanceStats** (9 connections) — `server/monitoring/performance_monitor.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 110 more nodes in this community*

## Relationships

- [api/monitoring.py](api-monitoring.py.md) (17 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (13 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (13 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (12 shared connections)
- [lifespan.py](lifespan.py.md) (11 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [LogAggregator](LogAggregator.md) (7 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [RoomCacheService](RoomCacheService.md) (3 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/services/inventory_mutation_guard.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 349 (93%)
- INFERRED: 28 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*