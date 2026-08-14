# lifespan.py

> 32 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (21 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **asyncio** (6 connections)
- **FastAPI** (4 connections)
- **test_cleanup_container_on_error_none()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_with_container()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_initialize_enhanced_systems()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_lifespan_happy_path()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_shutdown_with_error_handling()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_minimal()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **Any** (3 connections)
- **test_calculate_metrics_delta_connection_keys()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_calculate_metrics_delta_no_startup()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_metrics_to_file_writes_json()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_mythos_state_on_error_handles_failure()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_mythos_state_on_error_success()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **Application lifecycle management for MythosMUD server. This module handles…** (1 connections) — `server/app/lifespan.py`
- **Initialize enhanced logging and monitoring systems. Returns: LogAggregator…** (1 connections) — `server/app/lifespan.py`
- *... and 7 more nodes in this community*

## Relationships

- [lifespan_startup.py](lifespan_startup.py.md) (11 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (3 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (3 shared connections)
- [log_exception_once](log_exception_once.md) (2 shared connections)
- [RestartInvalidatingJWTStrategy](RestartInvalidatingJWTStrategy.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/tests/unit/app/test_lifespan_helpers.py`

## Audit Trail

- EXTRACTED: 115 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*