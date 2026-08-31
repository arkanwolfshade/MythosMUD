# get_session_maker

> 73 nodes

## Key Concepts

- **get_session_maker()** (100 connections) — `server/database.py`
- **PlayerRepository** (30 connections) — `server/persistence/repositories/player_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **check_invites.py** (7 connections) — `tools/invite_tools/check_invites.py`
- **.save_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.update_player_last_active()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **UUID** (6 connections)
- **.delete_player()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.save_players()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.soft_delete_player()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **main()** (5 connections) — `tools/invite_tools/check_invites.py`
- **get_invite_codes.py** (5 connections) — `e2e-tests/load-tests/get_invite_codes.py`
- **Any** (5 connections)
- **check_invite_status.py** (5 connections) — `server/scripts/check_invite_status.py`
- **list_active_invites.py** (5 connections) — `server/scripts/list_active_invites.py`
- **get_10_active_invites()** (4 connections) — `e2e-tests/load-tests/get_invite_codes.py`
- *... and 48 more nodes in this community*

## Relationships

- [sqlalchemy.md](sqlalchemy.md.md) (26 shared connections)
- [DatabaseError](DatabaseError.md) (13 shared connections)
- [log_and_raise](log_and_raise.md) (13 shared connections)
- [ValidationError](ValidationError.md) (11 shared connections)
- [ContainerData](ContainerData.md) (9 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (6 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (6 shared connections)
- [repositories/__init__.py](repositories-__init__.py.md) (5 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (5 shared connections)
- [test_player_spell_repository.py](test_player_spell_repository.py.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (4 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `tools/invite_tools/check_invites.py`

## Audit Trail

- EXTRACTED: 248 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*