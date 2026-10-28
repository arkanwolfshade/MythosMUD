# MagicCommandHandler

> 100 nodes · cohesion 0.03

## Key Concepts

- **test_admin_commands.py** (51 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **asyncio** (39 connections)
- **_resolve_admin_status_player()** (11 connections) — `server/commands/admin_commands.py`
- **_global_mute_request()** (9 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **TestResolveAdminStatusPlayer** (8 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **TestComputeAdminStatus** (7 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **_build_admin_status_message()** (6 connections) — `server/commands/admin_commands.py`
- **test_handle_mute_command_exception()** (5 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_global_command_no_target()** (5 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_global_command_requires_admin()** (5 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_global_command_success()** (5 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_unmute_global_command_not_muted()** (5 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_unmute_global_command_success()** (5 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_add_admin_command_no_target()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_add_admin_command_no_user_manager()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_add_admin_command_success()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_admin_command_hallucinate_dispatches_to_handler()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_admin_command_status()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_admin_command_time()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_admin_command_unknown()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_goto_command_no_app()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_goto_command_no_target()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_command_current_player_not_found()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_command_mute_failure()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_command_no_player_service()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- *... and 75 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (44 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (6 shared connections)
- [look_container.py](look_container.py.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (2 shared connections)
- [ErrorContext](ErrorContext.md) (1 shared connections)
- [security.ts](security.ts.md) (1 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/tests/unit/commands/test_admin_commands.py`

## Audit Trail

- EXTRACTED: 180 (86%)
- INFERRED: 29 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*