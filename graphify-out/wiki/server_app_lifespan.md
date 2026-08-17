# server app lifespan

> 38 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (22 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **asyncio** (6 connections)
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
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
- *... and 13 more nodes in this community*

## Relationships

- [server api monitoring models](server_api_monitoring_models.md) (8 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (4 shared connections)
- [characterinfo](characterinfo.md) (4 shared connections)
- [server monitoring init getattr](server_monitoring_init_getattr.md) (3 shared connections)
- [docs examples logging websocket integration](docs_examples_logging_websocket_integration.md) (3 shared connections)
- [logentry](logentry.md) (3 shared connections)
- [scripts generate openapi spec](scripts_generate_openapi_spec.md) (3 shared connections)
- [server monitoring memory leak metrics](server_monitoring_memory_leak_metrics.md) (3 shared connections)
- [holidayresolver](holidayresolver.md) (3 shared connections)
- [server app lifespan shutdown](server_app_lifespan_shutdown.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`

## Audit Trail

- EXTRACTED: 133 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*