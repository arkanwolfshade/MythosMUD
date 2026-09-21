# DatabaseError

> 374 nodes

## Key Concepts

- **DatabaseError** (254 connections) — `server/exceptions.py`
- **log_and_raise()** (192 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (102 connections) — `server/database.py`
- **database.py** (85 connections) — `server/database.py`
- **error_logging.py** (61 connections) — `server/utils/error_logging.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **PlayerRepository** (32 connections) — `server/persistence/repositories/player_repository.py`
- **repositories/__init__.py** (31 connections) — `server/persistence/repositories/__init__.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **player_spell_repository.py** (21 connections) — `server/persistence/repositories/player_spell_repository.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **dialogue_definition_repository.py** (20 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **PlayerSpell** (19 connections) — `server/models/player_spells.py`
- **experience_repository.py** (19 connections) — `server/persistence/repositories/experience_repository.py`
- **player_skill_repository.py** (19 connections) — `server/persistence/repositories/player_skill_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **profession_repository.py** (18 connections) — `server/persistence/repositories/profession_repository.py`
- **test_profession_repository.py** (18 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- *... and 349 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (73 shared connections)
- [models/player.py](models-player.py.md) (34 shared connections)
- [test_skill_service.py](test_skill_service.py.md) (30 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (26 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (21 shared connections)
- [Player](Player.md) (20 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (17 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (16 shared connections)
- [container_persistence.py](container_persistence.py.md) (14 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (14 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (14 shared connections)
- [container_query_helpers_async.py](container_query_helpers_async.py.md) (13 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/container/bundles/game.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/exceptions.py`
- `server/game/skill_service.py`
- `server/models/dialogue.py`
- `server/models/player_spells.py`
- `server/models/quest.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/persistence/repositories/emote_repository.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`

## Audit Trail

- EXTRACTED: 1387 (89%)
- INFERRED: 171 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*