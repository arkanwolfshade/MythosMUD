# lifespan_startup.py

> 102 nodes

## Key Concepts

- **lifespan_startup.py** (60 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (39 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_get_item_prototype_count()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- *... and 77 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (16 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [lifespan.py](lifespan.py.md) (11 shared connections)
- [CombatService](CombatService.md) (10 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (8 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [.__post_init__](__post_init__.md) (4 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (3 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_startup.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 281 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*