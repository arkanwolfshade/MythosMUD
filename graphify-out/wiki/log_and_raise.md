# log_and_raise

> 150 nodes

## Key Concepts

- **log_and_raise()** (174 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **_row_to_player_spell()** (9 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **validate_and_fix_player_room()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room_with_persistence()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **.get_by_player_id()** (7 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.get_player_spell()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.get_player_spells()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.learn_spell()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.record_spell_cast()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.update_mastery()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **player_repository_room.py** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- *... and 125 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (38 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (24 shared connections)
- [Player](Player.md) (21 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (20 shared connections)
- [magic_service.py](magic_service.py.md) (14 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (14 shared connections)
- [database.py](database.py.md) (13 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (10 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [DatabaseManager](DatabaseManager.md) (8 shared connections)
- [WearableContainerService](WearableContainerService.md) (8 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/game/mechanics.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_repository_room.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/utils/error_logging.py`
- `tools/invite_tools/check_invites.py`

## Audit Trail

- EXTRACTED: 819 (100%)
- INFERRED: 4 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*