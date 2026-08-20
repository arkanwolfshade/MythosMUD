# PlayerSavePreparer

> 26 nodes

## Key Concepts

- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **.prepare()** (10 connections) — `server/persistence/repositories/player_repository_save.py`
- **._prepare_inventory_payload()** (7 connections) — `server/persistence/repositories/player_repository_save.py`
- **Any** (7 connections)
- **Player** (7 connections)
- **_parse_equipped_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **_parse_inventory_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._ensure_inventory_record()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._normalize_timestamps()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_numeric_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_string_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._normalize_is_admin()** (4 connections) — `server/persistence/repositories/player_repository_save.py`
- **.execute()** (3 connections) — `server/persistence/repositories/player_repository_save.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/player_repository_save.py`
- **datetime** (2 connections)
- **Validate and serialize inventory payload. Returns (inventory_json,…** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Prepare player for upsert: normalize, validate inventory, build params.** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Execute upsert_player procedure with given params.** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Parse inventory from string or list. Raises InventorySchemaValidationError if…** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Parse equipped from string or dict. Raises InventorySchemaValidationError if…** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Prepares Player objects for upsert_player procedure calls. Handles…** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Ensure is_admin is an integer (PostgreSQL requires integer, not boolean).** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Ensure player has inventory_record and update with current payload.** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Normalize last_active, created_at, deleted_at to UTC for procedure call.** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Extract string fields with defaults for upsert_player.** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- *... and 1 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (7 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [validate_inventory_payload](validate_inventory_payload.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository_save.py`

## Audit Trail

- EXTRACTED: 53 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*