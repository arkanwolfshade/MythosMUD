# lifespan.py

> 80 nodes

## Key Concepts

- **lifespan.py** (46 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (28 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_lifespan_helpers.py** (27 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (16 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **memory_leak_metrics.py** (12 connections) — `server/monitoring/memory_leak_metrics.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **Any** (11 connections)
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **asyncio** (10 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_cleanup_dead_letter_queue_periodically()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **.collect_event_metrics()** (6 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- *... and 55 more nodes in this community*

## Relationships

- [lifespan_startup.py](lifespan_startup.py.md) (10 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (7 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_memory_leak_metrics.py](test_memory_leak_metrics.py.md) (5 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (3 shared connections)
- [factory.py](factory.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`

## Audit Trail

- EXTRACTED: 235 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*