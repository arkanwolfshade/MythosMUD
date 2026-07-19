# Admin Shutdown Commands

> 39 nodes · cohesion 0.10

## Key Concepts

- **admin_shutdown_command.py** (34 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections) — `server/commands/admin_shutdown_command.py`
- **handle_shutdown_command()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **broadcast_shutdown_notification()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **countdown_loop()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **_create_countdown_task()** (6 connections) — `server/commands/admin_shutdown_command.py`
- **_validate_shutdown_context()** (6 connections) — `server/commands/admin_shutdown_command.py`
- **_clear_shutdown_state()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_cancel()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_initiate()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_store_shutdown_data()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_broadcast_shutdown_cancellation()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_countdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_existing_shutdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_services()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_state()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_set_shutdown_pending_flag()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **Task** (2 connections) — `server/commands/admin_shutdown_command.py`
- **Admin shutdown command for MythosMUD.  This module provides the /shutdown comman** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Broadcast shutdown notification to all players.      Args:         connection_ma** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Cancel existing shutdown task if present.      Args:         app: FastAPI applic** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Set shutdown pending flag in container and app.state.      Args:         app: Fa** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Create countdown task from coroutine, handling task registry if available.** (1 connections) — `server/commands/admin_shutdown_command.py`
- *... and 14 more nodes in this community*

## Relationships

- [[Admin Shutdown Command]] (18 shared connections)
- [[Alias Expansion Logic]] (6 shared connections)
- [[Commands Admin Shutdown]] (4 shared connections)
- [[Server Process Termination]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Database Manager Tests]] (2 shared connections)
- [[Character Creation API]] (1 shared connections)
- [[Structured Logging Admin]] (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 180 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
