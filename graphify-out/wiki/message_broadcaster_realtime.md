# message broadcaster realtime

> 39 nodes

## Key Concepts

- **DialogueDefinitionRepository** (32 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
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
- **repo()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_delete_true()** (2 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- *... and 14 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (20 shared connections)
- [player preferences services](player_preferences_services.md) (6 shared connections)
- [dialogue service game](dialogue_service_game.md) (5 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [world models rationale](world_models_rationale.md) (3 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/models/dialogue.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 166 (92%)
- INFERRED: 15 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*