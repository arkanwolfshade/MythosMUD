# NPC Definition CRUD

> 62 nodes

## Key Concepts

- **InventorySchemaValidationError** (20 connections) — `server/schemas/shared/inventory_schema.py`
- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
- **__init__.py** (12 connections) — `server/schemas/shared/__init__.py`
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
- **.__init__()** (4 connections) — `server/persistence/repositories/player_repository.py`
- **._normalize_is_admin()** (4 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_persist_player_error()** (4 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **test_persist_player_validation_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_validate_inventory_payload_missing_required()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- **test_validate_inventory_payload_invalid_inventory()** (4 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- *... and 37 more nodes in this community*

## Relationships

- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (8 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (5 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (3 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (2 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_save.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 231 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*