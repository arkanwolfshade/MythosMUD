# Server Persistence

> 147 nodes

## Key Concepts

- **DatabaseError** (429 connections) — `server/exceptions.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **ExperienceRepository** (16 connections) — `server/persistence/repositories/experience_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **QuestInstanceRepository** (16 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **QuestInstance** (14 connections) — `server/models/quest.py`
- **QuestDefinitionRepository** (14 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest.py** (13 connections) — `server/models/quest.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.get_by_player_and_quest()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.get_by_player_id()** (8 connections) — `server/persistence/repositories/player_skill_repository.py`
- **UUID** (8 connections)
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_state_and_progress()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.update_player_xp()** (7 connections) — `server/persistence/repositories/experience_repository.py`
- **.get_by_id()** (7 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **.get_by_name()** (7 connections) — `server/persistence/repositories/quest_definition_repository.py`
- *... and 122 more nodes in this community*

## Relationships

- [Server Persistence (3)](Server_Persistence_%283%29.md) (46 shared connections)
- [Server Admin](Server_Admin.md) (33 shared connections)
- [Server Commands](Server_Commands.md) (29 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (20 shared connections)
- [Server Services](Server_Services.md) (17 shared connections)
- [Server Api](Server_Api.md) (16 shared connections)
- [Server Container Persistence](Server_Container_Persistence.md) (15 shared connections)
- [Server Persistence (2)](Server_Persistence_%282%29.md) (14 shared connections)
- [Server Persistence (5)](Server_Persistence_%285%29.md) (12 shared connections)
- [Server Game (9)](Server_Game_%289%29.md) (12 shared connections)
- [Server Infrastructure (2)](Server_Infrastructure_%282%29.md) (11 shared connections)
- [Server Realtime (3)](Server_Realtime_%283%29.md) (11 shared connections)

## Source Files

- `server/exceptions.py`
- `server/models/quest.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/structured_logging/logging_processors.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 660 (65%)
- INFERRED: 348 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*