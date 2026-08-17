# InventorySchemaValidationError

> 26 nodes

## Key Concepts

- **InventorySchemaValidationError** (20 connections) — `server/schemas/shared/inventory_schema.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
- **test_inventory_schema.py** (12 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **validate_inventory_items()** (9 connections) — `server/schemas/shared/inventory_schema.py`
- **inventory_schema.py** (7 connections) — `server/schemas/shared/inventory_schema.py`
- **_build_validator()** (5 connections) — `server/schemas/shared/inventory_schema.py`
- **test_validate_inventory_items_invalid_quantity()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_invalid_inventory()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_valid()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_valid()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Any** (3 connections)
- **Exception** (1 connections)
- **Inventory JSON schema validation utilities. As recorded in the restricted…** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Internal helper to construct a Draft7 validator instance.** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Validate a complete inventory payload against the canonical schema. Raises:…** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Validate only the inventory portion to simplify testing workflows. Raises:…** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Raised when inventory payloads fail schema validation.** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Unit tests for inventory_schema validation functions. Tests the validation…** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() accepts valid payload.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() raises error for missing required fields.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() raises error for invalid inventory.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_items() accepts valid items.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_items() raises error for missing required fields.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- *... and 1 more nodes in this community*

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (7 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (4 shared connections)
- [PlayerSavePreparer](PlayerSavePreparer.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [test_combat_schema.py](test_combat_schema.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 57 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*