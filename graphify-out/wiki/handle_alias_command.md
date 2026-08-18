# handle_alias_command

> 15 nodes

## Key Concepts

- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **_extract_alias_params()** (4 connections) — `server/commands/alias_commands.py`
- **_view_alias()** (4 connections) — `server/commands/alias_commands.py`
- **test_handle_alias_command_invalid_command_too_long()** (4 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_invalid_name_too_long()** (4 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_update_existing()** (4 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_view_from_structured_data()** (4 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Any** (4 connections)
- **Extract alias_name and command from command_data. Returns (alias_name, command).** (1 connections) — `server/commands/alias_commands.py`
- **View an existing alias. Returns result dict.** (1 connections) — `server/commands/alias_commands.py`
- **Handle the alias command for creating and viewing aliases. Args: command_data:…** (1 connections) — `server/commands/alias_commands.py`
- **Test handle_alias_command with alias name too long.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_alias_command with command too long.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_alias_command viewing alias from structured data.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **Test handle_alias_command updating existing alias.** (1 connections) — `server/tests/unit/commands/test_alias_commands.py`

## Relationships

- [asyncio](asyncio.md) (6 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (5 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [_create_alias](_create_alias.md) (1 shared connections)
- [test_handle_alias_command_circular_reference](test_handle_alias_command_circular_reference.md) (1 shared connections)
- [test_handle_alias_command_create_error](test_handle_alias_command_create_error.md) (1 shared connections)
- [test_handle_alias_command_create_from_args](test_handle_alias_command_create_from_args.md) (1 shared connections)
- [test_handle_alias_command_create_from_structured_data](test_handle_alias_command_create_from_structured_data.md) (1 shared connections)
- [test_handle_alias_command_invalid_command_empty](test_handle_alias_command_invalid_command_empty.md) (1 shared connections)
- [test_handle_alias_command_invalid_name_empty](test_handle_alias_command_invalid_name_empty.md) (1 shared connections)

## Source Files

- `server/commands/alias_commands.py`
- `server/tests/unit/commands/test_alias_commands.py`

## Audit Trail

- EXTRACTED: 43 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*