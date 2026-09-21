# lifespan.py

> 50 nodes

## Key Concepts

- **lifespan.py** (45 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (28 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (16 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **asyncio** (10 connections)
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_cleanup_dead_letter_queue_periodically()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **_mock_task_registry()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_runs_cleanup()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_swallows_cleanup_errors()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_metrics_to_file_writes_json()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_minimal()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_registers_dlq_cleanup_when_nats_available()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **FastAPI** (4 connections)
- **_close_registered_coro()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_none()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_with_container()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_initialize_enhanced_systems()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- *... and 25 more nodes in this community*

## Relationships

- [lifespan_startup.py](lifespan_startup.py.md) (9 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (4 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (4 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [LogAggregator](LogAggregator.md) (3 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (3 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)
- [endpoints.py](endpoints.py.md) (3 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`

## Audit Trail

- EXTRACTED: 156 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*