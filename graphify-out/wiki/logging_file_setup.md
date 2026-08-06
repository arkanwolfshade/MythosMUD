# logging file setup

> 30 nodes

## Key Concepts

- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **player_repository_save.py** (11 connections) — `server/persistence/repositories/player_repository_save.py`
- **.prepare()** (10 connections) — `server/persistence/repositories/player_repository_save.py`
- **Any** (7 connections)
- **Player** (7 connections)
- **._prepare_inventory_payload()** (7 connections) — `server/persistence/repositories/player_repository_save.py`
- **_parse_inventory_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **_parse_equipped_raw()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._ensure_inventory_record()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._normalize_timestamps()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_string_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **._upsert_numeric_defaults()** (5 connections) — `server/persistence/repositories/player_repository_save.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/player_repository.py`
- **._normalize_is_admin()** (4 connections) — `server/persistence/repositories/player_repository_save.py`
- **.execute()** (3 connections) — `server/persistence/repositories/player_repository_save.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/player_repository_save.py`
- **datetime** (2 connections)
- **Initialize the player repository.          Args:             room_cache: Shared** (1 connections) — `server/persistence/repositories/player_repository.py`
- **Player save/upsert helpers for PlayerRepository.  Handles inventory validation,** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Parse inventory from string or list. Raises InventorySchemaValidationError if in** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Parse equipped from string or dict. Raises InventorySchemaValidationError if inv** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Prepares Player objects for upsert_player procedure calls.      Handles normaliz** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Ensure is_admin is an integer (PostgreSQL requires integer, not boolean).** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Ensure player has inventory_record and update with current payload.** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- **Normalize last_active, created_at, deleted_at to UTC for procedure call.** (1 connections) — `server/persistence/repositories/player_repository_save.py`
- *... and 5 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [player room realtime](player_room_realtime.md) (4 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)
- [command parser helpers](command_parser_helpers.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_save.py`

## Audit Trail

- EXTRACTED: 113 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*