# Optimization Archive Modernization

> 259 nodes

## Key Concepts

- **DatabaseError** (434 connections) — `server/exceptions.py`
- **log_and_raise()** (174 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **ExperienceRepository** (16 connections) — `server/persistence/repositories/experience_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **experience_repository.py** (15 connections) — `server/persistence/repositories/experience_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **quest.py** (13 connections) — `server/models/quest.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **Player** (13 connections)
- **skill_use_log_repository.py** (13 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **.create()** (11 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- *... and 234 more nodes in this community*

## Relationships

- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (52 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (52 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (43 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (42 shared connections)
- [Client Event Store](Client_Event_Store.md) (28 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (26 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (22 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (22 shared connections)
- [Player State Factories](Player_State_Factories.md) (18 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (17 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (15 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (15 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `monitoring/webhook-receiver.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/mechanics.py`
- `server/models/quest.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`

## Audit Trail

- EXTRACTED: 1370 (78%)
- INFERRED: 395 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*