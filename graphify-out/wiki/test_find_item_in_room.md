# test find item in room

> 17 nodes

## Key Concepts

- **lifespan_shutdown.py** (15 connections) — `server/app/lifespan_shutdown.py`
- **shutdown_services()** (12 connections) — `server/app/lifespan_shutdown.py`
- **FastAPI** (5 connections)
- **_shutdown_mythos_chronicle()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_nats_handler()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_connection_manager()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_mythos_tick_scheduler()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_task_registry()** (4 connections) — `server/app/lifespan_shutdown.py`
- **_shutdown_event_bus()** (4 connections) — `server/app/lifespan_shutdown.py`
- **Application shutdown logic.  This module handles graceful shutdown of all servic** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown and persist mythos chronicle state.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown NATS message handler if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown connection manager if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown mythos tick scheduler if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown task registry if present.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Shutdown event bus and clean up all service subscriptions.** (1 connections) — `server/app/lifespan_shutdown.py`
- **Handle graceful shutdown of all services.** (1 connections) — `server/app/lifespan_shutdown.py`

## Relationships

- [test command parser](test_command_parser.md) (4 shared connections)
- [.shutdown()](shutdown%28%29.md) (3 shared connections)
- [get health status()](get_health_status%28%29.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)

## Source Files

- `server/app/lifespan_shutdown.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*