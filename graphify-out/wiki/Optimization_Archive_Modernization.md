# Optimization Archive Modernization

> 112 nodes

## Key Concepts

- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **quest.py** (13 connections) — `server/models/quest.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **.create()** (11 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **.get_by_player_and_quest()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (8 connections)
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.get_by_id()** (7 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **.get_by_name()** (7 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **_str_player_id()** (7 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_start_log_abandon_flow()** (7 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_by_trigger_then_abandon()** (7 connections) — `server/tests/integration/test_quest_flow.py`
- **QuestOffer** (6 connections) — `server/models/quest.py`
- *... and 87 more nodes in this community*

## Relationships

- [Schemas Maps Map](Schemas_Maps_Map.md) (53 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (10 shared connections)
- [Quest Service Core](Quest_Service_Core.md) (9 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (6 shared connections)
- [Container Persistence Layer](Container_Persistence_Layer.md) (3 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)

## Source Files

- `server/models/quest.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 445 (93%)
- INFERRED: 36 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*