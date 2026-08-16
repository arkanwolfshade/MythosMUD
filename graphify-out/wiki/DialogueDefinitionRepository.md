# DialogueDefinitionRepository

> 45 nodes

## Key Concepts

- **DialogueDefinitionRepository** (30 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **dialogue_definition_repository.py** (21 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_definition_repository.py** (21 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **DialogueDefinition** (12 connections) — `server/models/dialogue.py`
- **_row_to_dialogue()** (11 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **asyncio** (8 connections)
- **_as_dialogue_row()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_id()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_npc_definition_id()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.list_all()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.upsert()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_definition_dict()** (6 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_mock_session_with_rows()** (6 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **_DialogueRow** (5 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.delete()** (4 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_get_by_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_id_not_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_npc_definition_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_list_all_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_list_all_success()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_upsert_success()** (4 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_delete_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_delete_true()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **.__init__()** (2 connections) — `server/game/dialogue/dialogue_service.py`
- *... and 20 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [log_and_raise](log_and_raise.md) (7 shared connections)
- [get_session_maker](get_session_maker.md) (6 shared connections)
- [Player](Player.md) (5 shared connections)
- [DialogueService](DialogueService.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [persistence/repositories/__init__.py](persistence-repositories-__init__.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [database.py](database.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/models/dialogue.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 115 (88%)
- INFERRED: 15 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*