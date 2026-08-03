# commands quest rationale

> 107 nodes

## Key Concepts

- **quest_commands.py** (39 connections) — `server/commands/quest_commands.py`
- **handle_quest_command()** (20 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (20 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **Any** (18 connections)
- **_should_include_npc()** (14 connections) — `server/commands/look_npc.py`
- **handle_journal_command()** (14 connections) — `server/commands/quest_commands.py`
- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **resolve_npc_in_player_room()** (9 connections) — `server/commands/quest_commands.py`
- **_get_npcs_in_room()** (7 connections) — `server/commands/look_npc.py`
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
- *... and 82 more nodes in this community*

## Relationships

- [npc look commands](npc_look_commands.md) (23 shared connections)
- [quest chat game](quest_chat_game.md) (11 shared connections)
- [commands admin mute](commands_admin_mute.md) (7 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (5 shared connections)
- [quest game service](quest_game_service.md) (3 shared connections)
- [command factories create](command_factories_create.md) (3 shared connections)
- [look helpers commands](look_helpers_commands.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [quest service game](quest_service_game.md) (1 shared connections)
- [admin auth service](admin_auth_service.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/commands/quest_commands.py`
- `server/game/quest/quest_chat_notify.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`
- `server/tests/unit/commands/test_quest_commands.py`
- `server/tests/unit/game/test_chat_npc_system.py`

## Audit Trail

- EXTRACTED: 407 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*