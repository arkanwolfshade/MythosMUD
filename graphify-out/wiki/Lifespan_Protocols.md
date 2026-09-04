# Lifespan Protocols

> 66 nodes

## Key Concepts

- **lifespan_protocols.py** (30 connections) — `server/app/lifespan_protocols.py`
- **test_lifespan_shutdown.py** (27 connections) — `server/tests/unit/app/test_lifespan_shutdown.py`
- **lifespan_shutdown.py** (24 connections) — `server/app/lifespan_shutdown.py`
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
- **_legacy_container_attr()** (4 connections) — `server/app/lifespan_protocols.py`
- *... and 41 more nodes in this community*

## Relationships

- [Application Container Bundles](Application_Container_Bundles.md) (11 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (6 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (5 shared connections)
- [Time Service](Time_Service.md) (4 shared connections)
- [Task Registry](Task_Registry.md) (3 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (2 shared connections)
- [Nats Message Handler Broadcast](Nats_Message_Handler_Broadcast.md) (2 shared connections)
- [Test Game Tick Death](Test_Game_Tick_Death.md) (2 shared connections)
- [Connection Manager](Connection_Manager.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_shutdown.py`
- `server/tests/unit/app/test_lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 185 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*