# Player State Command Factory

> 35 nodes · cohesion 0.06

## Key Concepts

- **PlayerStateCommandFactory** (18 connections) — `server/utils/command_factories_player_state.py`
- **.create_journal_command()** (4 connections) — `server/utils/command_factories_player_state.py`
- **.create_quests_command()** (4 connections) — `server/utils/command_factories_player_state.py`
- **.create_quit_command()** (4 connections) — `server/utils/command_factories_player_state.py`
- **.create_rest_command()** (4 connections) — `server/utils/command_factories_player_state.py`
- **.create_skills_command()** (4 connections) — `server/utils/command_factories_player_state.py`
- **.create_status_command()** (4 connections) — `server/utils/command_factories_player_state.py`
- **.create_time_command()** (4 connections) — `server/utils/command_factories_player_state.py`
- **.create_whoami_command()** (4 connections) — `server/utils/command_factories_player_state.py`
- **.create_logout_command()** (3 connections) — `server/utils/command_factories_player_state.py`
- **.create_quest_command()** (3 connections) — `server/utils/command_factories_player_state.py`
- **.create_who_command()** (3 connections) — `server/utils/command_factories_player_state.py`
- **JournalCommand** (1 connections) — `server/utils/command_factories_player_state.py`
- **LogoutCommand** (1 connections) — `server/utils/command_factories_player_state.py`
- **QuestCommand** (1 connections) — `server/utils/command_factories_player_state.py`
- **QuestsCommand** (1 connections) — `server/utils/command_factories_player_state.py`
- **QuitCommand** (1 connections) — `server/utils/command_factories_player_state.py`
- **RestCommand** (1 connections) — `server/utils/command_factories_player_state.py`
- **SkillsCommand** (1 connections) — `server/utils/command_factories_player_state.py`
- **StatusCommand** (1 connections) — `server/utils/command_factories_player_state.py`
- **TimeCommand** (1 connections) — `server/utils/command_factories_player_state.py`
- **Create JournalCommand from arguments (quest log view).** (1 connections) — `server/utils/command_factories_player_state.py`
- **Create QuestsCommand from arguments (alias of journal).** (1 connections) — `server/utils/command_factories_player_state.py`
- **Create QuestCommand from arguments (e.g. abandon <quest name>).** (1 connections) — `server/utils/command_factories_player_state.py`
- **Factory class for creating player state command objects.** (1 connections) — `server/utils/command_factories_player_state.py`
- *... and 10 more nodes in this community*

## Relationships

- [[NPC Admin API]] (9 shared connections)
- [[Communication Command Classes]] (2 shared connections)
- [[Command Factory Creators]] (2 shared connections)
- [[Player State Factories]] (1 shared connections)

## Source Files

- `server/utils/command_factories_player_state.py`

## Audit Trail

- EXTRACTED: 80 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
