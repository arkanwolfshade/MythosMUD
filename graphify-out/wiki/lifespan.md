# lifespan

> 32 nodes

## Key Concepts

- **InventorySchemaValidationError** (20 connections) — `server/schemas/shared/inventory_schema.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
- **__init__.py** (12 connections) — `server/schemas/shared/__init__.py`
- **test_inventory_schema.py** (11 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **validate_inventory_items()** (9 connections) — `server/schemas/shared/inventory_schema.py`
- **inventory_schema.py** (7 connections) — `server/schemas/shared/inventory_schema.py`
- **_build_validator()** (5 connections) — `server/schemas/shared/inventory_schema.py`
- **test_persist_player_inventory_schema_error()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **test_persist_player_validation_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
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
- **Test _persist_player() returns error on InventorySchemaValidationError.** (1 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **Test _persist_player handles InventorySchemaValidationError.** (1 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- *... and 7 more nodes in this community*

## Relationships

- [Any](Any.md) (6 shared connections)
- [test room subscription manager helpers](test_room_subscription_manager_helpers.md) (5 shared connections)
- [DropResolved](DropResolved.md) (4 shared connections)
- [NPCInstanceService](NPCInstanceService.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [.end combat()](end_combat%28%29.md) (1 shared connections)
- [test command service](test_command_service.md) (1 shared connections)

## Source Files

- `server/schemas/shared/__init__.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 118 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*