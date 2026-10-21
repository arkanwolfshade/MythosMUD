# endpoints.py

> 332 nodes · cohesion 0.01

## Key Concepts

- **log_and_raise()** (195 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (111 connections) — `server/database.py`
- **session()** (39 connections) — `server/tests/unit/game/items/test_item_effects.py`
- **PlayerRepository** (35 connections) — `server/persistence/repositories/player_repository.py`
- **repositories/__init__.py** (31 connections) — `server/persistence/repositories/__init__.py`
- **DialogueDefinitionRepository** (30 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **player_spell_repository.py** (21 connections) — `server/persistence/repositories/player_spell_repository.py`
- **dialogue_definition_repository.py** (20 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_dialogue_definition_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **_container_data_to_dict()** (14 connections) — `server/persistence/repositories/container_repository.py`
- **models/quest.py** (13 connections) — `server/models/quest.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **DialogueDefinition** (12 connections) — `server/models/dialogue.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- *... and 307 more nodes in this community*

## Relationships

- [LoggingPatternLinter](LoggingPatternLinter.md) (53 shared connections)
- [AttributeError](AttributeError.md) (31 shared connections)
- [.profession_to_dict](profession_to_dict.md) (27 shared connections)
- [test_event_publisher.py](test_event_publisher.py.md) (25 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (23 shared connections)
- [Room](Room.md) (16 shared connections)
- [command_result_text](command_result_text.md) (15 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (15 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (12 shared connections)
- [command_guards.py](command_guards.py.md) (12 shared connections)
- [test_inventory_item_matching.py](test_inventory_item_matching.py.md) (11 shared connections)
- [test_aggression.py](test_aggression.py.md) (10 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/game/dialogue/dialogue_service.py`
- `server/models/dialogue.py`
- `server/models/quest.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/container_repository.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/persistence/repositories/emote_repository.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/item_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_mute_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/persistence/repositories/skill_repository.py`

## Audit Trail

- EXTRACTED: 1030 (93%)
- INFERRED: 83 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*