# Lifespan Startup Hooks

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

- [Distributed Event Bus](Distributed_Event_Bus.md) (22 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (10 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (6 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (4 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (3 shared connections)
- [Command Factory Creators](Command_Factory_Creators.md) (1 shared connections)
- [Community 2205](Community_2205.md) (1 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)

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