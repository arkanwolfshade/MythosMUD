# PlayerSavePreparer

> 56 nodes

## Key Concepts

- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **InventorySchemaValidationError** (16 connections) — `server/schemas/shared/inventory_schema.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
- **schemas/shared/__init__.py** (12 connections) — `server/schemas/shared/__init__.py`
- **player_repository_save.py** (11 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_inventory_schema.py** (11 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **.prepare()** (10 connections) — `server/persistence/repositories/player_repository_save.py`
- **validate_inventory_items()** (9 connections) — `server/schemas/shared/inventory_schema.py`
- **._prepare_inventory_payload()** (7 connections) — `server/persistence/repositories/player_repository_save.py`
- **Any** (7 connections)
- **Player** (7 connections)
- **inventory_schema.py** (7 connections) — `server/schemas/shared/inventory_schema.py`
- **_parse_equipped_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **_parse_inventory_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._ensure_inventory_record()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._normalize_timestamps()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_numeric_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_string_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **_build_validator()** (5 connections) — `server/schemas/shared/inventory_schema.py`
- **._normalize_is_admin()** (4 connections) — `server/persistence/repositories/player_repository_save.py`
- **.execute()** (3 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_validate_inventory_items_invalid_quantity()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_missing_required()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_valid()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_invalid_inventory()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- *... and 31 more nodes in this community*

## Relationships

- [log_and_raise](log_and_raise.md) (10 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (3 shared connections)
- [test_invite_schemas.py](test_invite_schemas.py.md) (3 shared connections)
- [test_inventory_commands_more_helpers.py](test_inventory_commands_more_helpers.py.md) (2 shared connections)
- [test_inventory_helpers_extended.py](test_inventory_helpers_extended.py.md) (2 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository_save.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 119 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*