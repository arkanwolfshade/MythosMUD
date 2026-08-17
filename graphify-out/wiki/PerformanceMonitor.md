# PerformanceMonitor

> 54 nodes

## Key Concepts

- **PerformanceMonitor** (32 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (21 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (21 connections) — `server/monitoring/performance_monitor.py`
- **test_performance_monitor.py** (19 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **get_performance_monitor()** (15 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (8 connections) — `server/monitoring/performance_monitor.py`
- **get_performance_stats()** (7 connections) — `server/monitoring/performance_monitor.py`
- **record_performance_metric()** (7 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **reset_performance_metrics()** (6 connections) — `server/monitoring/performance_monitor.py`
- **Any** (6 connections)
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.get_operation_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.add_alert_callback()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_all_stats()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_recent_metrics()** (4 connections) — `server/monitoring/performance_monitor.py`
- **test_module_level_helpers_use_global_monitor()** (4 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **.get_failed_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.get_slow_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (3 connections) — `server/monitoring/performance_monitor.py`
- **test_measure_performance_success_and_failure()** (3 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **.reset_metrics()** (2 connections) — `server/monitoring/performance_monitor.py`
- **_reset_global_monitor()** (2 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- *... and 29 more nodes in this community*

## Relationships

- [MonitoringDashboard](MonitoringDashboard.md) (9 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (8 shared connections)
- [service.py](service.py.md) (4 shared connections)
- [testing_examples.py](testing_examples.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [general_exception_handler](general_exception_handler.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [LogAggregator](LogAggregator.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)

## Source Files

- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 128 (90%)
- INFERRED: 14 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*