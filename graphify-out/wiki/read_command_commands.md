# read command commands

> 49 nodes

## Key Concepts

- **handle_read_command()** (27 connections) — `server/commands/read_command.py`
- **test_read_command.py** (18 connections) — `server/tests/unit/commands/test_read_command.py`
- **read_command.py** (15 connections) — `server/commands/read_command.py`
- **Any** (8 connections)
- **_format_learn_spell_message()** (5 connections) — `server/commands/read_command.py`
- **_learn_specific_spell()** (5 connections) — `server/commands/read_command.py`
- **_learn_single_spell()** (5 connections) — `server/commands/read_command.py`
- **_find_item_in_inventory()** (4 connections) — `server/commands/read_command.py`
- **_validate_spellbook()** (4 connections) — `server/commands/read_command.py`
- **_list_spells_in_book()** (4 connections) — `server/commands/read_command.py`
- **test_handle_read_command()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_no_target()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_no_spell_learning_service()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_item_not_found()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_not_spellbook()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_empty_spellbook()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_multiple_spells()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_single_spell_learn()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_specific_spell()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_spell_not_in_book()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_spell_registry_not_available()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_learn_failure()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_inventory_json_error()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- *... and 24 more nodes in this community*

## Relationships

- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/read_command.py`
- `server/tests/unit/commands/test_read_command.py`

## Audit Trail

- EXTRACTED: 162 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*