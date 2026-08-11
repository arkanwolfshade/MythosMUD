# Room Drop Renderer

> 34 nodes

## Key Concepts

- **admin_shutdown_command.py** (35 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **handle_shutdown_command()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
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

- [Services Lucidity Repository](Services_Lucidity_Repository.md) (12 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [E 2 E Cleanup Troubleshooting](E_2_E_Cleanup_Troubleshooting.md) (3 shared connections)
- [Status Effect Model](Status_Effect_Model.md) (3 shared connections)
- [Commands System Help](Commands_System_Help.md) (3 shared connections)
- [Persistence Refactoring Complete](Persistence_Refactoring_Complete.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (2 shared connections)
- [Chat Archive Advanced](Chat_Archive_Advanced.md) (2 shared connections)
- [Logging Structured Setup](Logging_Structured_Setup.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)
- [E2E Suite Overview](E2E_Suite_Overview.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 160 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*