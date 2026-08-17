# e2e tests load tests get

> 195 nodes

## Key Concepts

- **get_session_maker()** (97 connections) — `server/database.py`
- **test_quest_instance_repository.py** (23 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **test_quest_definition_repository.py** (21 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **quest_instance_repository.py** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_flow.py** (17 connections) — `server/tests/integration/test_quest_flow.py`
- **._initialize_database()** (15 connections) — `server/database.py`
- **models/quest.py** (14 connections) — `server/models/quest.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **_make_session_context()** (11 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **asyncio** (11 connections)
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_start_by_trigger_then_abandon()** (10 connections) — `server/tests/integration/test_quest_flow.py`
- **test_quest_start_log_abandon_flow()** (10 connections) — `server/tests/integration/test_quest_flow.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **asyncio** (9 connections)
- **_create_engine_or_raise()** (8 connections) — `server/database.py`
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- *... and 170 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (82 shared connections)
- [server game skill service](server_game_skill_service.md) (19 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (12 shared connections)
- [server models player playerchannelpreferences](server_models_player_playerchannelpreferences.md) (12 shared connections)
- [server game quest quest service](server_game_quest_quest_service.md) (10 shared connections)
- [server persistence container create params](server_persistence_container_create_params.md) (8 shared connections)
- [server database databasemanager](server_database_databasemanager.md) (6 shared connections)
- [server game dialogue dialogue service](server_game_dialogue_dialogue_service.md) (5 shared connections)
- [server game skill service skillservice](server_game_skill_service_skillservice.md) (5 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (4 shared connections)
- [server async persistence asyncpersistencelayer create](server_async_persistence_asyncpersistencelayer_create.md) (4 shared connections)
- [server database close db](server_database_close_db.md) (3 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/container/bundles/game.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/models/quest.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`
- `server/tests/unit/persistence/test_quest_definition_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`
- `tools/invite_tools/check_invites.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 513 (94%)
- INFERRED: 31 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*