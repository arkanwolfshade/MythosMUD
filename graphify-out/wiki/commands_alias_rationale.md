# commands alias rationale

> 69 nodes

## Key Concepts

- **test_alias_commands.py** (30 connections) — `server/tests/unit/commands/test_alias_commands.py`
- **handle_alias_command()** (24 connections) — `server/commands/alias_commands.py`
- **alias_commands.py** (15 connections) — `server/commands/alias_commands.py`
- **handle_unalias_command()** (12 connections) — `server/commands/alias_commands.py`
- **handle_aliases_command()** (11 connections) — `server/commands/alias_commands.py`
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

- [commands whisper command](commands_whisper_command.md) (9 shared connections)
- [commands npc admin](commands_npc_admin.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)

## Source Files

- `server/commands/alias_commands.py`
- `server/tests/unit/commands/test_alias_commands.py`

## Audit Trail

- EXTRACTED: 219 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*