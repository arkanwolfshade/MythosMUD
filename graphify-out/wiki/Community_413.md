# Community 413

> 42 nodes

## Key Concepts

- **test_lifespan_shutdown.py** (31 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **lifespan_shutdown.py** (19 connections) — `server/app/lifespan_shutdown.py`
- **asyncio** (16 connections)
- **shutdown_services()** (15 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (9 connections)
- **_shutdown_nats_handler()** (8 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (8 connections) — `server/app/lifespan_shutdown.py`
- **_flush_live_instances()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_connection_manager()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_event_bus()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_chronicle()** (6 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_tick_scheduler()** (6 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (5 connections)
- **test_flush_live_instances_tolerates_missing_service_and_errors()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_connection_manager()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_connection_manager_handles_errors()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_mythos_tick_scheduler()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_nats_handler_from_app_state()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_nats_handler_from_container()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_nats_handler_missing()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_services_orchestrates_all()** (4 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **mock_app()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_flush_live_instances_flushes_all()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_event_bus()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_event_bus_missing()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- *... and 17 more nodes in this community*

## Relationships

- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (5 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (4 shared connections)
- [Community 317](Community_317.md) (3 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)
- [Community 92](Community_92.md) (1 shared connections)
- [Community 563](Community_563.md) (1 shared connections)

## Source Files

- `server/app/lifespan_shutdown.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 116 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*