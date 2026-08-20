# command_service.py

> 104 nodes

## Key Concepts

- **command_service.py** (108 connections) — `server/commands/command_service.py`
- **asyncio** (30 connections)
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **handle_mute_command()** (18 connections) — `server/commands/admin_mute_commands.py`
- **Any** (16 connections)
- **handle_admin_command()** (13 connections) — `server/commands/admin_commands.py`
- **handle_mutes_command()** (11 connections) — `server/commands/admin_mute_commands.py`
- **handle_unmute_command()** (11 connections) — `server/commands/admin_mute_commands.py`
- **handle_mute_global_command()** (9 connections) — `server/commands/admin_mute_commands.py`
- **handle_unmute_global_command()** (9 connections) — `server/commands/admin_mute_commands.py`
- **_handle_admin_status_command()** (7 connections) — `server/commands/admin_commands.py`
- **_perform_mutes_list()** (7 connections) — `server/commands/admin_mute_commands.py`
- **_handle_admin_time_command()** (6 connections) — `server/commands/admin_commands.py`
- **_perform_mute()** (6 connections) — `server/commands/admin_mute_commands.py`
- **_collect_mute_display_lines()** (5 connections) — `server/commands/admin_mute_commands.py`
- **_format_mute_line()** (5 connections) — `server/commands/admin_mute_commands.py`
- **_mute_command_app()** (5 connections) — `server/commands/admin_mute_commands.py`
- **_extract_mute_target()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_mute_display_target()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_mute_success_result()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_parse_mute_duration_minutes()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_resolve_current_player_id_for_mutes()** (4 connections) — `server/commands/admin_mute_commands.py`
- **_resolve_muter_and_target_players()** (4 connections) — `server/commands/admin_mute_commands.py`
- **.is_admin()** (4 connections) — `server/commands/communication_commands_support.py`
- **test_handle_add_admin_command_no_target()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- *... and 79 more nodes in this community*

## Relationships

- [get_username_from_user](get_username_from_user.md) (38 shared connections)
- [get_logger](get_logger.md) (23 shared connections)
- [AliasStorage](AliasStorage.md) (10 shared connections)
- [request_with_app_container](request_with_app_container.md) (8 shared connections)
- [test_admin_teleport_commands.py](test_admin_teleport_commands.py.md) (6 shared connections)
- [ValidationError](ValidationError.md) (6 shared connections)
- [server/commands/__init__.py](server-commands-__init__.py.md) (6 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (6 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (6 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (4 shared connections)
- [combat_loader.py](combat_loader.py.md) (4 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (4 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_admin_commands.py`

## Audit Trail

- EXTRACTED: 245 (74%)
- INFERRED: 86 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*