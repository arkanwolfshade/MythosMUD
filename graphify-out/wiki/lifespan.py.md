# lifespan.py

> 101 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (30 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_lifespan_helpers.py** (22 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **test_main.py** (15 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **Any** (10 connections)
- **test_jwt_strategy.py** (10 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- *... and 76 more nodes in this community*

## Relationships

- [test_lifespan_startup.py](test_lifespan_startup.py.md) (16 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (15 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (12 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (7 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (6 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [test_users.py](test_users.py.md) (6 shared connections)
- [pytest.md](pytest.md.md) (6 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (5 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (4 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (4 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 294 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*