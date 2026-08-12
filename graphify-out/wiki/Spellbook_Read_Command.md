# Spellbook Read Command

> 50 nodes

## Key Concepts

- **handle_read_command()** (24 connections) — `server/commands/read_command.py`
- **test_read_command.py** (18 connections) — `server/tests/unit/commands/test_read_command.py`
- **read_command.py** (16 connections) — `server/commands/read_command.py`
- **Any** (9 connections)
- **_process_spellbook_read()** (8 connections) — `server/commands/read_command.py`
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
- *... and 25 more nodes in this community*

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)
- [Container Open Events](Container_Open_Events.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (1 shared connections)

## Source Files

- `server/commands/read_command.py`
- `server/tests/unit/commands/test_read_command.py`

## Audit Trail

- EXTRACTED: 168 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*