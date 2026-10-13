# Community 317

> 52 nodes

## Key Concepts

- **lifespan.py** (41 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (28 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (16 connections) — `server/app/lifespan.py`
- **_startup_application()** (16 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **asyncio** (10 connections)
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_cleanup_dead_letter_queue_periodically()** (7 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (6 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (6 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (6 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **_close_registered_coro()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **_mock_task_registry()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_runs_cleanup()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_swallows_cleanup_errors()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_metrics_to_file_writes_json()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_minimal()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_registers_dlq_cleanup_when_nats_available()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **FastAPI** (4 connections)
- **test_cleanup_container_on_error_none()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_with_container()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_initialize_enhanced_systems()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- *... and 27 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (9 shared connections)
- [Community 130](Community_130.md) (7 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (4 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (3 shared connections)
- [Community 476](Community_476.md) (3 shared connections)
- [Community 413](Community_413.md) (3 shared connections)
- [Community 214](Community_214.md) (3 shared connections)
- [Community 253](Community_253.md) (3 shared connections)
- [Community 454](Community_454.md) (2 shared connections)
- [Community 805](Community_805.md) (1 shared connections)
- [Community 608](Community_608.md) (1 shared connections)
- [Community 322](Community_322.md) (1 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/scripts/test_e2e_player_scripts.py`

## Audit Trail

- EXTRACTED: 147 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*