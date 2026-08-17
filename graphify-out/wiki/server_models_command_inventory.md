# server models command inventory

> 134 nodes

## Key Concepts

- **test_command_inventory.py** (65 connections) — `server/tests/unit/models/test_command_inventory.py`
- **EquipCommand** (23 connections) — `server/models/command_inventory.py`
- **PickupCommand** (22 connections) — `server/models/command_inventory.py`
- **UnequipCommand** (22 connections) — `server/models/command_inventory.py`
- **command_inventory.py** (14 connections) — `server/models/command_inventory.py`
- **DropCommand** (12 connections) — `server/models/command_inventory.py`
- **GetCommand** (12 connections) — `server/models/command_inventory.py`
- **PutCommand** (12 connections) — `server/models/command_inventory.py`
- **InventoryCommand** (8 connections) — `server/models/command_inventory.py`
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
- *... and 109 more nodes in this community*

## Relationships

- [server models command](server_models_command.md) (25 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (7 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 177 (72%)
- INFERRED: 68 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*