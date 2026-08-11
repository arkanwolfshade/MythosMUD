# Invite and User Schemas

> 70 nodes

## Key Concepts

- **test_admin_commands.py** (37 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **handle_admin_command()** (14 connections) — `server/commands/admin_commands.py`
- **_handle_admin_status_command()** (9 connections) — `server/commands/admin_commands.py`
- **_handle_admin_time_command()** (6 connections) — `server/commands/admin_commands.py`
- **.is_admin()** (4 connections) — `server/commands/communication_commands_support.py`
- **test_handle_mute_command_exception()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **Any** (3 connections)
- **test_handle_admin_command_status()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_admin_command_time()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_admin_command_unknown()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_command_no_user_manager()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_command_no_target()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_unmute_command_no_user_manager()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_unmute_command_no_target()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_unmute_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_unmute_command_idempotent_when_not_muted()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_global_command_no_user_manager()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mute_global_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_unmute_global_command_no_user_manager()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_unmute_global_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_add_admin_command_no_user_manager()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_add_admin_command_no_target()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_add_admin_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_mutes_command_no_user_manager()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- *... and 45 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (32 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (9 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Admin Status Commands](Admin_Status_Commands.md) (1 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (1 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (1 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (1 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (1 shared connections)
- [Look NPC Command](Look_NPC_Command.md) (1 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_admin_commands.py`

## Audit Trail

- EXTRACTED: 168 (85%)
- INFERRED: 30 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*