# Test Command Inventory

> 126 nodes

## Key Concepts

- **test_command_inventory.py** (65 connections) — `server/tests/unit/models/test_command_inventory.py`
- **EquipCommand** (23 connections) — `server/models/command_inventory.py`
- **PickupCommand** (22 connections) — `server/models/command_inventory.py`
- **UnequipCommand** (22 connections) — `server/models/command_inventory.py`
- **DropCommand** (12 connections) — `server/models/command_inventory.py`
- **field_validator** (5 connections)
- **.validate_equip_requirements()** (3 connections) — `server/models/command_inventory.py`
- **.validate_search_term()** (3 connections) — `server/models/command_inventory.py`
- **.validate_slot()** (3 connections) — `server/models/command_inventory.py`
- **.validate_pickup_requirements()** (3 connections) — `server/models/command_inventory.py`
- **.validate_search_term()** (3 connections) — `server/models/command_inventory.py`
- **.validate_search_term()** (3 connections) — `server/models/command_inventory.py`
- **.validate_slot()** (3 connections) — `server/models/command_inventory.py`
- **.validate_unequip_requirements()** (3 connections) — `server/models/command_inventory.py`
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
- *... and 101 more nodes in this community*

## Relationships

- [Command Aliases](Command_Aliases.md) (32 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (4 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 217 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*