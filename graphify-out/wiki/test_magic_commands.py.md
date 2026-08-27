# test_magic_commands.py

> 65 nodes

## Key Concepts

- **test_lifespan_shutdown.py** (27 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **lifespan_protocols.py** (26 connections) — `server/app/lifespan_protocols.py`
- **lifespan_shutdown.py** (22 connections) — `server/app/lifespan_shutdown.py`
- **shutdown_services()** (14 connections) — `server/app/lifespan_shutdown.py`
- **asyncio** (14 connections)
- **_resolve_service()** (10 connections) — `server/app/lifespan_protocols.py`
- **_shutdown_connection_manager()** (9 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_nats_handler()** (9 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (9 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (9 connections)
- **lifespan_connection_manager()** (8 connections) — `server/app/lifespan_protocols.py`
- **_shutdown_event_bus()** (8 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (8 connections)
- **lifespan_event_bus()** (7 connections) — `server/app/lifespan_protocols.py`
- **lifespan_memory_monitor()** (7 connections) — `server/app/lifespan_protocols.py`
- **lifespan_nats_handler()** (7 connections) — `server/app/lifespan_protocols.py`
- **lifespan_task_registry()** (7 connections) — `server/app/lifespan_protocols.py`
- **lifespan_tick_scheduler()** (7 connections) — `server/app/lifespan_protocols.py`
- **_shutdown_mythos_tick_scheduler()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_resolve_container_field()** (6 connections) — `server/app/lifespan_protocols.py`
- **_shutdown_mythos_chronicle()** (6 connections) — `server/app/lifespan_shutdown.py`
- **_container_attr()** (5 connections) — `server/app/lifespan_protocols.py`
- **lifespan_container()** (5 connections) — `server/app/lifespan_protocols.py`
- **FastAPI** (5 connections)
- **_legacy_container_attr()** (4 connections) — `server/app/lifespan_protocols.py`
- *... and 40 more nodes in this community*

## Relationships

- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (8 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [TestHelperFunctions](TestHelperFunctions.md) (3 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [PopulationStats](PopulationStats.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [test_player_event_handlers_utils.py](test_player_event_handlers_utils.py.md) (1 shared connections)
- [NPCEnteredRoom](NPCEnteredRoom.md) (1 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_shutdown.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 179 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*