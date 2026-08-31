# PerformanceMonitor

> 74 nodes

## Key Concepts

- **PerformanceMonitor** (35 connections) — `server/monitoring/performance_monitor.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **performance_monitor.py** (24 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (20 connections) — `server/monitoring/performance_monitor.py`
- **test_performance_monitor.py** (19 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **get_performance_monitor()** (16 connections) — `server/monitoring/performance_monitor.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **ExceptionStats** (10 connections) — `server/monitoring/exception_tracker.py`
- **PerformanceStats** (10 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **MonitoringSummary** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **record_performance_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **reset_performance_metrics()** (6 connections) — `server/monitoring/performance_monitor.py`
- **get_performance_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.get_operation_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- **ExportMetrics** (4 connections) — `server/monitoring/performance_monitor.py`
- **._evict_operation_stats()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_all_stats()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_recent_metrics()** (4 connections) — `server/monitoring/performance_monitor.py`
- **test_module_level_helpers_use_global_monitor()** (4 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **RecentMetricExport** (3 connections) — `server/monitoring/performance_monitor.py`
- *... and 49 more nodes in this community*

## Relationships

- [MonitoringDashboard](MonitoringDashboard.md) (14 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (12 shared connections)
- [lifespan.py](lifespan.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (5 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (4 shared connections)
- [testing_examples.py](testing_examples.py.md) (4 shared connections)
- [service.py](service.py.md) (3 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 184 (92%)
- INFERRED: 16 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*