# player_event_handlers.py

> 66 nodes · cohesion 0.09

## Key Concepts

- **test_admin_teleport_commands.py** (42 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **patch** (32 connections)
- **admin_confirm_teleport_commands.py** (28 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **asyncio** (28 connections)
- **handle_teleport_command()** (25 connections) — `server/commands/admin_teleport_commands.py`
- **handle_goto_command()** (21 connections) — `server/commands/admin_teleport_commands.py`
- **handle_confirm_goto_command()** (17 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **handle_confirm_teleport_command()** (17 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **_request_with_services()** (17 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **log_failed_admin_move()** (13 connections) — `server/commands/admin_teleport_utils.py`
- **Any** (8 connections)
- **_execute_confirm_goto_move()** (7 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **_execute_confirm_teleport_move()** (7 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **_resolve_connection_manager()** (7 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **_resolve_confirm_goto_target()** (6 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **_resolve_confirm_teleport_targets()** (6 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **test_handle_confirm_goto_exception()** (6 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_teleport_exception()** (6 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_goto_exception_logs_failure()** (6 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **_resolve_request_app_service()** (5 connections) — `server/commands/admin_confirm_teleport_commands.py`
- **test_handle_confirm_goto_context_error()** (5 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_goto_missing_target()** (5 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_goto_same_room()** (5 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_goto_success()** (5 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_teleport_context_error()** (5 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- *... and 41 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (21 shared connections)
- [ErrorContext](ErrorContext.md) (20 shared connections)
- [Async Code Review - Post Phase 2 Migration](Async_Code_Review_-_Post_Phase_2_Migration.md) (11 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (8 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (6 shared connections)
- [Room](Room.md) (2 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_shopkeeper_npc.py](test_shopkeeper_npc.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_confirm_teleport_commands.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/tests/unit/commands/test_admin_teleport_commands.py`

## Audit Trail

- EXTRACTED: 252 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*