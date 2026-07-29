# ExitStack

> 90 nodes

## Key Concepts

- **quest_commands.py** (38 connections) — `server/commands/quest_commands.py`
- **handle_quest_command()** (21 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (20 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Any** (18 connections)
- **handle_journal_command()** (15 connections) — `server/commands/quest_commands.py`
- **quest_chat_notify.py** (14 connections) — `server/game/quest/quest_chat_notify.py`
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **_resolve_npc_in_player_room()** (7 connections) — `server/commands/quest_commands.py`
- **_enter_quest_command_patches()** (7 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **title_from_quest_result()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **UUID** (6 connections)
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **_emit_npc_lines_for_results()** (6 connections) — `server/commands/quest_commands.py`
- **_quest_command_ready()** (6 connections) — `server/commands/quest_commands.py`
- **emit_quest_npc_say()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **quest_ask_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **quest_turnin_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **_get_container_and_persistence()** (5 connections) — `server/commands/quest_commands.py`
- **_format_one_quest_entry()** (5 connections) — `server/commands/quest_commands.py`
- **_format_quest_log()** (5 connections) — `server/commands/quest_commands.py`
- **_handle_quest_abandon()** (5 connections) — `server/commands/quest_commands.py`
- **ExitStack** (5 connections)
- *... and 65 more nodes in this community*

## Relationships

- [Any](Any.md) (10 shared connections)
- [look npc](look_npc.md) (9 shared connections)
- [.initialize()](initialize%28%29.md) (8 shared connections)
- [notify quest abandoned()](notify_quest_abandoned%28%29.md) (5 shared connections)
- [QuestCompleted](QuestCompleted.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (2 shared connections)
- [test quest service](test_quest_service.md) (1 shared connections)
- [collect inventory](collect_inventory.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/commands/test_quest_commands.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 358 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*