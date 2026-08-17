# lifespan_startup.py

> 92 nodes

## Key Concepts

- **lifespan_startup.py** (64 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (41 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **get_mythos_chronicle()** (27 connections) — `server/time/time_service.py`
- **asyncio** (18 connections)
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **_get_item_prototype_count()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **_start_npc_thread_manager_and_pending()** (4 connections) — `server/app/lifespan_startup.py`
- **test_get_item_prototype_count_non_iterable()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_get_item_prototype_entries_async_failure()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 67 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (13 shared connections)
- [lifespan.py](lifespan.py.md) (9 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [.__post_init__](__post_init__.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (4 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [HolidayService](HolidayService.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (3 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 274 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*