# Party Service Management

> 29 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **Any** (10 connections)
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **Unified metrics collector for memory leak detection.      Aggregates metrics fro** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect all metrics from all sources.          Returns:             Dictionary c** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect connection metrics from ConnectionManager.          Returns:** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect event metrics from EventBus.          Returns:             Dictionary wi** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect cache metrics from CacheManager.          Returns:             Dictionar** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect task metrics from TaskRegistry.          Returns:             Dictionary** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect NATS subscription metrics from NATSService.          Returns:** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rate for a single metric.          Args:             current: C** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rates for metrics over time.          Returns:             Dict** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Check connection-related alerts and append to alerts list.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 4 more nodes in this community*

## Relationships

- [Monitoring Response Models](Monitoring_Response_Models.md) (8 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (6 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (3 shared connections)
- [Target Resolution Service](Target_Resolution_Service.md) (2 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (2 shared connections)
- [Enhanced Logging Guide](Enhanced_Logging_Guide.md) (1 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (1 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 116 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*