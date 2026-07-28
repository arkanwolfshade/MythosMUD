# Player Save Preparer

> 63 nodes · cohesion 0.05

## Key Concepts

- **PlayerInventory** (25 connections) — `server/models/player.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
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
- **Base** (4 connections)
- **._normalize_is_admin()** (4 connections) — `server/persistence/repositories/player_repository_save.py`
- **.execute()** (3 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_player_channel_preferences_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_channel_preferences_with_muted_channels()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_multiple_rooms()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- *... and 38 more nodes in this community*

## Relationships

- [Event Bus Serialization](Event_Bus_Serialization.md) (11 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (6 shared connections)
- [Player Related Models](Player_Related_Models.md) (6 shared connections)
- [Commands Admin Shutdown](Commands_Admin_Shutdown.md) (5 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (4 shared connections)
- [Services Lucidity Repository](Services_Lucidity_Repository.md) (4 shared connections)
- [Metadata Npc](Metadata_Npc.md) (2 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (2 shared connections)
- [Player Death Service Tests](Player_Death_Service_Tests.md) (2 shared connections)
- [Combat Attack Flow](Combat_Attack_Flow.md) (2 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/models/player.py`
- `server/persistence/repositories/player_repository_save.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 208 (89%)
- INFERRED: 25 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*