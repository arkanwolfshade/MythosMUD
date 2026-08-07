# realtime game state

> 49 nodes

## Key Concepts

- **test_admin_teleport_commands.py** (36 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **handle_teleport_command()** (31 connections) — `server/commands/admin_teleport_commands.py`
- **handle_goto_command()** (21 connections) — `server/commands/admin_teleport_commands.py`
- **_request_with_services()** (17 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **handle_confirm_teleport_command()** (16 connections) — `server/commands/admin_teleport_commands.py`
- **handle_confirm_goto_command()** (16 connections) — `server/commands/admin_teleport_commands.py`
- **Any** (4 connections)
- **test_handle_teleport_command_no_app()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_teleport_command_no_target()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_goto_command_no_app()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_goto_command_no_target()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_goto_missing_target()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_goto_context_error()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_goto_same_room()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_goto_success()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_goto_exception_logs_failure()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_goto_missing_target()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_goto_success()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_goto_same_room()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_goto_exception()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_goto_resolve_target_error()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_teleport_context_error()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_teleport_missing_target()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_teleport_same_room()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- **test_handle_confirm_teleport_success()** (3 connections) — `server/tests/unit/commands/test_admin_teleport_commands.py`
- *... and 24 more nodes in this community*

## Relationships

- [npc service services](npc_service_services.md) (15 shared connections)
- [commands admin mute](commands_admin_mute.md) (8 shared connections)
- [npc rewards combat](npc_rewards_combat.md) (7 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (4 shared connections)
- [admin structured logging](admin_structured_logging.md) (3 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [security sessionManager SessionManager](security_sessionManager_SessionManager.md) (1 shared connections)

## Source Files

- `server/commands/admin_teleport_commands.py`
- `server/tests/unit/commands/test_admin_commands.py`
- `server/tests/unit/commands/test_admin_teleport_commands.py`

## Audit Trail

- EXTRACTED: 232 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*