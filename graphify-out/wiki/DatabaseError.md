# DatabaseError

> 269 nodes · cohesion 0.02

## Key Concepts

- **DatabaseError** (432 connections) — `server/exceptions.py`
- **log_and_raise()** (164 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **error_logging.py** (55 connections) — `server/utils/error_logging.py`
- **PlayerSpellRepository** (36 connections) — `server/persistence/repositories/player_spell_repository.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **__init__.py** (28 connections) — `server/persistence/repositories/__init__.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **PlayerSpell** (23 connections) — `server/models/player_spells.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **player_spell_repository.py** (20 connections) — `server/persistence/repositories/player_spell_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestInstanceRepository** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **profession_repository.py** (17 connections) — `server/persistence/repositories/profession_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **item_instance_persistence.py** (14 connections) — `server/persistence/item_instance_persistence.py`
- **quest.py** (13 connections) — `server/models/quest.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **Player** (13 connections)
- **skill_use_log_repository.py** (13 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- *... and 244 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (64 shared connections)
- [__init__.py](__init__.py.md) (61 shared connections)
- [container_persistence.py](container_persistence.py.md) (47 shared connections)
- [.get_instance](get_instance.md) (35 shared connections)
- [container_persistence_async.py](container_persistence_async.py.md) (31 shared connections)
- [Player](Player.md) (28 shared connections)
- [MythosMUDError](MythosMUDError.md) (27 shared connections)
- [test_container_persistence.py](test_container_persistence.py.md) (23 shared connections)
- [exceptions.py](exceptions.py.md) (22 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (21 shared connections)
- [MovementService](MovementService.md) (19 shared connections)
- [AliasStorage](AliasStorage.md) (16 shared connections)

## Source Files

- `server/database.py`
- `server/exceptions.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/models/player_spells.py`
- `server/models/quest.py`
- `server/persistence/item_instance_persistence.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/profession_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/integration/test_quest_flow.py`

## Audit Trail

- EXTRACTED: 1515 (78%)
- INFERRED: 422 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*