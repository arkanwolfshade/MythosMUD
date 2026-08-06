# aggro threat services

> 135 nodes

## Key Concepts

- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **test_lifespan_startup.py** (39 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_lifespan_helpers.py** (21 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **FastAPI** (13 connections)
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_get_item_prototype_count()** (7 connections) — `server/app/lifespan_startup.py`
- *... and 110 more nodes in this community*

## Relationships

- [nats services service](nats_services_service.md) (21 shared connections)
- [Error Conversion](Error_Conversion.md) (12 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [combat models rationale](combat_models_rationale.md) (7 shared connections)
- [player service game](player_service_game.md) (6 shared connections)
- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [spawn npc services](spawn_npc_services.md) (4 shared connections)
- [commands inventory command](commands_inventory_command.md) (4 shared connections)
- [command base models](command_base_models.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (3 shared connections)
- [room cache services](room_cache_services.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 593 (98%)
- INFERRED: 14 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*