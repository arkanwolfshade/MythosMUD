# Community 277

> 59 nodes

## Key Concepts

- **InventorySchemaValidationError** (21 connections) — `server/schemas/shared/inventory_schema.py`
- **schemas/shared/__init__.py** (15 connections) — `server/schemas/shared/__init__.py`
- **PlayerSavePreparer** (13 connections) — `server/persistence/repositories/player_repository_save.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
- **test_inventory_schema.py** (13 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **player_repository_save.py** (11 connections) — `server/persistence/repositories/player_repository_save.py`
- **.prepare()** (10 connections) — `server/persistence/repositories/player_repository_save.py`
- **validate_inventory_items()** (10 connections) — `server/schemas/shared/inventory_schema.py`
- **inventory_schema.py** (8 connections) — `server/schemas/shared/inventory_schema.py`
- **._prepare_inventory_payload()** (7 connections) — `server/persistence/repositories/player_repository_save.py`
- **Any** (7 connections)
- **Player** (7 connections)
- **_parse_equipped_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **_parse_inventory_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._ensure_inventory_record()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._normalize_timestamps()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_numeric_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_string_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **_build_validator()** (5 connections) — `server/schemas/shared/inventory_schema.py`
- **test_validate_inventory_items_inner_container_capacity_uses_global_cap()** (5 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **._normalize_is_admin()** (4 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_validate_inventory_items_invalid_quantity()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_invalid_inventory()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- *... and 34 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (13 shared connections)
- [Community 131](Community_131.md) (5 shared connections)
- [Community 284](Community_284.md) (2 shared connections)
- [Community 241](Community_241.md) (1 shared connections)
- [Community 227](Community_227.md) (1 shared connections)
- [Community 291](Community_291.md) (1 shared connections)
- [Magic & Tick Services](Magic_&_Tick_Services.md) (1 shared connections)
- [Community 187](Community_187.md) (1 shared connections)
- [Community 67](Community_67.md) (1 shared connections)
- [Community 252](Community_252.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository_save.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 126 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*