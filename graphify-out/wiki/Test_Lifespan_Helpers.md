# Test Lifespan Helpers

> 24 nodes

## Key Concepts

- **test_lifespan_helpers.py** (20 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **asyncio** (10 connections)
- **_mock_task_registry()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_swallows_cleanup_errors()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **_close_registered_coro()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_runs_cleanup()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_metrics_to_file_writes_json()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_minimal()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_registers_dlq_cleanup_when_nats_available()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_none()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_with_container()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_initialize_enhanced_systems()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_lifespan_happy_path()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_mythos_state_on_error_handles_failure()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_shutdown_with_error_handling()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_calculate_metrics_delta_connection_keys()** (1 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_calculate_metrics_delta_no_startup()** (1 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_mythos_state_on_error_success()** (1 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **MonkeyPatch** (1 connections)
- **Path** (1 connections)
- **Unit tests for lifespan helper functions.** (1 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **A failing cleanup run must be logged and not crash/raise out of the periodic…** (1 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **MagicMock register_task stand-in: close the coro so it is not left unawaited.** (1 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **Each wake-up should invoke cleanup_old_messages via to_thread; cancellation re-…** (1 connections) — `server/tests/unit/app/test_lifespan_helpers.py`

## Relationships

- [Test Websocket Handler Validation Errors](Test_Websocket_Handler_Validation_Errors.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (1 shared connections)

## Source Files

- `server/tests/unit/app/test_lifespan_helpers.py`

## Audit Trail

- EXTRACTED: 36 (92%)
- INFERRED: 3 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*