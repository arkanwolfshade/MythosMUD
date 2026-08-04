# eventLog projectorRoom roomMergeUtils

> 34 nodes

## Key Concepts

- **admin_shutdown_command.py** (35 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **handle_shutdown_command()** (13 connections) — `server/commands/admin_shutdown_command.py`
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
- **Cancel existing shutdown task if present.      Args:         app: FastAPI applic** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Set shutdown pending flag in container and app.state.      Args:         app: Fa** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Create countdown task from coroutine, handling task registry if available.** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Store shutdown data in container and app.state.      Args:         app: FastAPI** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Clear shutdown state in container and app.state.      Args:         app: FastAPI** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Main countdown loop that sends notifications and executes shutdown.      Args:** (1 connections) — `server/commands/admin_shutdown_command.py`
- *... and 9 more nodes in this community*

## Relationships

- [shutdown admin command](shutdown_admin_command.md) (13 shared connections)
- [commands whisper command](commands_whisper_command.md) (5 shared connections)
- [motd loader rationale](motd_loader_rationale.md) (3 shared connections)
- [services service hallucination](services_service_hallucination.md) (3 shared connections)
- [occupant realtime formatter](occupant_realtime_formatter.md) (3 shared connections)
- [shutdown commands sequence](shutdown_commands_sequence.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [lucidity models rationale](lucidity_models_rationale.md) (2 shared connections)
- [admin structured logging](admin_structured_logging.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (2 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 160 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*