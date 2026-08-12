# lifespan.py

> 116 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **asyncio** (14 connections)
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **SystemAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- *... and 91 more nodes in this community*

## Relationships

- [api/monitoring.py](api-monitoring.py.md) (13 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (12 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (7 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (6 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [factory.py](factory.py.md) (5 shared connections)
- [User](User.md) (4 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (4 shared connections)
- [test_users.py](test_users.py.md) (3 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 294 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*