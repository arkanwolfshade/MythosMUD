# lifespan_startup.py

> 100 nodes

## Key Concepts

- **lifespan_startup.py** (66 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (43 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **FastAPI** (16 connections)
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (15 connections)
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
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
- **_log_npc_startup_errors()** (5 connections) — `server/app/lifespan_startup.py`
- **_start_nats_message_handler()** (5 connections) — `server/app/lifespan_startup.py`
- **mock_app()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 75 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (16 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (10 shared connections)
- [lifespan.py](lifespan.py.md) (10 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)
- [test_npc_service.py](test_npc_service.py.md) (3 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (3 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (3 shared connections)
- [time_event_consumer.py](time_event_consumer.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/services/npc_service/__init__.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 287 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*