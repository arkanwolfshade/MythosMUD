# lifespan.py

> 98 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (32 connections) — `server/monitoring/memory_leak_metrics.py`
- **PerformanceMonitor** (25 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (19 connections) — `server/monitoring/performance_monitor.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **PerformanceMetric** (8 connections) — `server/monitoring/performance_monitor.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **Any** (6 connections)
- *... and 73 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (19 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (18 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (16 shared connections)
- [get_cache_manager](get_cache_manager.md) (14 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_users.py](test_users.py.md) (6 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (6 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (5 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (5 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (4 shared connections)
- [LogAggregator](LogAggregator.md) (4 shared connections)
- [testing_examples.py](testing_examples.py.md) (4 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 292 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*