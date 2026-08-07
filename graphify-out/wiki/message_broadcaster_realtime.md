# message broadcaster realtime

> 43 nodes

## Key Concepts

- **DialogueDefinitionRepository** (32 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **dialogue_definition_repository.py** (20 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_definition_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **DialogueDefinition** (13 connections) — `server/models/dialogue.py`
- **_row_to_dialogue()** (11 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.list_all()** (8 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_id()** (8 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.get_by_npc_definition_id()** (8 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **.upsert()** (8 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_DialogueRow** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_as_dialogue_row()** (7 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_definition_dict()** (6 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **_mock_session_with_rows()** (6 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **.delete()** (5 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_list_all_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_list_all_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_id_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_get_by_npc_definition_id_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_upsert_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **.__init__()** (2 connections) — `server/game/dialogue/dialogue_service.py`
- **.__init__()** (2 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_definition_dict_non_dict()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_definition_dict_coerces_keys()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_row_to_dialogue()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- *... and 18 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (8 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (7 shared connections)
- [add used user](add_used_user.md) (7 shared connections)
- [dialogue service game](dialogue_service_game.md) (6 shared connections)
- [player room realtime](player_room_realtime.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (1 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/models/dialogue.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 192 (92%)
- INFERRED: 16 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*