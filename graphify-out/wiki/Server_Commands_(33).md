# Server Commands (33)

> 38 nodes

## Key Concepts

- **admin_shutdown_command.py** (35 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **handle_shutdown_command()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **broadcast_shutdown_notification()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **countdown_loop()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **_create_countdown_task()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_store_shutdown_data()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_clear_shutdown_state()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_validate_shutdown_context()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_cancel()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_initiate()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_existing_shutdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_set_shutdown_pending_flag()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_state()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_countdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_broadcast_shutdown_cancellation()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_services()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **Task** (2 connections)
- **Admin shutdown command for MythosMUD.  This module provides the /shutdown comman** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Broadcast shutdown notification to all players.      Args:         connection_ma** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Cancel existing shutdown task if present.      Args:         app: FastAPI applic** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Set shutdown pending flag in container and app.state.      Args:         app: Fa** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Create countdown task from coroutine, handling task registry if available.** (1 connections) — `server/commands/admin_shutdown_command.py`
- *... and 13 more nodes in this community*

## Relationships

- [Server Commands (21)](Server_Commands_%2821%29.md) (16 shared connections)
- [Server Commands](Server_Commands.md) (13 shared connections)
- [Server Api (4)](Server_Api_%284%29.md) (3 shared connections)
- [Server Commands (66)](Server_Commands_%2866%29.md) (3 shared connections)
- [Server Commands (54)](Server_Commands_%2854%29.md) (3 shared connections)
- [Server Structured Logging (10)](Server_Structured_Logging_%2810%29.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 180 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*