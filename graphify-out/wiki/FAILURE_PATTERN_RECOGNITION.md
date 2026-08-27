# FAILURE PATTERN RECOGNITION

> 12 nodes

## Key Concepts

- **GetCommand** (12 connections) — `server/models/command_inventory.py`
- **test_get_command_container_min_length()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_item_min_length()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_quantity_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_get_command_with_quantity()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Command for getting items from a container into inventory.** (1 connections) — `server/models/command_inventory.py`
- **Test GetCommand requires item and container.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test GetCommand can have optional quantity.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test GetCommand validates item min length.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test GetCommand validates container min length.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test GetCommand validates quantity is >= 1.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`

## Relationships

- [devDependencies](devDependencies.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [test_connection_error_methods.py](test_connection_error_methods.py.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 21 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*