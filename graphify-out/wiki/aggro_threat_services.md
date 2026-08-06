# aggro threat services

> 63 nodes

## Key Concepts

- **test_lifespan_helpers.py** (21 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **FastAPI** (4 connections)
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- **Any** (3 connections)
- **test_initialize_container_and_legacy_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_no_item_factory()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_async_registry()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_setup_connection_manager()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_setup_connection_manager_no_manager()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_npc_startup_spawning()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 38 more nodes in this community*

## Relationships

- [Magic Spell Service](Magic_Spell_Service.md) (21 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (13 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (10 shared connections)
- [nats services service](nats_services_service.md) (9 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (2 shared connections)
- [player room event](player_room_event.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [effect player repository](effect_player_repository.md) (1 shared connections)
- [command base models](command_base_models.md) (1 shared connections)
- [feature services flag](feature_services_flag.md) (1 shared connections)
- [playerHandlers eventHandlers healthEvent](playerHandlers_eventHandlers_healthEvent.md) (1 shared connections)
- [player service game](player_service_game.md) (1 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 233 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*