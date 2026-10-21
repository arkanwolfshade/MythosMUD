# NPCThreadManager

> 71 nodes · cohesion 0.06

## Key Concepts

- **test_lifespan_shutdown.py** (31 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **lifespan_protocols.py** (30 connections) — `server/app/lifespan_protocols.py`
- **lifespan_shutdown.py** (27 connections) — `server/app/lifespan_shutdown.py`
- **asyncio** (16 connections)
- **shutdown_services()** (15 connections) — `server/app/lifespan_shutdown.py`
- **_resolve_service()** (10 connections) — `server/app/lifespan_protocols.py`
- **_shutdown_connection_manager()** (9 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_nats_handler()** (9 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (9 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (9 connections)
- **lifespan_connection_manager()** (8 connections) — `server/app/lifespan_protocols.py`
- **lifespan_task_registry()** (8 connections) — `server/app/lifespan_protocols.py`
- **FastAPI** (8 connections)
- **_shutdown_event_bus()** (8 connections) — `server/app/lifespan_shutdown.py`
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
- **FastAPI** (5 connections)
- *... and 46 more nodes in this community*

## Relationships

- [test_message_handlers.py](test_message_handlers.py.md) (12 shared connections)
- [Room](Room.md) (4 shared connections)
- [command_error](command_error.md) (3 shared connections)
- [EventHandler](EventHandler.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (2 shared connections)
- [deque](deque.md) (2 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_shutdown.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 200 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*