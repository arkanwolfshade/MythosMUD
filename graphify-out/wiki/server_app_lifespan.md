# server app lifespan

> 44 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (22 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **test_main.py** (15 connections) — `server/tests/unit/test_main.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **asyncio** (6 connections)
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (4 connections)
- **test_cleanup_container_on_error_none()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_with_container()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_initialize_enhanced_systems()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_lifespan_happy_path()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_shutdown_with_error_handling()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_minimal()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **Any** (3 connections)
- **test_calculate_metrics_delta_connection_keys()** (2 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- *... and 19 more nodes in this community*

## Relationships

- [server api monitoring models](server_api_monitoring_models.md) (9 shared connections)
- [server app lifespan protocols nats](server_app_lifespan_protocols_nats.md) (8 shared connections)
- [server monitoring exception tracker](server_monitoring_exception_tracker.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (5 shared connections)
- [server api system monitoring get](server_api_system_monitoring_get.md) (4 shared connections)
- [memorymonitor](memorymonitor.md) (4 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (4 shared connections)
- [server monitoring monitoring dashboard monitoringdashboard](server_monitoring_monitoring_dashboard_monitoringdashboard.md) (3 shared connections)
- [logentry](logentry.md) (3 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (3 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 157 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*