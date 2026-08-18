# lifespan_protocols.py

> 74 nodes

## Key Concepts

- **lifespan_protocols.py** (30 connections) — `server/app/lifespan_protocols.py`
- **test_lifespan_shutdown.py** (27 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **lifespan_shutdown.py** (24 connections) — `server/app/lifespan_shutdown.py`
- **shutdown_services()** (14 connections) — `server/app/lifespan_shutdown.py`
- **asyncio** (14 connections)
- **_resolve_service()** (10 connections) — `server/app/lifespan_protocols.py`
- **_shutdown_connection_manager()** (9 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_nats_handler()** (9 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (9 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (9 connections)
- **_shutdown_event_bus()** (8 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (8 connections)
- **lifespan_connection_manager()** (7 connections) — `server/app/lifespan_protocols.py`
- **_shutdown_mythos_chronicle()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_tick_scheduler()** (7 connections) — `server/app/lifespan_shutdown.py`
- **lifespan_event_bus()** (6 connections) — `server/app/lifespan_protocols.py`
- **lifespan_memory_monitor()** (6 connections) — `server/app/lifespan_protocols.py`
- **lifespan_nats_handler()** (6 connections) — `server/app/lifespan_protocols.py`
- **lifespan_task_registry()** (6 connections) — `server/app/lifespan_protocols.py`
- **lifespan_tick_scheduler()** (6 connections) — `server/app/lifespan_protocols.py`
- **_resolve_container_field()** (6 connections) — `server/app/lifespan_protocols.py`
- **_container_attr()** (5 connections) — `server/app/lifespan_protocols.py`
- **lifespan_container()** (5 connections) — `server/app/lifespan_protocols.py`
- **FastAPI** (5 connections)
- *... and 49 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (11 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [TaskRegistry](TaskRegistry.md) (3 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (3 shared connections)
- [MythosChronicle](MythosChronicle.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (2 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (1 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_shutdown.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 205 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*