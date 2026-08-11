# UI Player Event Handlers

> 113 nodes

## Key Concepts

- **test_admin_commands.py** (37 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **handle_mute_command()** (20 connections) — `server/commands/admin_mute_commands.py`
- **Any** (16 connections)
- **handle_admin_command()** (14 connections) — `server/commands/admin_commands.py`
- **handle_unmute_command()** (13 connections) — `server/commands/admin_mute_commands.py`
- **handle_add_admin_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **handle_mutes_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **handle_mute_global_command()** (10 connections) — `server/commands/admin_mute_commands.py`
- **handle_unmute_global_command()** (10 connections) — `server/commands/admin_mute_commands.py`
- **_handle_admin_status_command()** (9 connections) — `server/commands/admin_commands.py`
- **_perform_mutes_list()** (7 connections) — `server/commands/admin_mute_commands.py`
- **_handle_admin_time_command()** (6 connections) — `server/commands/admin_commands.py`
- **_perform_mute()** (6 connections) — `server/commands/admin_mute_commands.py`
- **_mute_command_app()** (5 connections) — `server/commands/admin_mute_commands.py`
- **_format_mute_line()** (5 connections) — `server/commands/admin_mute_commands.py`
- **_collect_mute_display_lines()** (5 connections) — `server/commands/admin_mute_commands.py`
- **_extract_mute_target()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_parse_mute_duration_minutes()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_resolve_muter_and_target_players()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_mute_success_result()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_mute_display_target()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_resolve_current_player_id_for_mutes()** (4 connections) — `server/commands/admin_mute_commands.py`
- **.is_admin()** (4 connections) — `server/commands/communication_commands_support.py`
- *... and 88 more nodes in this community*

## Relationships

- [Chat NATS Publisher](Chat_NATS_Publisher.md) (18 shared connections)
- [E2E Suite Overview](E2E_Suite_Overview.md) (15 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (11 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (3 shared connections)
- [Admin Status Commands](Admin_Status_Commands.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (3 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (1 shared connections)
- [Commands System Help](Commands_System_Help.md) (1 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (1 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_admin_commands.py`

## Audit Trail

- EXTRACTED: 367 (85%)
- INFERRED: 65 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*