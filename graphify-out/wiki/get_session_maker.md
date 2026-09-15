# get_session_maker

> 153 nodes

## Key Concepts

- **get_session_maker()** (102 connections) — `server/database.py`
- **PlayerRepository** (32 connections) — `server/persistence/repositories/player_repository.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **PlayerSpell** (19 connections) — `server/models/player_spells.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **retry_with_backoff()** (14 connections) — `server/utils/retry.py`
- **test_spell_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **test_player_skill_repository.py** (12 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **_row_to_player_spell()** (11 connections) — `server/persistence/repositories/player_spell_repository.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_by_player_id()** (7 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.get_player_spell()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.get_player_spells()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.learn_spell()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.record_spell_cast()** (7 connections) — `server/persistence/repositories/player_spell_repository.py`
- *... and 128 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (84 shared connections)
- [Player](Player.md) (14 shared connections)
- [DatabaseManager](DatabaseManager.md) (11 shared connections)
- [PlayerService](PlayerService.md) (10 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (8 shared connections)
- [ContainerRepository](ContainerRepository.md) (7 shared connections)
- [retry.py](retry.py.md) (7 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (5 shared connections)
- [PlayerEffectRepository](PlayerEffectRepository.md) (5 shared connections)
- [Any](Any.md) (5 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (4 shared connections)
- [SkillRepository](SkillRepository.md) (4 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/models/player_spells.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/unit/models/test_player_spells.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`
- `server/utils/retry.py`
- `tools/invite_tools/check_invites.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 430 (96%)
- INFERRED: 20 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*