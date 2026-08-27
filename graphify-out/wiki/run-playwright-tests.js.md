# run-playwright-tests.js

> 11 nodes

## Key Concepts

- **DropCommand** (12 connections) — `server/models/command_inventory.py`
- **test_drop_command_index_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_missing_index()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_quantity_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_drop_command_with_quantity()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test DropCommand requires index.** (2 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Command for dropping items from inventory into the room.** (1 connections) — `server/models/command_inventory.py`
- **Test DropCommand can have optional quantity.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test DropCommand validates index is >= 1.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test DropCommand validates quantity is >= 1.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`

## Relationships

- [devDependencies](devDependencies.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [.get_original_string_id](get_original_string_id.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 21 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*