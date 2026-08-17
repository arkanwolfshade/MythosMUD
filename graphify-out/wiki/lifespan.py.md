# lifespan.py

> 69 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (22 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_jwt_strategy.py** (10 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **auth/conftest.py** (8 connections) — `server/tests/unit/auth/conftest.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **asyncio** (6 connections)
- **test_read_token_rejects_missing_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_read_token_rejects_wrong_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **set_auth_epoch_for_tests()** (4 connections) — `server/tests/unit/auth/conftest.py`
- **FastAPI** (4 connections)
- *... and 44 more nodes in this community*

## Relationships

- [User](User.md) (13 shared connections)
- [get_monitoring_dashboard](get_monitoring_dashboard.md) (7 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [HolidayService](HolidayService.md) (4 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (3 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`

## Audit Trail

- EXTRACTED: 189 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*