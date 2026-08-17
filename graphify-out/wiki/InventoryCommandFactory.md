# InventoryCommandFactory

> 109 nodes

## Key Concepts

- **InventoryCommandFactory** (76 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (49 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_command_factories_inventory_helpers.py** (23 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **.create_inventory_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- **test_create_drop_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_inventory_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_invalid_quantity()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_drop_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_drop_command_invalid_quantity()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_drop_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_empty_search_term()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_empty_search_term()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_with_extra_tokens()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_index_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_pickup_command_quantity_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- *... and 84 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (38 shared connections)
- [.create_unequip_command](create_unequip_command.md) (19 shared connections)
- [.create_get_command](create_get_command.md) (17 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [_parse_equip_selector](_parse_equip_selector.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 197 (70%)
- INFERRED: 83 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*