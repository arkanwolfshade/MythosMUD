# test_memory_leak_metrics.py

> 45 nodes

## Key Concepts

- **test_memory_leak_metrics.py** (24 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **memory_leak_metrics.py** (13 connections) — `server/monitoring/memory_leak_metrics.py`
- **collector()** (4 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_calculate_growth_rates()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_calculate_growth_rates_insufficient_history()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_cache_capacity()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_closed_websockets_threshold()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_no_alerts()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_subscriber_growth_rate()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_task_growth_rate()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_all_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_all_metrics_error_handling()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_cache_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_connection_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_connection_metrics_no_manager()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_event_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_event_metrics_no_bus()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_nats_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_task_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collector_initialization()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_metrics_collection_performance()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_metrics_history_bounded()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **fixture** (1 connections)
- **Memory leak metrics collector for MythosMUD. This module provides comprehensive…** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Unit tests for memory leak metrics collector. Tests the…** (1 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- *... and 20 more nodes in this community*

## Relationships

- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/tests/unit/monitoring/test_memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 57 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*