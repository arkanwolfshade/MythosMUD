# test_player_related_models.py

> 65 nodes

## Key Concepts

- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerInventory** (16 connections) — `server/models/player.py`
- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **player_repository_save.py** (11 connections) — `server/persistence/repositories/player_repository_save.py`
- **PlayerExploration** (10 connections) — `server/models/player.py`
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
- **Base** (4 connections)
- **.execute()** (3 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_player_channel_preferences_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_table_name()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_with_muted_channels()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- *... and 40 more nodes in this community*

## Relationships

- [models/player.py](models-player.py.md) (15 shared connections)
- [DatabaseError](DatabaseError.md) (6 shared connections)
- [Player](Player.md) (3 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (3 shared connections)
- [schemas/shared/__init__.py](schemas-shared-__init__.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_save.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 119 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*