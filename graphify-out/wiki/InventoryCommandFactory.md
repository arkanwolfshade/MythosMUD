# InventoryCommandFactory

> 30 nodes

## Key Concepts

- **InventoryCommandFactory** (76 connections) — `server/utils/command_factories_inventory.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **test_create_pickup_command_empty_search_term()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_with_extra_tokens()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_quantity_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_quantity_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_with_index()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_with_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_quantity_only()** (4 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **._parse_index_or_search_term()** (4 connections) — `server/utils/command_factories_inventory.py`
- **._parse_quantity_from_args()** (4 connections) — `server/utils/command_factories_inventory.py`
- **Test create_pickup_command() with numeric index.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_pickup_command() with quantity.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **Test create_pickup_command() creates PickupCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error with no args.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when quantity is zero.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when quantity is negative.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when index is zero.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when index is negative.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when index has extra tokens.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **Test create_pickup_command() raises error when search term is empty.** (1 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- *... and 5 more nodes in this community*

## Relationships

- [test_command_factories_inventory.py](test_command_factories_inventory.py.md) (19 shared connections)
- [test_command_factories_inventory_helpers.py](test_command_factories_inventory_helpers.py.md) (15 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [.create_put_command](create_put_command.md) (10 shared connections)
- [.create_get_command](create_get_command.md) (10 shared connections)
- [.create_equip_command](create_equip_command.md) (9 shared connections)
- [.create_drop_command](create_drop_command.md) (7 shared connections)
- [CombatCommandFactory](CombatCommandFactory.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [test_command_inventory.py](test_command_inventory.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 59 (46%)
- INFERRED: 68 (54%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*