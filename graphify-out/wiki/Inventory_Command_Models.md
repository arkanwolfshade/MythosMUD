# Inventory Command Models

> 119 nodes · cohesion 0.03

## Key Concepts

- **test_command_inventory.py** (62 connections) — `server/tests/unit/models/test_command_inventory.py`
- **EquipCommand** (23 connections) — `server/models/command_inventory.py`
- **PickupCommand** (22 connections) — `server/models/command_inventory.py`
- **UnequipCommand** (22 connections) — `server/models/command_inventory.py`
- **command_inventory.py** (12 connections) — `server/models/command_inventory.py`
- **DropCommand** (12 connections) — `server/models/command_inventory.py`
- **InventoryCommand** (8 connections) — `server/models/command_inventory.py`
- **Test PickupCommand can be created with index.** (6 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Strip and validate search term.** (3 connections) — `server/models/command_inventory.py`
- **Test PickupCommand validates index is >= 1.** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand validates quantity is >= 1.** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test DropCommand can have optional quantity.** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand strips whitespace from search_term.** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_index_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_missing_index()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_quantity_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_with_quantity()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_index_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_search_term_max_length()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_target_slot_max_length()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_requirements_neither_provided()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_search_term_empty_string()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_search_term_strips()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_equip_command_validate_search_term_whitespace_only()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- *... and 94 more nodes in this community*

## Relationships

- [[Base Command Models]] (38 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 398 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
