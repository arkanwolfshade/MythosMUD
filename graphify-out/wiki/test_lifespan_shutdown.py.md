# test_lifespan_shutdown.py

> 38 nodes

## Key Concepts

- **test_lifespan_shutdown.py** (26 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **lifespan_shutdown.py** (17 connections) — `server/app/lifespan_shutdown.py`
- **shutdown_services()** (14 connections) — `server/app/lifespan_shutdown.py`
- **asyncio** (14 connections)
- **FastAPI** (9 connections)
- **_shutdown_nats_handler()** (8 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (8 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_connection_manager()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_event_bus()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_chronicle()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_tick_scheduler()** (6 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (5 connections)
- **test_shutdown_connection_manager()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_connection_manager_handles_errors()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_mythos_tick_scheduler()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_nats_handler_from_app_state()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_nats_handler_from_container()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_nats_handler_missing()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_services_orchestrates_all()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **mock_app()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_event_bus()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_event_bus_missing()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_mythos_chronicle_handles_error()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_mythos_chronicle_success()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_task_registry_missing()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- *... and 13 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [MythosChronicle](MythosChronicle.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)

## Source Files

- `server/app/lifespan_shutdown.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 103 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*