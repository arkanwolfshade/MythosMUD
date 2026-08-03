# metrics memory leak

> 40 nodes

## Key Concepts

- **test_memory_leak_metrics.py** (23 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collector_initialization()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_connection_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_connection_metrics_no_manager()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_event_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_event_metrics_no_bus()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_cache_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_task_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_nats_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_all_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_calculate_growth_rates()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_calculate_growth_rates_insufficient_history()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_closed_websockets_threshold()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_subscriber_growth_rate()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_cache_capacity()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_task_growth_rate()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_no_alerts()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_metrics_collection_performance()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_metrics_history_bounded()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_all_metrics_error_handling()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **Unit tests for memory leak metrics collector.  Tests the MemoryLeakMetricsCollec** (1 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **Test MemoryLeakMetricsCollector initialization.** (1 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **Test collection of connection metrics.** (1 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **Test collection of connection metrics when manager is not available.** (1 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **Test collection of event metrics.** (1 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- *... and 15 more nodes in this community*

## Relationships

- [message nats handler](message_nats_handler.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/monitoring/test_memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 81 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*