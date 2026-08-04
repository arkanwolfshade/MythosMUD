# npc population stats

> 59 nodes

## Key Concepts

- **PlayerInventory** (25 connections) — `server/models/player.py`
- **test_player_related_models.py** (19 connections) — `server/tests/unit/models/test_player_related_models.py`
- **PlayerExploration** (18 connections) — `server/models/player.py`
- **PlayerSkill** (17 connections) — `server/models/player_skill.py`
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
- **Base** (4 connections)
- **._normalize_is_admin()** (4 connections) — `server/persistence/repositories/player_repository_save.py`
- **.execute()** (3 connections) — `server/persistence/repositories/player_repository_save.py`
- **test_player_inventory_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_defaults()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_with_data()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_inventory_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_creation()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- **test_player_exploration_repr()** (3 connections) — `server/tests/unit/models/test_player_related_models.py`
- *... and 34 more nodes in this community*

## Relationships

- [combat models rationale](combat_models_rationale.md) (13 shared connections)
- [player preferences service](player_preferences_service.md) (7 shared connections)
- [world models rationale](world_models_rationale.md) (7 shared connections)
- [player room realtime](player_room_realtime.md) (6 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (6 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (5 shared connections)
- [logging file setup](logging_file_setup.md) (5 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (2 shared connections)
- [effect player repository](effect_player_repository.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (2 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (2 shared connections)

## Source Files

- `server/models/player.py`
- `server/models/player_skill.py`
- `server/persistence/repositories/player_repository_save.py`
- `server/tests/unit/models/test_player_related_models.py`

## Audit Trail

- EXTRACTED: 205 (86%)
- INFERRED: 32 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*