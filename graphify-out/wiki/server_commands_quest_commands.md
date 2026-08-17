# server commands quest commands

> 42 nodes

## Key Concepts

- **quest_commands.py** (40 connections) — `server/commands/quest_commands.py`
- **Any** (18 connections)
- **handle_journal_command()** (14 connections) — `server/commands/quest_commands.py`
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **resolve_npc_in_player_room()** (9 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **_emit_npc_lines_for_results()** (6 connections) — `server/commands/quest_commands.py`
- **_quest_command_ready()** (6 connections) — `server/commands/quest_commands.py`
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **quest_ask_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **quest_turnin_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **UUID** (6 connections)
- **_format_one_quest_entry()** (5 connections) — `server/commands/quest_commands.py`
- **_format_quest_log()** (5 connections) — `server/commands/quest_commands.py`
- **_get_container_and_persistence()** (5 connections) — `server/commands/quest_commands.py`
- **_handle_quest_abandon()** (5 connections) — `server/commands/quest_commands.py`
- **test_emit_quest_npc_say_and_templates()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **_format_goal_line()** (4 connections) — `server/commands/quest_commands.py`
- **_format_quest_action_results()** (4 connections) — `server/commands/quest_commands.py`
- **_parse_quest_subcommand()** (4 connections) — `server/commands/quest_commands.py`
- **Quest commands: journal / quests (quest log), quest abandon/ask/turnin. Returns…** (1 connections) — `server/commands/quest_commands.py`
- **Return a single goal progress line for the quest log.** (1 connections) — `server/commands/quest_commands.py`
- **Return lines for a single quest log entry.** (1 connections) — `server/commands/quest_commands.py`
- *... and 17 more nodes in this community*

## Relationships

- [server game chat npc system](server_game_chat_npc_system.md) (11 shared connections)
- [exitstack](exitstack.md) (11 shared connections)
- [server commands quest commands npc](server_commands_quest_commands_npc.md) (6 shared connections)
- [server commands look npc](server_commands_look_npc.md) (5 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (4 shared connections)
- [server game quest quest service](server_game_quest_quest_service.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server commands look npc get](server_commands_look_npc_get.md) (2 shared connections)
- [server commands look npc rationale](server_commands_look_npc_rationale.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (1 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 124 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*