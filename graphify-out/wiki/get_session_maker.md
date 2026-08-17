# get_session_maker

> 216 nodes

## Key Concepts

- **get_session_maker()** (97 connections) — `server/database.py`
- **PlayerRepository** (30 connections) — `server/persistence/repositories/player_repository.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **test_experience_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_skill_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **retry_with_backoff()** (14 connections) — `server/utils/retry.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **test_player_skill_repository.py** (13 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **_row_to_player_spell()** (11 connections) — `server/persistence/repositories/player_spell_repository.py`
- **test_skill_use_log_repository.py** (11 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **asyncio** (10 connections)
- **.get_active_effects_for_player()** (9 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **_row_to_skill()** (9 connections) — `server/persistence/repositories/skill_repository.py`
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- *... and 191 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (127 shared connections)
- [pytest.md](pytest.md.md) (34 shared connections)
- [ContainerRepository](ContainerRepository.md) (8 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (6 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (5 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (5 shared connections)
- [item_instance_persistence_async.py](item_instance_persistence_async.py.md) (5 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (5 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (5 shared connections)
- [User](User.md) (4 shared connections)
- [bundles/game.py](bundles-game.py.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/async_persistence.py`
- `server/database.py`
- `server/game/mechanics.py`
- `server/game/skill_service.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 554 (89%)
- INFERRED: 65 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*