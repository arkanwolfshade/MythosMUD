# Communication Command Handlers

> 69 nodes

## Key Concepts

- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **handle_alias_command()** (25 connections) — `server/commands/alias_commands.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **handle_unalias_command()** (13 connections) — `server/commands/alias_commands.py`
- **handle_aliases_command()** (12 connections) — `server/commands/alias_commands.py`
- **_create_alias()** (5 connections) — `server/commands/alias_commands.py`
- **_extract_alias_params()** (4 connections) — `server/commands/alias_commands.py`
- **Any** (4 connections)
- **_view_alias()** (4 connections) — `server/commands/alias_commands.py`
- **_validate_alias_params()** (3 connections) — `server/commands/alias_commands.py`
- **test_handle_alias_command_no_storage()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_no_args()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_view_existing()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_view_nonexistent()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_args()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_from_structured_data()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_invalid_name_too_long()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_invalid_command_too_long()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_circular_reference()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_alias_command_create_error()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_aliases_command_no_storage()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_aliases_command_no_aliases()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_aliases_command_with_aliases()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_aliases_command_error()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_unalias_command_no_storage()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- *... and 44 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (11 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)

## Source Files

- `server/commands/alias_commands.py`
- `server/tests/unit/commands/test_alias_commands.py`

## Audit Trail

- EXTRACTED: 219 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*