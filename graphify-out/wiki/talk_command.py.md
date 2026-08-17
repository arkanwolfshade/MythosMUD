# talk_command.py

> 30 nodes

## Key Concepts

- **talk_command.py** (28 connections) — `server/commands/talk_command.py`
- **test_talk_command.py** (15 connections) — `server/tests/unit/commands/test_talk_command.py`
- **handle_talk_command()** (13 connections) — `server/commands/talk_command.py`
- **DialoguePrompt** (12 connections) — `server/game/dialogue/dialogue_service.py`
- **_emit_prompt()** (10 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (9 connections) — `server/commands/talk_command.py`
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
- **talk / talk <n> command for NPC dialogue trees (#583).** (1 connections) — `server/commands/talk_command.py`
- **Handle talk <npc> or talk <n> against same-room NPCs.** (1 connections) — `server/commands/talk_command.py`
- **Extract player UUID from player model.** (1 connections) — `server/commands/talk_command.py`
- **Join talk args into a single remainder string.** (1 connections) — `server/commands/talk_command.py`
- *... and 5 more nodes in this community*

## Relationships

- [DialogueService](DialogueService.md) (12 shared connections)
- [communication_commands_flows.py](communication_commands_flows.py.md) (7 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [quest_commands.py](quest_commands.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [quest_chat_notify.py](quest_chat_notify.py.md) (2 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/talk_command.py`
- `server/game/dialogue/dialogue_service.py`
- `server/tests/unit/commands/test_talk_command.py`

## Audit Trail

- EXTRACTED: 89 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*