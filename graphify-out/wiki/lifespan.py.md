# lifespan.py

> 134 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **factory.py** (37 connections) — `server/app/factory.py`
- **MemoryLeakMetricsCollector** (32 connections) — `server/monitoring/memory_leak_metrics.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **log_aggregator.py** (14 connections) — `server/structured_logging/log_aggregator.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **Any** (10 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- *... and 109 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (36 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (17 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (17 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (16 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (14 shared connections)
- [server/main.py](server-main.py.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [User](User.md) (7 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (6 shared connections)
- [LogAggregator](LogAggregator.md) (6 shared connections)
- [database.py](database.py.md) (5 shared connections)
- [test_users.py](test_users.py.md) (4 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/app/factory.py`
- `server/app/lifespan.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 650 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*