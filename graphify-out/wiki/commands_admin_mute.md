# commands admin mute

> 105 nodes

## Key Concepts

- **test_admin_commands.py** (37 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **handle_mute_command()** (19 connections) — `server/commands/admin_mute_commands.py`
- **Any** (16 connections)
- **handle_unmute_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **handle_add_admin_command()** (11 connections) — `server/commands/admin_mute_commands.py`
- **handle_mutes_command()** (11 connections) — `server/commands/admin_mute_commands.py`
- **handle_mute_global_command()** (9 connections) — `server/commands/admin_mute_commands.py`
- **handle_unmute_global_command()** (9 connections) — `server/commands/admin_mute_commands.py`
- **_perform_mutes_list()** (7 connections) — `server/commands/admin_mute_commands.py`
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
- **test_handle_mute_command_exception()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **_mute_duration_display()** (3 connections) — `server/commands/admin_mute_commands.py`
- **_mutes_list_result()** (3 connections) — `server/commands/admin_mute_commands.py`
- **test_handle_admin_command_status()** (3 connections) — `server/tests/unit/commands/test_admin_commands.py`
- *... and 80 more nodes in this community*

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (31 shared connections)
- [combat services turn](combat_services_turn.md) (9 shared connections)
- [npc populate databases](npc_populate_databases.md) (7 shared connections)
- [NATS Messaging](NATS_Messaging.md) (5 shared connections)
- [command helpers functions](command_helpers_functions.md) (3 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (1 shared connections)
- [admin command setstat](admin_command_setstat.md) (1 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/tests/unit/commands/test_admin_commands.py`

## Audit Trail

- EXTRACTED: 335 (87%)
- INFERRED: 52 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*