# get_session_maker

> 231 nodes

## Key Concepts

- **get_session_maker()** (100 connections) — `server/database.py`
- **DialogueDefinitionRepository** (30 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_dialogue_definition_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **test_spell_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **models/quest.py** (13 connections) — `server/models/quest.py`
- **_row_to_dialogue()** (11 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_row_to_player_spell()** (11 connections) — `server/persistence/repositories/player_spell_repository.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **asyncio** (11 connections)
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **asyncio** (9 connections)
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- *... and 206 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (98 shared connections)
- [Player](Player.md) (21 shared connections)
- [QuestService](QuestService.md) (13 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (12 shared connections)
- [item_instance_persistence_async.py](item_instance_persistence_async.py.md) (9 shared connections)
- [GameBundle](GameBundle.md) (8 shared connections)
- [SkillRepository](SkillRepository.md) (8 shared connections)
- [test_quest_start_by_trigger_then_abandon](test_quest_start_by_trigger_then_abandon.md) (7 shared connections)
- [ContainerRepository](ContainerRepository.md) (7 shared connections)
- [PlayerService](PlayerService.md) (6 shared connections)
- [TargetMatch](TargetMatch.md) (5 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (4 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/game/dialogue/dialogue_service.py`
- `server/models/quest.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/persistence/repositories/emote_repository.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`
- `tools/invite_tools/check_invites.py`

## Audit Trail

- EXTRACTED: 589 (94%)
- INFERRED: 38 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*