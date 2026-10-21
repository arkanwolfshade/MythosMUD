# ADR-026: Item Catalog Metadata Contracts

> 31 nodes · cohesion 0.11

## Key Concepts

- **InventorySchemaValidationError** (21 connections) — `server/schemas/shared/inventory_schema.py`
- **schemas/shared/__init__.py** (15 connections) — `server/schemas/shared/__init__.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
- **test_inventory_schema.py** (13 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **validate_inventory_items()** (10 connections) — `server/schemas/shared/inventory_schema.py`
- **inventory_schema.py** (8 connections) — `server/schemas/shared/inventory_schema.py`
- **_build_validator()** (5 connections) — `server/schemas/shared/inventory_schema.py`
- **test_validate_inventory_items_inner_container_capacity_uses_global_cap()** (5 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_invalid_quantity()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_invalid_inventory()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Any** (3 connections)
- **test_validate_inventory_items_valid()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_valid()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Shared schemas: base models, target resolution, inventory validation.** (1 connections) — `server/schemas/shared/__init__.py`
- **Exception** (1 connections)
- **Inventory JSON schema validation utilities. As recorded in the restricted…** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Internal helper to construct a Draft7 validator instance.** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Validate a complete inventory payload against the canonical schema. Raises:…** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Validate only the inventory portion to simplify testing workflows. Raises:…** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Raised when inventory payloads fail schema validation.** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **parametrize** (1 connections)
- **Unit tests for inventory_schema validation functions. Tests the validation…** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() accepts valid payload.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- *... and 6 more nodes in this community*

## Relationships

- [test_websocket_helpers.py](test_websocket_helpers.py.md) (8 shared connections)
- [test_room_write_procedures.py](test_room_write_procedures.py.md) (5 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (2 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (2 shared connections)
- [item_prototype.schema.json](item_prototype.schema.json.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (1 shared connections)
- [MemoryThresholdMonitor](MemoryThresholdMonitor.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [saveMapChanges.ts](saveMapChanges.ts.md) (1 shared connections)

## Source Files

- `server/schemas/shared/__init__.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 73 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*