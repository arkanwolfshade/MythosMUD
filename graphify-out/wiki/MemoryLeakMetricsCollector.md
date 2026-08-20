# MemoryLeakMetricsCollector

> 35 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (30 connections) — `server/monitoring/memory_leak_metrics.py`
- **memory_leak_metrics.py** (13 connections) — `server/monitoring/memory_leak_metrics.py`
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager.py`
- **Any** (10 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **Memory leak metrics collector for MythosMUD. This module provides comprehensive…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect event metrics from EventBus. Returns: Dictionary with event metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect NATS subscription metrics from NATSService. Returns: Dictionary with…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Unified metrics collector for memory leak detection. Aggregates metrics from…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rate for a single metric. Args: current: Current metrics…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 10 more nodes in this community*

## Relationships

- [api/monitoring.py](api-monitoring.py.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_memory_leak_metrics.py](test_memory_leak_metrics.py.md) (3 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (2 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (2 shared connections)
- [.get_instance](get_instance.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [get_monitoring_dashboard](get_monitoring_dashboard.md) (1 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 89 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*