# lifespan_protocols.py

> 68 nodes

## Key Concepts

- **lifespan_protocols.py** (30 connections) — `server/app/lifespan_protocols.py`
- **test_lifespan_shutdown.py** (26 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **lifespan_shutdown.py** (24 connections) — `server/app/lifespan_shutdown.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
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
- **_shutdown_mythos_chronicle()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_tick_scheduler()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_resolve_container_field()** (6 connections) — `server/app/lifespan_protocols.py`
- **_container_attr()** (5 connections) — `server/app/lifespan_protocols.py`
- **lifespan_container()** (5 connections) — `server/app/lifespan_protocols.py`
- **FastAPI** (5 connections)
- *... and 43 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (12 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (3 shared connections)
- [TaskRegistry](TaskRegistry.md) (3 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (3 shared connections)
- [MythosChronicle](MythosChronicle.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_shutdown.py`
- `server/container/__init__.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 200 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*