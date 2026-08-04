# npc commands admin

> 138 nodes

## Key Concepts

- **test_command_inventory.py** (63 connections) — `server/tests/unit/models/test_command_inventory.py`
- **EquipCommand** (23 connections) — `server/models/command_inventory.py`
- **PickupCommand** (22 connections) — `server/models/command_inventory.py`
- **UnequipCommand** (22 connections) — `server/models/command_inventory.py`
- **DropCommand** (12 connections) — `server/models/command_inventory.py`
- **PutCommand** (12 connections) — `server/models/command_inventory.py`
- **GetCommand** (12 connections) — `server/models/command_inventory.py`
- **test_pickup_command_validate_search_term_empty_string()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_requirements_neither_provided()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_index_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_search_term_max_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_index_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_missing_index()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_put_command_item_min_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_put_command_container_min_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_put_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_item_min_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_container_min_length()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_search_term_empty_string()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_requirements_neither_provided()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_slot_empty_string()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_slot_whitespace_only()** (4 connections) — `server/tests/unit/models/test_command_inventory.py`
- *... and 113 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (27 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (24 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 401 (92%)
- INFERRED: 36 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*