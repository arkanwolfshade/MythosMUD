# server monitoring memory leak metrics

> 29 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (30 connections) — `server/monitoring/memory_leak_metrics.py`
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
- **Collect event metrics from EventBus. Returns: Dictionary with event metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect NATS subscription metrics from NATSService. Returns: Dictionary with…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Unified metrics collector for memory leak detection. Aggregates metrics from…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rate for a single metric. Args: current: Current metrics…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rates for metrics over time. Returns: Dictionary mapping…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Check connection-related alerts and append to alerts list.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Check subscriber growth rate alerts and append to alerts list.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Check cache-related alerts and append to alerts list.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 4 more nodes in this community*

## Relationships

- [server api monitoring](server_api_monitoring.md) (6 shared connections)
- [server api monitoring models](server_api_monitoring_models.md) (3 shared connections)
- [server app lifespan](server_app_lifespan.md) (3 shared connections)
- [server tests unit monitoring test](server_tests_unit_monitoring_test.md) (2 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (2 shared connections)
- [server monitoring init getattr](server_monitoring_init_getattr.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)
- [performancestats](performancestats.md) (1 shared connections)
- [server caching cache service](server_caching_cache_service.md) (1 shared connections)
- [server app task registry get](server_app_task_registry_get.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 67 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*