# test_lifespan_helpers.py

> 28 nodes

## Key Concepts

- **test_lifespan_helpers.py** (22 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
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
- **Perform application shutdown with comprehensive error handling. Args: app:…** (1 connections) — `server/app/lifespan.py`
- **Attempt to persist mythos chronicle state during error conditions.** (1 connections) — `server/app/lifespan.py`
- **Attempt to cleanup container during error conditions.** (1 connections) — `server/app/lifespan.py`
- **Application lifespan manager with comprehensive monitoring and logging. Handles…** (1 connections) — `server/app/lifespan.py`
- *... and 3 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (20 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (3 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [create_app](create_app.md) (1 shared connections)
- [.error](error.md) (1 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/tests/unit/app/test_lifespan_helpers.py`

## Audit Trail

- EXTRACTED: 76 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*