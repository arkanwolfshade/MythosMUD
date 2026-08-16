# test_quest_definition_repository.py

> 42 nodes

## Key Concepts

- **test_quest_definition_repository.py** (21 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
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
- **Return quest IDs offered by the given entity (npc or room).** (1 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **Map procedure result row to QuestDefinition model.** (1 connections) — `server/persistence/repositories/quest_definition_repository.py`
- *... and 17 more nodes in this community*

## Relationships

- [Player](Player.md) (11 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [log_and_raise](log_and_raise.md) (3 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [fixtures/integration/__init__.py](fixtures-integration-__init__.py.md) (2 shared connections)
- [SkillService](SkillService.md) (1 shared connections)
- [persistence/repositories/__init__.py](persistence-repositories-__init__.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`

## Audit Trail

- EXTRACTED: 83 (88%)
- INFERRED: 11 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*