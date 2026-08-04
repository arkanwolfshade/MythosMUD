# Magic Spell Service

> 82 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (21 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **conftest.py** (6 connections) — `server/tests/unit/auth/conftest.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **test_read_token_accepts_matching_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **FastAPI** (4 connections)
- **test_read_token_rejects_wrong_epoch()** (4 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- *... and 57 more nodes in this community*

## Relationships

- [player death service](player_death_service.md) (12 shared connections)
- [Error Conversion](Error_Conversion.md) (7 shared connections)
- [command combat models](command_combat_models.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (7 shared connections)
- [auth users rationale](auth_users_rationale.md) (7 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (6 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (5 shared connections)
- [time service rationale](time_service_rationale.md) (4 shared connections)
- [command base models](command_base_models.md) (3 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (3 shared connections)
- [room cache services](room_cache_services.md) (3 shared connections)
- [log structured logging](log_structured_logging.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 345 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*