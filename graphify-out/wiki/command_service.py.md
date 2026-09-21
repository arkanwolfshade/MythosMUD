# command_service.py

> 140 nodes

## Key Concepts

- **command_service.py** (104 connections) — `server/commands/command_service.py`
- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **asyncio** (23 connections)
- **position_commands.py** (20 connections) — `server/commands/position_commands.py`
- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **system_commands.py** (13 connections) — `server/commands/system_commands.py`
- **handle_unalias_command()** (12 connections) — `server/commands/alias_commands.py`
- **test_position_commands.py** (12 connections) — `server/tests/unit/commands/test_position_commands.py`
- **handle_aliases_command()** (11 connections) — `server/commands/alias_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **SupportsPlayerPersistence** (8 connections) — `server/services/player_position_service.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **SupportsConnectionManager** (7 connections) — `server/services/player_position_service.py`
- **_get_position_command_services()** (7 connections) — `server/commands/position_commands.py`
- **test_websocket_handler_help.py** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_help.py`
- **_create_alias()** (5 connections) — `server/commands/alias_commands.py`
- **Request** (5 connections)
- **test_help_commands.py** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- *... and 115 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (29 shared connections)
- [AliasStorage](AliasStorage.md) (16 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (10 shared connections)
- [request_with_app_container](request_with_app_container.md) (8 shared connections)
- [.state](state.md) (7 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (7 shared connections)
- [get_username_from_user](get_username_from_user.md) (6 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (6 shared connections)
- [SpellRegistry](SpellRegistry.md) (6 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (5 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (4 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (4 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/alias_commands.py`
- `server/commands/command_service.py`
- `server/commands/exploration_commands.py`
- `server/commands/help_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_alias_commands.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 355 (86%)
- INFERRED: 60 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*