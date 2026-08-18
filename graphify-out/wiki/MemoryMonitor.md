# memorymonitor

> 62 nodes

## Key Concepts

- **lifespan_protocols.py** (30 connections) — `server/app/lifespan_protocols.py`
- **test_lifespan_shutdown.py** (27 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **lifespan_shutdown.py** (24 connections) — `server/app/lifespan_shutdown.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
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
- *... and 37 more nodes in this community*

## Relationships

- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (11 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server app lifespan](server_app_lifespan.md) (4 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (3 shared connections)
- [server app task registry](server_app_task_registry.md) (3 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (3 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [server tests unit time test](server_tests_unit_time_test.md) (2 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (2 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (2 shared connections)
- [server realtime memory monitor memorymonitor](server_realtime_memory_monitor_memorymonitor.md) (1 shared connections)
- [server app lifespan protocols nats](server_app_lifespan_protocols_nats.md) (1 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_shutdown.py`
- `server/container/__init__.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 195 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*