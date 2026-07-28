# App Lifespan Shutdown

> 17 nodes · cohesion 0.19

## Key Concepts

- **lifespan_shutdown.py** (15 connections) — `server/app/lifespan_shutdown.py`
- **shutdown_services()** (12 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (5 connections)
- **_shutdown_connection_manager()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_event_bus()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_chronicle()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_tick_scheduler()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_nats_handler()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (4 connections) — `server/app/lifespan_shutdown.py`
- **Application shutdown logic.  This module handles graceful shutdown of all servic** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown event bus and clean up all service subscriptions.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Handle graceful shutdown of all services.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown and persist mythos chronicle state.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown NATS message handler if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown connection manager if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown mythos tick scheduler if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown task registry if present.** (1 connections) — `server/app/lifespan_shutdown.py`

## Relationships

- [Application DI Bundles](Application_DI_Bundles.md) (4 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (2 shared connections)

## Source Files

- `server/app/lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*