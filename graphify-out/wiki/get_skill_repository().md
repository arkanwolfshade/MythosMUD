# get skill repository()

> 40 nodes

## Key Concepts

- **admin_shutdown_command.py** (35 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **handle_shutdown_command()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **parse_shutdown_parameters()** (11 connections) — `server/commands/admin_shutdown_command.py`
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
- *... and 15 more nodes in this community*

## Relationships

- [Any](Any.md) (17 shared connections)
- [test npc combat integration service](test_npc_combat_integration_service.md) (4 shared connections)
- [test format player location invalid()](test_format_player_location_invalid%28%29.md) (3 shared connections)
- [Schedule a best effort graceful](Schedule_a_best_effort_graceful.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [test magic commands](test_magic_commands.md) (2 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (2 shared connections)
- [get item description from prototype()](get_item_description_from_prototype%28%29.md) (2 shared connections)
- [DropResolved](DropResolved.md) (2 shared connections)
- [AuthSlice](AuthSlice.md) (1 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (1 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 192 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*