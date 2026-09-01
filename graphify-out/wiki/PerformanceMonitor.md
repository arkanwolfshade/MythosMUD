# PerformanceMonitor

> 61 nodes

## Key Concepts

- **PerformanceMonitor** (35 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (24 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (20 connections) — `server/monitoring/performance_monitor.py`
- **test_performance_monitor.py** (19 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **get_performance_monitor()** (16 connections) — `server/monitoring/performance_monitor.py`
- **.initialize()** (11 connections) — `server/container/bundles/monitoring.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
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
- **.add_alert_callback()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.get_failed_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.get_slow_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (3 connections) — `server/monitoring/performance_monitor.py`
- **test_measure_performance_success_and_failure()** (3 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- *... and 36 more nodes in this community*

## Relationships

- [ExceptionTracker](ExceptionTracker.md) (10 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (5 shared connections)
- [testing_examples.py](testing_examples.py.md) (4 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [service.py](service.py.md) (3 shared connections)
- [correct_patterns.py](correct_patterns.py.md) (3 shared connections)
- [log_with_context](log_with_context.md) (3 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (1 shared connections)

## Source Files

- `server/container/bundles/monitoring.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 147 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*