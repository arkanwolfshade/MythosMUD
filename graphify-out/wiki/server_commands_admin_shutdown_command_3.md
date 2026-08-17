# server commands admin shutdown command

> 38 nodes

## Key Concepts

- **admin_shutdown_command.py** (36 connections) — `server/commands/admin_shutdown_command.py`
- **Any** (20 connections)
- **handle_shutdown_command()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **initiate_shutdown_countdown()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **cancel_shutdown_countdown()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **broadcast_shutdown_notification()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **countdown_loop()** (7 connections) — `server/commands/admin_shutdown_command.py`
- **_clear_shutdown_state()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_create_countdown_task()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_cancel()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_handle_shutdown_initiate()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_store_shutdown_data()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_validate_shutdown_context()** (5 connections) — `server/commands/admin_shutdown_command.py`
- **_broadcast_shutdown_cancellation()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_countdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_cancel_existing_shutdown_task()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_services()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_get_shutdown_state()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **_set_shutdown_pending_flag()** (4 connections) — `server/commands/admin_shutdown_command.py`
- **Task** (2 connections)
- **Admin shutdown command for MythosMUD. This module provides the /shutdown…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Broadcast shutdown notification to all players. Args: connection_manager:…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Cancel existing shutdown task if present. Args: app: FastAPI application…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Set shutdown pending flag in container and app.state. Args: app: FastAPI…** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Create countdown task from coroutine, handling task registry if available.…** (1 connections) — `server/commands/admin_shutdown_command.py`
- *... and 13 more nodes in this community*

## Relationships

- [server commands admin shutdown command](server_commands_admin_shutdown_command.md) (17 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [asyncio mark](asyncio_mark.md) (3 shared connections)
- [server commands shutdown process termination](server_commands_shutdown_process_termination.md) (3 shared connections)
- [server commands alias commands](server_commands_alias_commands.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (2 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (2 shared connections)
- [server structured logging admin actions](server_structured_logging_admin_actions.md) (2 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)
- [server api character creation](server_api_character_creation.md) (1 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 109 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*