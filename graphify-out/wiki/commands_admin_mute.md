# commands admin mute

> 105 nodes

## Key Concepts

- **test_admin_commands.py** (37 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **handle_mute_command()** (19 connections) — `server/commands/admin_mute_commands.py`
- **Any** (16 connections)
- **handle_admin_command()** (13 connections) — `server/commands/admin_commands.py`
- **handle_unmute_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **handle_add_admin_command()** (11 connections) — `server/commands/admin_mute_commands.py`
- **handle_mutes_command()** (11 connections) — `server/commands/admin_mute_commands.py`
- **_handle_admin_status_command()** (9 connections) — `server/commands/admin_commands.py`
- **handle_mute_global_command()** (9 connections) — `server/commands/admin_mute_commands.py`
- **handle_unmute_global_command()** (9 connections) — `server/commands/admin_mute_commands.py`
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
- *... and 80 more nodes in this community*

## Relationships

- [alias storage rationale](alias_storage_rationale.md) (11 shared connections)
- [realtime real time](realtime_real_time.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (10 shared connections)
- [realtime game state](realtime_game_state.md) (8 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [npc service services](npc_service_services.md) (4 shared connections)
- [container schemas containers](container_schemas_containers.md) (3 shared connections)
- [command models admin](command_models_admin.md) (3 shared connections)
- [admin structured logging](admin_structured_logging.md) (3 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (3 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (2 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (2 shared connections)

## Source Files

- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_admin_commands.py`

## Audit Trail

- EXTRACTED: 351 (86%)
- INFERRED: 58 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*