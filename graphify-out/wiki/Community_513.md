# Community 513

> 33 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (28 connections) — `server/monitoring/memory_leak_metrics.py`
- **Any** (11 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (6 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **Log memory leak metrics periodically. Args: collector:…** (1 connections) — `server/app/lifespan.py`
- **Collect event metrics from EventBus. Returns: Dictionary with event metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect NATS subscription metrics from NATSService. Returns: Dictionary with…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Unified metrics collector for memory leak detection. Aggregates metrics from…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rate for a single metric. Args: current: Current metrics…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rates for metrics over time. Returns: Dictionary mapping…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 8 more nodes in this community*

## Relationships

- [Community 362](Community_362.md) (4 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (3 shared connections)
- [Community 239](Community_239.md) (2 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (2 shared connections)
- [Community 93](Community_93.md) (2 shared connections)
- [Community 183](Community_183.md) (1 shared connections)
- [Community 255](Community_255.md) (1 shared connections)
- [Community 312](Community_312.md) (1 shared connections)
- [Community 105](Community_105.md) (1 shared connections)
- [Community 408](Community_408.md) (1 shared connections)
- [Community 1420](Community_1420.md) (1 shared connections)
- [Community 387](Community_387.md) (1 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/monitoring/memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 70 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*