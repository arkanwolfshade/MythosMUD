# test command parser helpers

> 28 nodes

## Key Concepts

- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **_parse_equip_selector()** (5 connections) — `server/utils/command_factories_inventory.py`
- **test_create_equip_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_zero()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_negative()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_empty_search_term()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_with_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_search_term_with_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_inferred_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_with_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_equip_command_with_name_and_slot()** (3 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **_normalize_equip_slot_tokens()** (3 connections) — `server/utils/command_factories_inventory.py`
- **_maybe_extract_equip_slot()** (3 connections) — `server/utils/command_factories_inventory.py`
- **Test create_equip_command() creates EquipCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() raises error when index is zero.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() raises error when index is negative.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() handles index with slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() handles search term with slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() raises error when search term is empty.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() infers slot from known slots.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() with slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_equip_command() with item name and inferred slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Normalize multi-word slot tokens (e.g. 'main hand' -> 'main_hand'); reduces crea** (1 connections) — `server/utils/command_factories_inventory.py`
- *... and 3 more nodes in this community*

## Relationships

- [Spell Targeting](Spell_Targeting.md) (16 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [.validate search term()](validate_search_term%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 71 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*