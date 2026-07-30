# websocket handler app state

> 87 nodes

## Key Concepts

- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **__init__.py** (29 connections) — `server/commands/__init__.py`
- **handle_alias_command()** (25 connections) — `server/commands/alias_commands.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **handle_unalias_command()** (13 connections) — `server/commands/alias_commands.py`
- **handle_aliases_command()** (12 connections) — `server/commands/alias_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (11 connections) — `server/tests/unit/commands/test_position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_sit_command()** (9 connections) — `server/commands/position_commands.py`
- **_create_alias()** (5 connections) — `server/commands/alias_commands.py`
- **_extract_alias_params()** (4 connections) — `server/commands/alias_commands.py`
- **Any** (4 connections)
- **_view_alias()** (4 connections) — `server/commands/alias_commands.py`
- **Any** (4 connections)
- **_validate_alias_params()** (3 connections) — `server/commands/alias_commands.py`
- **test_handle_alias_command_no_storage()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_no_args()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_view_existing()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_view_nonexistent()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_args()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_structured_data()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_invalid_name_too_long()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_invalid_command_too_long()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- *... and 62 more nodes in this community*

## Relationships

- [DropResolved](DropResolved.md) (12 shared connections)
- [test magic commands](test_magic_commands.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (8 shared connections)
- [Player Position Service](Player_Position_Service.md) (6 shared connections)
- [.get instance()](get_instance%28%29.md) (4 shared connections)
- [Any](Any.md) (3 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (3 shared connections)
- [get skill repository()](get_skill_repository%28%29.md) (2 shared connections)
- [AuthSlice](AuthSlice.md) (2 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (2 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (1 shared connections)
- [NATS](NATS.md) (1 shared connections)

## Source Files

- `server/commands/__init__.py`
- `server/commands/alias_commands.py`
- `server/commands/position_commands.py`
- `server/tests/unit/commands/test_alias_commands.py`
- `server/tests/unit/commands/test_position_commands.py`

## Audit Trail

- EXTRACTED: 316 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*