# command parser helpers

> 25 nodes

## Key Concepts

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
- **Inventory JSON schema validation utilities.  As recorded in the restricted stack** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Internal helper to construct a Draft7 validator instance.** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Validate a complete inventory payload against the canonical schema.      Raises:** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Validate only the inventory portion to simplify testing workflows.      Raises:** (1 connections) — `server/schemas/shared/inventory_schema.py`
- **Unit tests for inventory_schema validation functions.  Tests the validation func** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() accepts valid payload.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() raises error for missing required fields.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_payload() raises error for invalid inventory.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_items() accepts valid items.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_items() raises error for missing required fields.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **Test validate_inventory_items() raises error for invalid quantity.** (1 connections) — `server/tests/unit/schemas/test_inventory_schema.py`

## Relationships

- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (8 shared connections)
- [command factories moderation](command_factories_moderation.md) (3 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (2 shared connections)
- [logging file setup](logging_file_setup.md) (2 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (1 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/schemas/shared/__init__.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 90 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*