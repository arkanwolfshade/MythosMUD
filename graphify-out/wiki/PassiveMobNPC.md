# PassiveMobNPC

> 46 nodes · cohesion 0.08

## Key Concepts

- **quest_commands.py** (42 connections) — `server/commands/quest_commands.py`
- **Any** (18 connections)
- **handle_journal_command()** (15 connections) — `server/commands/quest_commands.py`
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **resolve_npc_in_player_room()** (9 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **npc_definition_id()** (7 connections) — `server/commands/quest_commands.py`
- **_quest_command_ready()** (7 connections) — `server/commands/quest_commands.py`
- **emit_quest_npc_say()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **_emit_npc_lines_for_results()** (6 connections) — `server/commands/quest_commands.py`
- **_get_container_and_persistence()** (6 connections) — `server/commands/quest_commands.py`
- **UUID** (6 connections)
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **quest_ask_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **quest_turnin_npc_line()** (6 connections) — `server/game/quest/quest_chat_notify.py`
- **_format_one_quest_entry()** (5 connections) — `server/commands/quest_commands.py`
- **_format_quest_log()** (5 connections) — `server/commands/quest_commands.py`
- **_handle_quest_abandon()** (5 connections) — `server/commands/quest_commands.py`
- **test_emit_quest_npc_say_and_templates()** (5 connections) — `server/tests/unit/game/test_chat_npc_system.py`
- **_format_goal_line()** (4 connections) — `server/commands/quest_commands.py`
- **_format_quest_action_results()** (4 connections) — `server/commands/quest_commands.py`
- **_parse_quest_subcommand()** (4 connections) — `server/commands/quest_commands.py`
- **Quest commands: journal / quests (quest log), quest abandon/ask/turnin. Returns…** (1 connections) — `server/commands/quest_commands.py`
- *... and 21 more nodes in this community*

## Relationships

- [test_database_helpers.py](test_database_helpers.py.md) (11 shared connections)
- [handle_command](handle_command.md) (11 shared connections)
- [command_parser.py](command_parser.py.md) (9 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (5 shared connections)
- [Persistence Layer Refactoring - COMPLETE ✅](Persistence_Layer_Refactoring_-_COMPLETE_✅.md) (5 shared connections)
- [item_catalog_repository.py](item_catalog_repository.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (2 shared connections)
- [Commands](Commands.md) (2 shared connections)
- [.load_room_data](load_room_data.md) (2 shared connections)
- [properties](properties.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 135 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*