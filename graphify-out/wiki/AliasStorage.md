# AliasStorage

> 159 nodes

## Key Concepts

- **AliasStorage** (217 connections) — `server/alias_storage.py`
- **command_service.py** (92 connections) — `server/commands/command_service.py`
- **.__init__()** (71 connections) — `server/commands/command_service.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **position_commands.py** (21 connections) — `server/commands/position_commands.py`
- **handle_mute_command()** (19 connections) — `server/commands/admin_mute_commands.py`
- **handle_teleport_command()** (19 connections) — `server/commands/admin_teleport_commands.py`
- **handle_say_command()** (17 connections) — `server/commands/communication_commands.py`
- **Any** (16 connections)
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **handle_admin_command()** (14 connections) — `server/commands/admin_commands.py`
- **handle_goto_command()** (14 connections) — `server/commands/admin_teleport_commands.py`
- **handle_pose_command()** (14 connections) — `server/commands/communication_commands.py`
- **handle_inventory_command()** (14 connections) — `server/commands/inventory_commands.py`
- **handle_unalias_command()** (13 connections) — `server/commands/alias_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_mutes_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **handle_unmute_command()** (12 connections) — `server/commands/admin_mute_commands.py`
- **handle_aliases_command()** (12 connections) — `server/commands/alias_commands.py`
- **handle_global_command()** (12 connections) — `server/commands/communication_commands.py`
- **_handle_position_change()** (12 connections) — `server/commands/position_commands.py`
- *... and 134 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (53 shared connections)
- [request_with_app_container](request_with_app_container.md) (36 shared connections)
- [alias_storage.py](alias_storage.py.md) (34 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (34 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (28 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (22 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (18 shared connections)
- [.get_player_aliases](get_player_aliases.md) (17 shared connections)
- [get_username_from_user](get_username_from_user.md) (16 shared connections)
- [combat_loader.py](combat_loader.py.md) (11 shared connections)
- [inventory_commands.py](inventory_commands.py.md) (11 shared connections)
- [.state](state.md) (11 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/admin_setlucidity_command.py`
- `server/commands/admin_summon_command.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/alias_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/magic_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 765 (87%)
- INFERRED: 113 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*