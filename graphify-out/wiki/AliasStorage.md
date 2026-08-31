# AliasStorage

> 170 nodes

## Key Concepts

- **AliasStorage** (264 connections) — `server/alias_storage.py`
- **command_service.py** (108 connections) — `server/commands/command_service.py`
- **alias_storage.py** (75 connections) — `server/alias_storage.py`
- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **command_parser.py** (47 connections) — `server/utils/command_parser.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **position_commands.py** (21 connections) — `server/commands/position_commands.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **magic_service()** (14 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **handle_inventory_command()** (13 connections) — `server/commands/inventory_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **test_position_commands.py** (13 connections) — `server/tests/unit/commands/test_position_commands.py`
- **handle_unalias_command()** (12 connections) — `server/commands/alias_commands.py`
- **handle_aliases_command()** (11 connections) — `server/commands/alias_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **.get_player_aliases()** (10 connections) — `server/alias_storage.py`
- **handle_add_admin_command()** (10 connections) — `server/commands/admin_mute_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **.get_alias_file_path()** (9 connections) — `server/alias_storage.py`
- **._load_alias_data()** (9 connections) — `server/alias_storage.py`
- *... and 145 more nodes in this community*

## Relationships

- [Alias](Alias.md) (65 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (35 shared connections)
- [get_logger](get_logger.md) (32 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (29 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (27 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (20 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (18 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (17 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (16 shared connections)
- [.state](state.md) (15 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (13 shared connections)
- [command_result_text](command_result_text.md) (13 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/__init__.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`
- `server/commands/alias_commands.py`
- `server/commands/command_service.py`
- `server/commands/exploration_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/magic_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/utils/alias_graph.py`
- `server/utils/command_helpers.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 745 (80%)
- INFERRED: 189 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*