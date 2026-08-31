# InventorySchemaValidationError

> 56 nodes

## Key Concepts

- **InventorySchemaValidationError** (20 connections) — `server/schemas/shared/inventory_schema.py`
- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **schemas/shared/__init__.py** (16 connections) — `server/schemas/shared/__init__.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
- **player_repository_save.py** (12 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_inventory_schema.py** (12 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
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
- **test_validate_inventory_items_invalid_quantity()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_invalid_inventory()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **.execute()** (3 connections) — `server/persistence/repositories/player_repository_save.py`
- *... and 31 more nodes in this community*

## Relationships

- [Player](Player.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_inventory_helpers_extended.py](test_inventory_helpers_extended.py.md) (4 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (4 shared connections)
- [test_invite_schemas.py](test_invite_schemas.py.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [migrate_combat_data.py](migrate_combat_data.py.md) (1 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (1 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (1 shared connections)
- [test_party_commands.py](test_party_commands.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository_save.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 125 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*