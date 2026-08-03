# message broadcaster realtime

> 35 nodes

## Key Concepts

- **test_lifespan_helpers.py** (21 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **FastAPI** (4 connections)
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- **Any** (3 connections)
- **.test_lifespan_initialization_failure()** (3 connections) — `server/tests/unit/test_main.py`
- **test_calculate_metrics_delta_no_startup()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_calculate_metrics_delta_connection_keys()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_metrics_to_file_writes_json()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_mythos_state_on_error_handles_failure()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_with_container()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_none()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_initialize_enhanced_systems()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_minimal()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_shutdown_with_error_handling()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_mythos_state_on_error_success()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_lifespan_happy_path()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **Calculate metrics delta between startup and shutdown.** (1 connections) — `server/app/lifespan.py`
- *... and 10 more nodes in this community*

## Relationships

- [Magic Spell Service](Magic_Spell_Service.md) (13 shared connections)
- [System Metrics](System_Metrics.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [player service game](player_service_game.md) (2 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (1 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (1 shared connections)
- [log structured logging](log_structured_logging.md) (1 shared connections)
- [command base models](command_base_models.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [player death service](player_death_service.md) (1 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (1 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 135 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*