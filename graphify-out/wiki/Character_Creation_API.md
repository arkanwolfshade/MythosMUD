# Character Creation API

> 65 nodes

## Key Concepts

- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **handle_alias_command()** (25 connections) — `server/commands/alias_commands.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
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
- **test_handle_unalias_command_no_args()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **test_handle_unalias_command_alias_not_found()** (3 connections) — `server/tests/unit/commands/test_alias_commands.py`
- *... and 40 more nodes in this community*

## Relationships

- [Chat NATS Publisher](Chat_NATS_Publisher.md) (20 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)

## Source Files

- `server/commands/alias_commands.py`
- `server/tests/unit/commands/test_alias_commands.py`

## Audit Trail

- EXTRACTED: 194 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*