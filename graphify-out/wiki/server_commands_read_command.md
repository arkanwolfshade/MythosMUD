# server commands read command

> 51 nodes

## Key Concepts

- **handle_read_command()** (23 connections) — `server/commands/read_command.py`
- **test_read_command.py** (19 connections) — `server/tests/unit/commands/test_read_command.py`
- **read_command.py** (16 connections) — `server/commands/read_command.py`
- **asyncio** (15 connections)
- **_process_spellbook_read()** (8 connections) — `server/commands/read_command.py`
- **Any** (8 connections)
- **_format_learn_spell_message()** (5 connections) — `server/commands/read_command.py`
- **_learn_single_spell()** (5 connections) — `server/commands/read_command.py`
- **_learn_specific_spell()** (5 connections) — `server/commands/read_command.py`
- **_find_item_in_inventory()** (4 connections) — `server/commands/read_command.py`
- **_list_spells_in_book()** (4 connections) — `server/commands/read_command.py`
- **_validate_spellbook()** (4 connections) — `server/commands/read_command.py`
- **test_handle_read_command()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_empty_spellbook()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_inventory_json_error()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_item_not_found()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_learn_failure()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_multiple_spells()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_no_spell_learning_service()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_no_target()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_not_spellbook()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_player_not_found()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_single_spell_learn()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_specific_spell()** (4 connections) — `server/tests/unit/commands/test_read_command.py`
- *... and 26 more nodes in this community*

## Relationships

- [server commands admin commands](server_commands_admin_commands.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/read_command.py`
- `server/tests/unit/commands/test_read_command.py`

## Audit Trail

- EXTRACTED: 102 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*