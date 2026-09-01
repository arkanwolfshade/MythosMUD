# ApplicationContainer

> 190 nodes

## Key Concepts

- **ApplicationContainer** (161 connections) — `server/container/main.py`
- **lifespan_startup.py** (66 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (43 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_application_container.py** (29 connections) — `server/tests/unit/test_application_container.py`
- **.get_instance()** (23 connections) — `server/container/main.py`
- **get_container()** (21 connections) — `server/container/main.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
- **asyncio** (18 connections)
- **test_application_container_main.py** (18 connections) — `server/tests/unit/container/test_application_container_main.py`
- **FastAPI** (16 connections)
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (15 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (9 connections) — `server/app/lifespan_startup.py`
- **fixtures/unit/__init__.py** (9 connections) — `server/tests/fixtures/unit/__init__.py`
- **_attach_combat_service()** (8 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- *... and 165 more nodes in this community*

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (47 shared connections)
- [EventBus](EventBus.md) (18 shared connections)
- [lifespan.py](lifespan.py.md) (15 shared connections)
- [SpellEffects](SpellEffects.md) (14 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (13 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (9 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [User](User.md) (4 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (4 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/container/__init__.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/services/combat_cleanup_handler.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 572 (96%)
- INFERRED: 25 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*