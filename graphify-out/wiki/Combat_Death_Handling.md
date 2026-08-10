# Combat Death Handling

> 34 nodes

## Key Concepts

- **quest_commands.py** (32 connections) — `server/commands/quest_commands.py`
- **handle_quest_command()** (21 connections) — `server/commands/quest_commands.py`
- **Any** (17 connections)
- **handle_journal_command()** (15 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **_handle_quest_npc_sub()** (8 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **UUID** (6 connections)
- **_quest_command_ready()** (6 connections) — `server/commands/quest_commands.py`
- **_get_container_and_persistence()** (5 connections) — `server/commands/quest_commands.py`
- **_format_one_quest_entry()** (5 connections) — `server/commands/quest_commands.py`
- **_format_quest_log()** (5 connections) — `server/commands/quest_commands.py`
- **_handle_quest_abandon()** (5 connections) — `server/commands/quest_commands.py`
- **_parse_quest_subcommand()** (4 connections) — `server/commands/quest_commands.py`
- **_format_goal_line()** (4 connections) — `server/commands/quest_commands.py`
- **_npc_definition_id()** (4 connections) — `server/commands/quest_commands.py`
- **_format_quest_action_results()** (4 connections) — `server/commands/quest_commands.py`
- **Quest commands: journal / quests (quest log), quest abandon/ask/turnin.  Returns** (1 connections) — `server/commands/quest_commands.py`
- **Get QuestService from request app container, or None if unavailable.** (1 connections) — `server/commands/quest_commands.py`
- **Get container and async_persistence from request, or None.** (1 connections) — `server/commands/quest_commands.py`
- **Extract player_id from player object as UUID, or None.** (1 connections) — `server/commands/quest_commands.py`
- **Parse quest subcommand args.      Returns (subcommand, remainder, error_message)** (1 connections) — `server/commands/quest_commands.py`
- **Resolve player, player_id and QuestService from request and current_user.     Re** (1 connections) — `server/commands/quest_commands.py`
- **Return a single goal progress line for the quest log.** (1 connections) — `server/commands/quest_commands.py`
- *... and 9 more nodes in this community*

## Relationships

- [Server Config Loading](Server_Config_Loading.md) (16 shared connections)
- [Client Event Store](Client_Event_Store.md) (12 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (6 shared connections)
- [Quest Service Core](Quest_Service_Core.md) (3 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (1 shared connections)
- [Logging System Planning](Logging_System_Planning.md) (1 shared connections)
- [Chat Archive Advanced](Chat_Archive_Advanced.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`

## Audit Trail

- EXTRACTED: 175 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*