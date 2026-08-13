# get_session_maker

> 113 nodes

## Key Concepts

- **get_session_maker()** (91 connections) — `server/database.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
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
- **.save_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- *... and 88 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (31 shared connections)
- [log_and_raise](log_and_raise.md) (29 shared connections)
- [Player](Player.md) (20 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (8 shared connections)
- [PlayerService](PlayerService.md) (8 shared connections)
- [_container_data_to_dict](_container_data_to_dict.md) (7 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (6 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [retry.py](retry.py.md) (5 shared connections)
- [PlayerSavePreparer](PlayerSavePreparer.md) (4 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (3 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_repository_room.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `tools/invite_tools/check_invites.py`

## Audit Trail

- EXTRACTED: 338 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*