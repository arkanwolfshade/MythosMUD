# PlayerInventory

> 32 nodes

## Key Concepts

- **PlayerInventory** (16 connections) — `server/models/player.py`
- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **player_repository_save.py** (11 connections) — `server/persistence/repositories/player_repository_save.py`
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
- **.__init__()** (4 connections) — `server/persistence/repositories/player_repository.py`
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

- [test_player_related_models.py](test_player_related_models.py.md) (7 shared connections)
- [get_session_maker](get_session_maker.md) (5 shared connections)
- [Player](Player.md) (5 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (5 shared connections)
- [server/models/__init__.py](server-models-__init__.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_save.py`

## Audit Trail

- EXTRACTED: 74 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*