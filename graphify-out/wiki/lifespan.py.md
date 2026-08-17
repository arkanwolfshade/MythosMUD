# lifespan.py

> 102 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (22 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **test_main.py** (15 connections) — `server/tests/unit/test_main.py`
- **asyncio** (14 connections)
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **auth/conftest.py** (8 connections) — `server/tests/unit/auth/conftest.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **asyncio** (6 connections)
- **TestLifespan** (5 connections) — `server/tests/unit/test_main.py`
- **Request** (5 connections)
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- *... and 77 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (22 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (9 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (7 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [register_user](register_user.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (4 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (3 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (3 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/auth/token_epoch.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 260 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*