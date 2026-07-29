# memory leak metrics

> 37 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **Any** (10 connections)
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **health_service.py** (9 connections) — `server/services/health_service.py`
- **memory_leak_metrics.py** (8 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (2 connections) — `server/monitoring/memory_leak_metrics.py`
- **Memory leak metrics collector for MythosMUD.  This module provides comprehensive** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Unified metrics collector for memory leak detection.      Aggregates metrics fro** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Initialize the memory leak metrics collector.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect all metrics from all sources.          Returns:             Dictionary c** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect connection metrics from ConnectionManager.          Returns:** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect event metrics from EventBus.          Returns:             Dictionary wi** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 12 more nodes in this community*

## Relationships

- [monitoring](monitoring.md) (8 shared connections)
- [main()](main%28%29.md) (6 shared connections)
- [lifespan](lifespan.md) (5 shared connections)
- [PerformanceStats](PerformanceStats.md) (4 shared connections)
- [test memory leak metrics](test_memory_leak_metrics.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [ConnectionsComponent](ConnectionsComponent.md) (2 shared connections)
- [get health service()](get_health_service%28%29.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [connection manager api](connection_manager_api.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/connection_manager.py`
- `server/services/health_service.py`

## Audit Trail

- EXTRACTED: 149 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*