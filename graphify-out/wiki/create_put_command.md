# .create_put_command

> 20 nodes

## Key Concepts

- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **test_create_put_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_only_item()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_quantity_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_quantity_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_with_in()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_put_command_with_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_put_command_multi_word_container()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_multi_word_container_no_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_with_in_keyword()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() handles optional 'in' keyword.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_put_command() with quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_put_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() raises error with only item.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() handles 'in' keyword.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() raises error when quantity is zero.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() raises error when quantity is negative.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() handles multi-word container.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_put_command() handles multi-word container without quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Create put command. Supports: put <item> [in] <container> [quantity] The "in"…** (1 connections) — `server/utils/command_factories_inventory.py`

## Relationships

- [InventoryCommandFactory](InventoryCommandFactory.md) (10 shared connections)
- [test_command_factories_inventory.py](test_command_factories_inventory.py.md) (7 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [test_command_factories_inventory_helpers.py](test_command_factories_inventory_helpers.py.md) (3 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 32 (71%)
- INFERRED: 13 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*