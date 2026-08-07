# commands shutdown process

> 102 nodes

## Key Concepts

- **get_session_maker()** (97 connections) — `server/database.py`
- **__init__.py** (30 connections) — `server/persistence/repositories/__init__.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestInstanceRepository** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **quest.py** (13 connections) — `server/models/quest.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
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
- *... and 77 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (33 shared connections)
- [add used user](add_used_user.md) (24 shared connections)
- [level curve game](level_curve_game.md) (15 shared connections)
- [quest game service](quest_game_service.md) (11 shared connections)
- [player room realtime](player_room_realtime.md) (10 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (9 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (8 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (8 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (8 shared connections)
- [command commands service](command_commands_service.md) (6 shared connections)
- [lucidity active service](lucidity_active_service.md) (6 shared connections)
- [combat services messaging](combat_services_messaging.md) (6 shared connections)

## Source Files

- `server/database.py`
- `server/models/quest.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`
- `tools/invite_tools/check_invites.py`

## Audit Trail

- EXTRACTED: 523 (94%)
- INFERRED: 32 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*