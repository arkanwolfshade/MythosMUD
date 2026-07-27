# Quest Flow Integration

> 52 nodes · cohesion 0.06

## Key Concepts

- **QuestDefinitionRepository** (21 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_definition_repository.py** (18 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_quest_flow.py** (12 connections) — `server/tests/integration/test_quest_flow.py`
- **QuestDefinition** (12 connections) — `server/models/quest.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_quest_start_by_trigger_then_abandon()** (7 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_log_abandon_flow()** (7 connections) — `server/tests/integration/test_quest_flow.py`
- **_row_to_quest_definition()** (7 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **.get_by_id()** (6 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **.get_by_name()** (6 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **QuestDefinition** (5 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **_make_shared_session_factory()** (4 connections) — `server/tests/integration/test_quest_flow.py`
- **_row_for_quest_definition()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_success()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_success()** (4 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **.list_quest_ids_offered_by()** (4 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_database_error()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_database_error()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_get_by_name_not_found()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_database_error()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_empty()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **test_list_quest_ids_offered_by_success()** (3 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **Any** (3 connections) — `server/persistence/repositories/quest_definition_repository.py`
- *... and 27 more nodes in this community*

## Relationships

- [[NPC Admin API]] (17 shared connections)
- [[Game Service Bundle]] (7 shared connections)
- [[SQLAlchemy Model Base]] (6 shared connections)
- [[Quest Service Core]] (3 shared connections)
- [[Quest Instance Repository]] (3 shared connections)
- [[Integration DB Fixtures]] (3 shared connections)
- [[Game State Provider Tests]] (1 shared connections)
- [[NPC Definition CRUD]] (1 shared connections)

## Source Files

- `server/models/quest.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/services/npc_service_models.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 174 (91%)
- INFERRED: 17 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
