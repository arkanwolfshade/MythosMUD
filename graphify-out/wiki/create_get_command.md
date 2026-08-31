# .create_get_command

> 20 nodes

## Key Concepts

- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **test_create_get_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_get_command_quantity_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_get_command_quantity_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_get_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_get_command_with_from()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_get_command_multi_word_container()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_get_command_multi_word_container_no_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_get_command_only_item_get_from_room()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_get_command_with_from_keyword()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_get_command() creates GetCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_get_command() handles optional 'from' keyword.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_get_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_get_command() with single arg returns get-from-room…** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_get_command() handles 'from' keyword.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_get_command() raises error when quantity is zero.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_get_command() raises error when quantity is negative.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_get_command() handles multi-word container.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_get_command() handles multi-word container without quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Create get command. Supports: get <item> [from] <container> [quantity] The…** (1 connections) — `server/utils/command_factories_inventory.py`

## Relationships

- [InventoryCommandFactory](InventoryCommandFactory.md) (10 shared connections)
- [test_command_factories_inventory.py](test_command_factories_inventory.py.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_command_factories_inventory_helpers.py](test_command_factories_inventory_helpers.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 31 (72%)
- INFERRED: 12 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*