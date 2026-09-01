# lifespan.py

> 85 nodes

## Key Concepts

- **lifespan.py** (46 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (29 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **MemoryLeakMetricsCollector** (28 connections) — `server/monitoring/memory_leak_metrics.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (16 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **memory_leak_metrics.py** (12 connections) — `server/monitoring/memory_leak_metrics.py`
- **Any** (11 connections)
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **asyncio** (10 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_cleanup_dead_letter_queue_periodically()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **.collect_event_metrics()** (6 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- *... and 60 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (15 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (8 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (5 shared connections)
- [test_memory_leak_metrics.py](test_memory_leak_metrics.py.md) (5 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (4 shared connections)
- [LogAggregator](LogAggregator.md) (4 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (3 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)
- [User](User.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/app/test_lifespan_helpers.py`

## Audit Trail

- EXTRACTED: 238 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*