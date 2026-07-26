# test_lifespan_startup.py

> 56 nodes · cohesion 0.05

## Key Concepts

- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (5 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (4 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (4 connections) — `server/app/lifespan_startup.py`
- **Any** (4 connections)
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_initialize_chat_service()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_combat_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_async_registry()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_no_item_factory()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_magic_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_mythos_time_consumer()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_nats_and_combat_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_npc_services()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_npc_startup_spawning()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 31 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (22 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (10 shared connections)
- [lifespan.py](lifespan.py.md) (6 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [SpellRegistry](SpellRegistry.md) (3 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (1 shared connections)
- [dependencies.py](dependencies.py.md) (1 shared connections)
- [__init__.py](__init__.py.md) (1 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/container/main.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 192 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*