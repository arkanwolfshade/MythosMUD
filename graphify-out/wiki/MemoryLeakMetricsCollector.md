# MemoryLeakMetricsCollector

> 32 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (30 connections) — `server/monitoring/memory_leak_metrics.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
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
- **test_resolve_memory_leak_collector_singleton_resets_with_patch()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Get or create MemoryLeakMetricsCollector instance. Returns:…** (1 connections) — `server/api/monitoring.py`
- **Collect event metrics from EventBus. Returns: Dictionary with event metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect NATS subscription metrics from NATSService. Returns: Dictionary with…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Unified metrics collector for memory leak detection. Aggregates metrics from…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rate for a single metric. Args: current: Current metrics…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rates for metrics over time. Returns: Dictionary mapping…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 7 more nodes in this community*

## Relationships

- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (8 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (3 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (2 shared connections)
- [test_memory_leak_metrics.py](test_memory_leak_metrics.py.md) (2 shared connections)
- [NPCStartupService](NPCStartupService.md) (2 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 77 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*