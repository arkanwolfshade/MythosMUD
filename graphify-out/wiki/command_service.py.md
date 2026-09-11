# command_service.py

> 50 nodes

## Key Concepts

- **command_service.py** (108 connections) — `server/commands/command_service.py`
- **server/commands/__init__.py** (29 connections) — `server/commands/__init__.py`
- **position_commands.py** (20 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (12 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **handle_help_command()** (11 connections) — `server/commands/system_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **SupportsPlayerPersistence** (8 connections) — `server/services/player_position_service.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **SupportsConnectionManager** (7 connections) — `server/services/player_position_service.py`
- **_get_position_command_services()** (7 connections) — `server/commands/position_commands.py`
- **Request** (5 connections)
- **test_help_commands.py** (5 connections) — `server/tests/unit/commands/test_help_commands.py`
- **asyncio** (5 connections)
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **test_handle_help_command_no_topic()** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_unknown_topic()** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_help_command_with_topic()** (4 connections) — `server/tests/unit/commands/test_help_commands.py`
- **test_handle_ground_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_lie_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_sit_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_already_standing_still_sends_player_update()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **help_commands.py** (4 connections) — `server/commands/help_commands.py`
- *... and 25 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (20 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (9 shared connections)
- [AliasStorage](AliasStorage.md) (8 shared connections)
- [Player](Player.md) (8 shared connections)
- [admin_commands.py](admin_commands.py.md) (8 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (8 shared connections)
- [communication_commands.py](communication_commands.py.md) (8 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (6 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (6 shared connections)
- [.async_persistence](async_persistence.md) (5 shared connections)
- [command_result_text](command_result_text.md) (4 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (4 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/command_service.py`
- `server/commands/help_commands.py`
- `server/commands/position_commands.py`
- `server/commands/system_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_help_commands.py`
- `server/tests/unit/commands/test_position_commands.py`

## Audit Trail

- EXTRACTED: 176 (73%)
- INFERRED: 65 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*