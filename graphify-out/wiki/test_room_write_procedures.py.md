# test_room_write_procedures.py

> 32 nodes · cohesion 0.11

## Key Concepts

- **PlayerInventory** (19 connections) — `server/models/player.py`
- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **player_repository_save.py** (11 connections) — `server/persistence/repositories/player_repository_save.py`
- **.prepare()** (10 connections) — `server/persistence/repositories/player_repository_save.py`
- **._prepare_inventory_payload()** (7 connections) — `server/persistence/repositories/player_repository_save.py`
- **Any** (7 connections)
- **Player** (7 connections)
- **.__init__()** (5 connections) — `server/persistence/repositories/player_repository.py`
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
- **Player inventory model for persistent storage of items. This matches the…** (1 connections) — `server/models/player.py`
- **Initialize the player repository. Args: room_cache: Shared room cache for room…** (1 connections) — `server/persistence/repositories/player_repository.py`
- **Player save/upsert helpers for PlayerRepository. Handles inventory validation,…** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Validate and serialize inventory payload. Returns (inventory_json,…** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Prepare player for upsert: normalize, validate inventory, build params.** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Execute upsert_player procedure with given params.** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Parse inventory from string or list. Raises InventorySchemaValidationError if…** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- *... and 7 more nodes in this community*

## Relationships

- [test_connection_event_helpers.py](test_connection_event_helpers.py.md) (8 shared connections)
- [endpoints.py](endpoints.py.md) (5 shared connections)
- [ADR-026: Item Catalog Metadata Contracts](ADR-026-_Item_Catalog_Metadata_Contracts.md) (5 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (3 shared connections)
- [overrides](overrides.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (2 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (1 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_save.py`

## Audit Trail

- EXTRACTED: 76 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*