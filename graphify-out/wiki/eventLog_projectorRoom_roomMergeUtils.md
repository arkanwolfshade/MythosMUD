# eventLog projectorRoom roomMergeUtils

> 42 nodes

## Key Concepts

- **admin_shutdown_command.py** (35 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **handle_shutdown_command()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **parse_shutdown_parameters()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **validate_shutdown_admin_permission()** (9 connections) — `server/commands/admin_shutdown_command.py`
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
- **Validate that a player has admin permissions for server shutdown.      Args:** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Broadcast shutdown notification to all players.      Args:         connection_ma** (1 connections) — `server/commands/admin_shutdown_command.py`
- *... and 17 more nodes in this community*

## Relationships

- [shutdown admin command](shutdown_admin_command.md) (22 shared connections)
- [realtime real time](realtime_real_time.md) (4 shared connections)
- [shutdown commands sequence](shutdown_commands_sequence.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (2 shared connections)
- [lucidity models rationale](lucidity_models_rationale.md) (2 shared connections)
- [admin structured logging](admin_structured_logging.md) (2 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)
- [logout command commands](logout_command_commands.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 201 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*