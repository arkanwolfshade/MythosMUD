# .get room by id()

> 42 nodes

## Key Concepts

- **quest_commands.py** (38 connections) — `server/commands/quest_commands.py`
- **Any** (18 connections)
- **handle_journal_command()** (15 connections) — `server/commands/quest_commands.py`
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **_resolve_npc_in_player_room()** (7 connections) — `server/commands/quest_commands.py`
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **UUID** (6 connections)
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **_emit_npc_lines_for_results()** (6 connections) — `server/commands/quest_commands.py`
- **_quest_command_ready()** (6 connections) — `server/commands/quest_commands.py`
- **quest_ask_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **quest_turnin_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
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
- *... and 17 more nodes in this community*

## Relationships

- [ExitStack](ExitStack.md) (11 shared connections)
- [.initialize()](initialize%28%29.md) (11 shared connections)
- [look npc](look_npc.md) (9 shared connections)
- [QuestCompleted](QuestCompleted.md) (3 shared connections)
- [test magic commands](test_magic_commands.md) (2 shared connections)
- [DropResolved](DropResolved.md) (2 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (2 shared connections)
- [AuthSlice](AuthSlice.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [notify quest abandoned()](notify_quest_abandoned%28%29.md) (1 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/game/quest/quest_chat_notify.py`

## Audit Trail

- EXTRACTED: 196 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*