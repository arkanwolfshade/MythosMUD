# .create_equip_command

> 20 nodes

## Key Concepts

- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **test_create_equip_command_empty_search_term()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_with_slot()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_inferred_slot()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_search_term_with_slot()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **_normalize_equip_slot_tokens()** (3 connections) — `server/utils/command_factories_inventory.py`
- **Test create_equip_command() raises error when index is zero.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() raises error when index is negative.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() handles index with slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() handles search term with slot.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() raises error when search term is empty.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() infers slot from known slots.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() creates EquipCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_equip_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Create equip command.** (1 connections) — `server/utils/command_factories_inventory.py`
- **Normalize multi-word slot tokens (e.g. 'main hand' -> 'main_hand'); reduces…** (1 connections) — `server/utils/command_factories_inventory.py`

## Relationships

- [InventoryCommandFactory](InventoryCommandFactory.md) (9 shared connections)
- [test_command_factories_inventory.py](test_command_factories_inventory.py.md) (8 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_command_factories_inventory_helpers.py](test_command_factories_inventory_helpers.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 34 (74%)
- INFERRED: 12 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*