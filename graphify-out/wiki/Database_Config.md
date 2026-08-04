# Database Config

> 136 nodes

## Key Concepts

- **get_session_maker()** (97 connections) — `server/database.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestInstanceRepository** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_flow.py** (15 connections) — `server/tests/integration/test_quest_flow.py`
- **quest.py** (13 connections) — `server/models/quest.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
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
- *... and 111 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (63 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (13 shared connections)
- [game models enums](game_models_enums.md) (12 shared connections)
- [world models rationale](world_models_rationale.md) (9 shared connections)
- [quest game service](quest_game_service.md) (9 shared connections)
- [persistence container item](persistence_container_item.md) (8 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (7 shared connections)
- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (6 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (4 shared connections)
- [command commands service](command_commands_service.md) (4 shared connections)
- [effect player repository](effect_player_repository.md) (4 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/models/quest.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`
- `tools/invite_tools/check_invites.py`

## Audit Trail

- EXTRACTED: 597 (94%)
- INFERRED: 35 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*