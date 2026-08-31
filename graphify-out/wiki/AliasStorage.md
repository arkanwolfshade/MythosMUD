# AliasStorage

> 240 nodes

## Key Concepts

- **AliasStorage** (264 connections) — `server/alias_storage.py`
- **command_service.py** (108 connections) — `server/commands/command_service.py`
- **alias_storage.py** (75 connections) — `server/alias_storage.py`
- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **test_alias_commands.py** (31 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **asyncio** (23 connections)
- **position_commands.py** (21 connections) — `server/commands/position_commands.py`
- **test_communication_commands_channels.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_channels.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **magic_service()** (14 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **handle_inventory_command()** (13 connections) — `server/commands/inventory_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **asyncio** (13 connections)
- **test_position_commands.py** (13 connections) — `server/tests/unit/commands/test_position_commands.py`
- **handle_unalias_command()** (12 connections) — `server/commands/alias_commands.py`
- **handle_aliases_command()** (11 connections) — `server/commands/alias_commands.py`
- **handle_global_command()** (11 connections) — `server/commands/communication_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **.get_player_aliases()** (10 connections) — `server/alias_storage.py`
- **handle_local_command()** (10 connections) — `server/commands/communication_commands.py`
- *... and 215 more nodes in this community*

## Relationships

- [Alias](Alias.md) (65 shared connections)
- [get_logger](get_logger.md) (43 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (29 shared connections)
- [request_with_app_container](request_with_app_container.md) (29 shared connections)
- [get_username_from_user](get_username_from_user.md) (26 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (18 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (16 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (14 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (13 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (13 shared connections)
- [.state](state.md) (12 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (11 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/__init__.py`
- `server/commands/alias_commands.py`
- `server/commands/command_service.py`
- `server/commands/communication_commands.py`
- `server/commands/exploration_commands.py`
- `server/commands/follow_commands.py`
- `server/commands/help_commands.py`
- `server/commands/inventory_commands.py`
- `server/commands/magic_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/commands/time_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_alias_commands.py`
- `server/tests/unit/commands/test_communication_commands_channels.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/utils/alias_graph.py`

## Audit Trail

- EXTRACTED: 828 (84%)
- INFERRED: 152 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*