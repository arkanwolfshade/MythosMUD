# Room Drop Renderer

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

- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (18 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (3 shared connections)
- [Realtime Message Builders](Realtime_Message_Builders.md) (3 shared connections)
- [Persistence Refactoring Complete](Persistence_Refactoring_Complete.md) (3 shared connections)
- [Chat Archive Advanced](Chat_Archive_Advanced.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (1 shared connections)
- [Structured Logging Admin](Structured_Logging_Admin.md) (1 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)
- [Connection Room Presence Utils](Connection_Room_Presence_Utils.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 192 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*