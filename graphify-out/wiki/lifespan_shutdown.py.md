# lifespan_shutdown.py

> 17 nodes

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
- **Application shutdown logic. This module handles graceful shutdown of all…** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown event bus and clean up all service subscriptions.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Handle graceful shutdown of all services.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown and persist mythos chronicle state.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown NATS message handler if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown connection manager if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown mythos tick scheduler if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown task registry if present.** (1 connections) — `server/app/lifespan_shutdown.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ScheduleService](ScheduleService.md) (1 shared connections)

## Source Files

- `server/app/lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*