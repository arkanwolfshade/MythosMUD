# test_lifespan_shutdown.py

> 73 nodes

## Key Concepts

- **test_lifespan_shutdown.py** (31 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **lifespan_protocols.py** (30 connections) — `server/app/lifespan_protocols.py`
- **lifespan_shutdown.py** (27 connections) — `server/app/lifespan_shutdown.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **asyncio** (16 connections)
- **shutdown_services()** (15 connections) — `server/app/lifespan_shutdown.py`
- **_resolve_service()** (10 connections) — `server/app/lifespan_protocols.py`
- **_shutdown_connection_manager()** (9 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_nats_handler()** (9 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (9 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (9 connections)
- **lifespan_connection_manager()** (8 connections) — `server/app/lifespan_protocols.py`
- **lifespan_task_registry()** (8 connections) — `server/app/lifespan_protocols.py`
- **_shutdown_event_bus()** (8 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (8 connections)
- **lifespan_event_bus()** (7 connections) — `server/app/lifespan_protocols.py`
- **lifespan_memory_monitor()** (7 connections) — `server/app/lifespan_protocols.py`
- **lifespan_nats_handler()** (7 connections) — `server/app/lifespan_protocols.py`
- **lifespan_tick_scheduler()** (7 connections) — `server/app/lifespan_protocols.py`
- **_flush_live_instances()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_chronicle()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_tick_scheduler()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_resolve_container_field()** (6 connections) — `server/app/lifespan_protocols.py`
- **_container_attr()** (5 connections) — `server/app/lifespan_protocols.py`
- **lifespan_container()** (5 connections) — `server/app/lifespan_protocols.py`
- *... and 48 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (12 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (6 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (4 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (3 shared connections)
- [TaskRegistry](TaskRegistry.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (2 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (2 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_shutdown.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 224 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*