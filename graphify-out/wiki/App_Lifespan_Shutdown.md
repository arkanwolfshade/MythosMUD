# App Lifespan Shutdown

> 18 nodes · cohesion 0.19

## Key Concepts

- **lifespan_shutdown.py** (15 connections) — `server/app/lifespan_shutdown.py`
- **shutdown_services()** (12 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (5 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_connection_manager()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_event_bus()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_chronicle()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_tick_scheduler()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_nats_handler()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (4 connections) — `server/app/lifespan_shutdown.py`
- **ApplicationContainer** (3 connections) — `server/app/lifespan_shutdown.py`
- **Application shutdown logic.  This module handles graceful shutdown of all servic** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown event bus and clean up all service subscriptions.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Handle graceful shutdown of all services.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown and persist mythos chronicle state.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown NATS message handler if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown connection manager if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown mythos tick scheduler if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown task registry if present.** (1 connections) — `server/app/lifespan_shutdown.py`

## Relationships

- [[App Lifespan Management]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Game Tick Processing]] (2 shared connections)
- [[Application DI Bundles]] (1 shared connections)

## Source Files

- `server/app/lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
