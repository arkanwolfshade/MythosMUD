# NPC Definition CRUD

> 54 nodes

## Key Concepts

- **InventorySchemaValidationError** (20 connections) — `server/schemas/shared/inventory_schema.py`
- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
- **player_repository_save.py** (11 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_inventory_schema.py** (11 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **.prepare()** (10 connections) — `server/persistence/repositories/player_repository_save.py`
- **validate_inventory_items()** (9 connections) — `server/schemas/shared/inventory_schema.py`
- **Any** (7 connections)
- **Player** (7 connections)
- **._prepare_inventory_payload()** (7 connections) — `server/persistence/repositories/player_repository_save.py`
- **inventory_schema.py** (7 connections) — `server/schemas/shared/inventory_schema.py`
- **_parse_inventory_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **_parse_equipped_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._ensure_inventory_record()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._normalize_timestamps()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_string_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_numeric_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **_build_validator()** (5 connections) — `server/schemas/shared/inventory_schema.py`
- **._normalize_is_admin()** (4 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_validate_inventory_payload_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_invalid_inventory()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_items_invalid_quantity()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **.execute()** (3 connections) — `server/persistence/repositories/player_repository_save.py`
- **Any** (3 connections)
- *... and 29 more nodes in this community*

## Relationships

- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (4 shared connections)
- [Dependency Upgrade Report](Dependency_Upgrade_Report.md) (3 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (2 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (2 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (1 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository_save.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 203 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*