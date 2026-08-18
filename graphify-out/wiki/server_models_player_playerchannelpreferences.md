# server models player playerchannelpreferences

> 69 nodes

## Key Concepts

- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerInventory** (16 connections) — `server/models/player.py`
- **PlayerSavePreparer** (16 connections) — `server/persistence/repositories/player_repository_save.py`
- **PlayerChannelPreferences** (15 connections) — `server/models/player.py`
- **player_repository_save.py** (12 connections) — `server/persistence/repositories/player_repository_save.py`
- **PlayerExploration** (10 connections) — `server/models/player.py`
- **.prepare()** (10 connections) — `server/persistence/repositories/player_repository_save.py`
- **player_preferences_service.py** (10 connections) — `server/services/player_preferences_service.py`
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
- *... and 44 more nodes in this community*

## Relationships

- [server async persistence](server_async_persistence.md) (10 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (7 shared connections)
- [fixturerequest](fixturerequest.md) (5 shared connections)
- [server schemas shared init](server_schemas_shared_init.md) (5 shared connections)
- [server services player preferences service](server_services_player_preferences_service.md) (4 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server commands channel commands](server_commands_channel_commands.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_save.py`
- `server/services/player_preferences_service.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 134 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*