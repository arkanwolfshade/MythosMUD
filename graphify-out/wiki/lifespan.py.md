# lifespan.py

> 153 nodes

## Key Concepts

- **lifespan.py** (44 connections) — `server/app/lifespan.py`
- **test_lifespan_startup.py** (39 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_lifespan_helpers.py** (21 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **asyncio** (18 connections)
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- *... and 128 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (31 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (15 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (11 shared connections)
- [test_users.py](test_users.py.md) (7 shared connections)
- [MythosChronicle](MythosChronicle.md) (5 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (4 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (3 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (3 shared connections)
- [User](User.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`

## Audit Trail

- EXTRACTED: 374 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*