# test_quest_definition_repository.py

> 44 nodes

## Key Concepts

- **test_quest_definition_repository.py** (21 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **asyncio** (9 connections)
- **.get_by_id()** (6 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **.get_by_name()** (6 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **_row_to_quest_definition()** (6 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_get_by_id_database_error()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_success()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_database_error()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_success()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_database_error()** (5 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **.list_quest_ids_offered_by()** (4 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **mock_quest_definition()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_definition_repository()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **_row_for_quest_definition()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_not_found()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_not_found()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_empty()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_success()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **fixture** (2 connections)
- **Any** (1 connections)
- **Quest template: id (PK), definition JSONB, timestamps.** (1 connections) — `server/models/quest.py`
- *... and 19 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (5 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [test_quest_start_by_trigger_then_abandon](test_quest_start_by_trigger_then_abandon.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)

## Source Files

- `server/models/quest.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`

## Audit Trail

- EXTRACTED: 89 (88%)
- INFERRED: 12 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*