# commands quest rationale

> 83 nodes

## Key Concepts

- **quest_commands.py** (39 connections) — `server/commands/quest_commands.py`
- **handle_quest_command()** (20 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (20 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Any** (18 connections)
- **handle_journal_command()** (14 connections) — `server/commands/quest_commands.py`
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **resolve_npc_in_player_room()** (9 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **npc_definition_id()** (7 connections) — `server/commands/quest_commands.py`
- **emit_quest_npc_say()** (7 connections) — `server/game/quest/quest_chat_notify.py`
- **_enter_quest_command_patches()** (7 connections) — `server/tests/unit/commands/test_quest_commands.py`
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
- **ExitStack** (5 connections)
- **test_quest_ask_success()** (5 connections) — `server/tests/unit/commands/test_quest_commands.py`
- *... and 58 more nodes in this community*

## Relationships

- [npc look commands](npc_look_commands.md) (9 shared connections)
- [calendar models rationale](calendar_models_rationale.md) (6 shared connections)
- [dialogue service game](dialogue_service_game.md) (5 shared connections)
- [quest chat game](quest_chat_game.md) (5 shared connections)
- [commands whisper command](commands_whisper_command.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [quest game service](quest_game_service.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [quest service game](quest_service_game.md) (1 shared connections)
- [player preferences services](player_preferences_services.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/commands/test_quest_commands.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 336 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*