# command base models

> 36 nodes

## Key Concepts

- **test_lifespan_shutdown.py** (26 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **lifespan_shutdown.py** (16 connections) — `server/app/lifespan_shutdown.py`
- **shutdown_services()** (14 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (9 connections)
- **_shutdown_nats_handler()** (8 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (8 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_chronicle()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_connection_manager()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_event_bus()** (7 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_tick_scheduler()** (6 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (5 connections)
- **test_shutdown_nats_handler_from_container()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_nats_handler_from_app_state()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_nats_handler_missing()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_connection_manager()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_connection_manager_handles_errors()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_mythos_tick_scheduler()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_services_orchestrates_all()** (3 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **mock_app()** (2 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_mythos_chronicle_success()** (2 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_mythos_chronicle_handles_error()** (2 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_task_registry_success()** (2 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_task_registry_timeout()** (2 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_task_registry_missing()** (2 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **test_shutdown_event_bus()** (2 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- *... and 11 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (1 shared connections)

## Source Files

- `server/app/lifespan_shutdown.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 160 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*