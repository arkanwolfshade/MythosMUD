# Cursor Plans Disconnect

> 80 nodes

## Key Concepts

- **test_command_factories_player_state.py** (27 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **PlayerStateCommandFactory** (17 connections) — `server/utils/command_factories_player_state.py`
- **RestCommand** (6 connections) — `server/models/command_player_state.py`
- **SkillsCommand** (6 connections) — `server/models/command_utility.py`
- **JournalCommand** (6 connections) — `server/models/command_utility.py`
- **QuestsCommand** (6 connections) — `server/models/command_utility.py`
- **QuestCommand** (6 connections) — `server/models/command_utility.py`
- **.create_status_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_time_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_whoami_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_quit_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_rest_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_skills_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_journal_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_quests_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_who_command()** (5 connections) — `server/utils/command_factories_player_state.py`
- **.create_logout_command()** (5 connections) — `server/utils/command_factories_player_state.py`
- **.create_quest_command()** (5 connections) — `server/utils/command_factories_player_state.py`
- **test_create_status_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_whoami_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_time_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_quit_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_rest_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_skills_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_create_journal_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- *... and 55 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (9 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (9 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (8 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (8 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (6 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (5 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (3 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (1 shared connections)

## Source Files

- `server/models/command_player_state.py`
- `server/models/command_utility.py`
- `server/tests/unit/utils/test_command_factories_player_state.py`
- `server/utils/command_factories_player_state.py`

## Audit Trail

- EXTRACTED: 232 (92%)
- INFERRED: 19 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*