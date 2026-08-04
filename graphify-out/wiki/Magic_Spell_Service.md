# Magic Spell Service

> 132 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_startup.py** (39 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_lifespan_helpers.py** (21 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_get_item_prototype_count()** (7 connections) — `server/app/lifespan_startup.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **_log_npc_startup_errors()** (6 connections) — `server/app/lifespan_startup.py`
- **conftest.py** (6 connections) — `server/tests/unit/auth/conftest.py`
- *... and 107 more nodes in this community*

## Relationships

- [nats services service](nats_services_service.md) (38 shared connections)
- [player requests schemas](player_requests_schemas.md) (9 shared connections)
- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [System Metrics](System_Metrics.md) (5 shared connections)
- [command combat models](command_combat_models.md) (4 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (3 shared connections)
- [command base models](command_base_models.md) (3 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (3 shared connections)
- [room cache services](room_cache_services.md) (3 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (3 shared connections)
- [Spell Validation](Spell_Validation.md) (3 shared connections)
- [log structured logging](log_structured_logging.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 505 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*