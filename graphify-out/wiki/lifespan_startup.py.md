# lifespan_startup.py

> 80 nodes

## Key Concepts

- **lifespan_startup.py** (60 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **asyncio** (12 connections)
- **initialize_combat_services()** (11 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **subscribe_quest_events()** (8 connections) — `server/app/lifespan_event_subscriptions.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **subscribe_room_occupants_refresh()** (6 connections) — `server/app/lifespan_event_subscriptions.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (5 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (4 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (4 connections) — `server/app/lifespan_startup.py`
- **_start_npc_thread_manager_and_pending()** (4 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (4 connections) — `server/app/lifespan_startup.py`
- *... and 55 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (15 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (14 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (7 shared connections)
- [ScheduleService](ScheduleService.md) (4 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (3 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [magic_service.py](magic_service.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 362 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*