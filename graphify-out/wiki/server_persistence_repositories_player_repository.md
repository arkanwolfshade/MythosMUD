# server persistence repositories player repository

> 54 nodes

## Key Concepts

- **InventorySchemaValidationError** (20 connections) — `server/schemas/shared/inventory_schema.py`
- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **schemas/shared/__init__.py** (16 connections) — `server/schemas/shared/__init__.py`
- **validate_inventory_payload()** (13 connections) — `server/schemas/shared/inventory_schema.py`
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
- **test_validate_inventory_items_valid()** (3 connections) — `server/tests/unit/schemas/test_inventory_schema.py`
- *... and 29 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [aliasrecord](aliasrecord.md) (8 shared connections)
- [server models player playerchannelpreferences](server_models_player_playerchannelpreferences.md) (4 shared connections)
- [get current active user](get_current_active_user.md) (3 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (2 shared connections)
- [draft7validator](draft7validator.md) (1 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (1 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (1 shared connections)
- [server commands follow commands](server_commands_follow_commands.md) (1 shared connections)
- [server commands party commands](server_commands_party_commands.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository_save.py`
- `server/schemas/shared/__init__.py`
- `server/schemas/shared/inventory_schema.py`
- `server/tests/unit/schemas/test_inventory_schema.py`

## Audit Trail

- EXTRACTED: 119 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*