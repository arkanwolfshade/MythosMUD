# server game dialogue dialogue service

> 40 nodes

## Key Concepts

- **DialogueDefinitionRepository** (30 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_definition_repository.py** (21 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
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
- **.__init__()** (2 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_definition_dict_coerces_keys()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- *... and 15 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (6 shared connections)
- [server game skill service](server_game_skill_service.md) (6 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (5 shared connections)
- [server game dialogue dialogue service](server_game_dialogue_dialogue_service.md) (3 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 96 (87%)
- INFERRED: 14 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*