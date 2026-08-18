# lifespan.py

> 69 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (30 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_lifespan_helpers.py** (22 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **Any** (10 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **asyncio** (6 connections)
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 44 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (20 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (7 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (7 shared connections)
- [MythosChronicle](MythosChronicle.md) (4 shared connections)
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) (3 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)
- [test_users.py](test_users.py.md) (3 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`

## Audit Trail

- EXTRACTED: 198 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*