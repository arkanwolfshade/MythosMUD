# server commands quest commands npc

> 30 nodes

## Key Concepts

- **talk_command.py** (28 connections) — `server/commands/talk_command.py`
- **test_talk_command.py** (15 connections) — `server/tests/unit/commands/test_talk_command.py`
- **handle_talk_command()** (13 connections) — `server/commands/talk_command.py`
- **_emit_prompt()** (10 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (9 connections) — `server/commands/talk_command.py`
- **npc_definition_id()** (7 connections) — `server/commands/quest_commands.py`
- **_resolve_player_id()** (7 connections) — `server/commands/talk_command.py`
- **_talk_by_option_index()** (7 connections) — `server/commands/talk_command.py`
- **_remainder_from_command_data()** (5 connections) — `server/commands/talk_command.py`
- **UUID** (5 connections)
- **test_talk_with_npc_success()** (4 connections) — `server/tests/unit/commands/test_talk_command.py`
- **asyncio** (4 connections)
- **test_emit_prompt_ended()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_emit_prompt_with_options()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_usage()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_talk_by_option_index_error_string()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_remainder_from_command_data_list()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_remainder_from_command_data_string()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_resolve_player_id_invalid()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_resolve_player_id_uuid()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **Return NPC definition id as string for quest offers/triggers.** (1 connections) — `server/commands/quest_commands.py`
- **talk / talk <n> command for NPC dialogue trees (#583).** (1 connections) — `server/commands/talk_command.py`
- **Handle talk <npc> or talk <n> against same-room NPCs.** (1 connections) — `server/commands/talk_command.py`
- **Extract player UUID from player model.** (1 connections) — `server/commands/talk_command.py`
- *... and 5 more nodes in this community*

## Relationships

- [server game dialogue dialogue service](server_game_dialogue_dialogue_service.md) (13 shared connections)
- [server commands communication commands flows](server_commands_communication_commands_flows.md) (7 shared connections)
- [server commands quest commands](server_commands_quest_commands.md) (6 shared connections)
- [server game chat npc system](server_game_chat_npc_system.md) (3 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/commands/talk_command.py`
- `server/tests/unit/commands/test_talk_command.py`

## Audit Trail

- EXTRACTED: 87 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*