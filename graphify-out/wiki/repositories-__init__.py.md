# repositories/__init__.py

> 121 nodes

## Key Concepts

- **repositories/__init__.py** (31 connections) — `server/persistence/repositories/__init__.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **models/quest.py** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **asyncio** (11 connections)
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_start_by_trigger_then_abandon()** (9 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_log_abandon_flow()** (9 connections) — `server/tests/integration/test_quest_flow.py`
- **asyncio** (9 connections)
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_str_player_id()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (7 connections)
- *... and 96 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (24 shared connections)
- [get_session_maker](get_session_maker.md) (14 shared connections)
- [QuestService](QuestService.md) (11 shared connections)
- [server/models/__init__.py](server-models-__init__.py.md) (9 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)
- [PlayerSkillRepository](PlayerSkillRepository.md) (4 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)

## Source Files

- `server/models/quest.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 306 (92%)
- INFERRED: 25 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*