# Player Position Service

> 113 nodes

## Key Concepts

- **.__init__()** (71 connections) — `server/commands/command_service.py`
- **test_admin_commands.py** (37 connections) — `server/tests/unit/commands/test_admin_commands.py`
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

- [test command factories inventory](test_command_factories_inventory.md) (21 shared connections)
- [test magic commands](test_magic_commands.md) (15 shared connections)
- [DropResolved](DropResolved.md) (10 shared connections)
- [real time](real_time.md) (8 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (6 shared connections)
- [CommandHandler](CommandHandler.md) (5 shared connections)
- [Any](Any.md) (4 shared connections)
- [ContainerData](ContainerData.md) (3 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [test quest service collect](test_quest_service_collect.md) (3 shared connections)
- [.get instance()](get_instance%28%29.md) (3 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_admin_commands.py`

## Audit Trail

- EXTRACTED: 336 (71%)
- INFERRED: 134 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*