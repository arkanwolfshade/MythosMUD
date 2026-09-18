# Community 312

> 52 nodes

## Key Concepts

- **test_lifespan_helpers.py** (28 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **_startup_application()** (16 connections) — `server/app/lifespan.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **asyncio** (10 connections)
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_cleanup_dead_letter_queue_periodically()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **TestLifespan** (5 connections) — `server/tests/unit/test_main.py`
- **_mock_task_registry()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_runs_cleanup()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_swallows_cleanup_errors()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_metrics_to_file_writes_json()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_minimal()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_registers_dlq_cleanup_when_nats_available()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **.test_lifespan_initialization_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **FastAPI** (4 connections)
- **_close_registered_coro()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_none()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_with_container()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- *... and 27 more nodes in this community*

## Relationships

- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (12 shared connections)
- [Community 105](Community_105.md) (6 shared connections)
- [Community 93](Community_93.md) (3 shared connections)
- [Community 103](Community_103.md) (3 shared connections)
- [Community 153](Community_153.md) (1 shared connections)
- [Community 239](Community_239.md) (1 shared connections)
- [Community 183](Community_183.md) (1 shared connections)
- [Community 205](Community_205.md) (1 shared connections)
- [Community 504](Community_504.md) (1 shared connections)
- [Community 57](Community_57.md) (1 shared connections)
- [Community 211](Community_211.md) (1 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (1 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 125 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*