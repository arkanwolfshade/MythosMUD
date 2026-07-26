# lifespan.py

> 365 nodes · cohesion 0.01

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **MonitoringDashboard** (31 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceMonitor** (24 connections) — `server/monitoring/performance_monitor.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **ExceptionTracker** (23 connections) — `server/monitoring/exception_tracker.py`
- **websocket_integration.py** (22 connections) — `docs/examples/logging/websocket_integration.py`
- **correct_patterns.py** (20 connections) — `docs/examples/logging/correct_patterns.py`
- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (20 connections) — `server/monitoring/performance_monitor.py`
- **exception_tracker.py** (18 connections) — `server/monitoring/exception_tracker.py`
- **log_with_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **track_exception()** (15 connections) — `server/monitoring/exception_tracker.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- *... and 340 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (18 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (18 shared connections)
- [monitoring.py](monitoring.py.md) (17 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (15 shared connections)
- [User](User.md) (11 shared connections)
- [bind_request_context](bind_request_context.md) (10 shared connections)
- [LogAggregator](LogAggregator.md) (8 shared connections)
- [enhanced_error_logging.py](enhanced_error_logging.py.md) (8 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (7 shared connections)
- [testing_examples.py](testing_examples.py.md) (7 shared connections)
- [test_lifespan_startup.py](test_lifespan_startup.py.md) (6 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (6 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/websocket_integration.py`
- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 1363 (94%)
- INFERRED: 93 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*