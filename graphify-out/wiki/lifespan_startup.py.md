# lifespan_startup.py

> 103 nodes

## Key Concepts

- **lifespan_startup.py** (65 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (42 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **FastAPI** (16 connections)
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (15 connections)
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (9 connections) — `server/app/lifespan_startup.py`
- **_attach_combat_service()** (8 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (6 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **test_setup_connection_manager()** (6 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **nats_is_connected()** (5 connections) — `server/app/lifespan_protocols.py`
- **_ensure_room_cache_before_npc_startup()** (5 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (5 connections) — `server/app/lifespan_startup.py`
- *... and 78 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (20 shared connections)
- [event_types.py](event_types.py.md) (10 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [lifespan.py](lifespan.py.md) (7 shared connections)
- [npc_database.py](npc_database.py.md) (4 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (4 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (3 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/container/bundles/npc.py`
- `server/services/npc_service/__init__.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 294 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*