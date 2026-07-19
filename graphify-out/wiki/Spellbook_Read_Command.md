# Spellbook Read Command

> 45 nodes · cohesion 0.07

## Key Concepts

- **handle_read_command()** (27 connections) — `server/commands/read_command.py`
- **test_read_command.py** (17 connections) — `server/tests/unit/commands/test_read_command.py`
- **Any** (8 connections) — `server/commands/read_command.py`
- **_format_learn_spell_message()** (5 connections) — `server/commands/read_command.py`
- **_learn_single_spell()** (5 connections) — `server/commands/read_command.py`
- **_learn_specific_spell()** (5 connections) — `server/commands/read_command.py`
- **Test handle_read_command() when player is not found.** (5 connections) — `server/tests/unit/commands/test_read_command.py`
- **_find_item_in_inventory()** (4 connections) — `server/commands/read_command.py`
- **_list_spells_in_book()** (4 connections) — `server/commands/read_command.py`
- **_validate_spellbook()** (4 connections) — `server/commands/read_command.py`
- **test_handle_read_command()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_empty_spellbook()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_inventory_json_error()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_item_not_found()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_learn_failure()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_multiple_spells()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_no_spell_learning_service()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_no_target()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_not_spellbook()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_single_spell_learn()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_specific_spell()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_spell_not_in_book()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- **test_handle_read_command_spell_registry_not_available()** (3 connections) — `server/tests/unit/commands/test_read_command.py`
- *... and 20 more nodes in this community*

## Relationships

- [[Alias Expansion Logic]] (10 shared connections)
- [[Communication Command Handlers]] (2 shared connections)
- [[Ground and Rescue Commands]] (2 shared connections)
- [[Command Helper Utilities]] (1 shared connections)
- [[Lucidity Recovery Commands]] (1 shared connections)

## Source Files

- `server/commands/read_command.py`
- `server/tests/unit/commands/test_read_command.py`

## Audit Trail

- EXTRACTED: 147 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
