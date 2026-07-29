# init

> 28 nodes

## Key Concepts

- **InventorySchemaValidationError** (20 connections) — `server/schemas/shared/inventory_schema.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
- **__init__.py** (12 connections) — `server/schemas/shared/__init__.py`
- **test_inventory_schema.py** (11 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **validate_inventory_items()** (9 connections) — `server/schemas/shared/inventory_schema.py`
- **inventory_schema.py** (7 connections) — `server/schemas/shared/inventory_schema.py`
- **_build_validator()** (5 connections) — `server/schemas/shared/inventory_schema.py`
- **test_validate_inventory_payload_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_invalid_inventory()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_invalid_quantity()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Any** (3 connections)
- **test_validate_inventory_payload_valid()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_valid()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Shared schemas: base models, target resolution, inventory validation.** (1 connections) — `server/schemas/shared/__init__.py`
- **Exception** (1 connections)
- **Inventory JSON schema validation utilities.  As recorded in the restricted stack** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Raised when inventory payloads fail schema validation.** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Internal helper to construct a Draft7 validator instance.** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Validate a complete inventory payload against the canonical schema.      Raises:** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Validate only the inventory portion to simplify testing workflows.      Raises:** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Unit tests for inventory_schema validation functions.  Tests the validation func** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() accepts valid payload.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() raises error for missing required fields.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() raises error for invalid inventory.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- *... and 3 more nodes in this community*

## Relationships

- [player repository save](player_repository_save.md) (5 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (4 shared connections)
- [invite](invite.md) (3 shared connections)
- [DropResolved](DropResolved.md) (3 shared connections)
- [combat taunt](combat_taunt.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/schemas/shared/__init__.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 108 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*