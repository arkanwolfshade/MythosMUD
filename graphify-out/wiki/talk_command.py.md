# talk_command.py

> 36 nodes

## Key Concepts

- **talk_command.py** (28 connections) — `server/commands/talk_command.py`
- **test_talk_command.py** (15 connections) — `server/tests/unit/commands/test_talk_command.py`
- **handle_talk_command()** (13 connections) — `server/commands/talk_command.py`
- **_emit_prompt()** (10 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (9 connections) — `server/commands/talk_command.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **game/dialogue/__init__.py** (9 connections) — `server/game/dialogue/__init__.py`
- **_resolve_player_id()** (7 connections) — `server/commands/talk_command.py`
- **_talk_by_option_index()** (7 connections) — `server/commands/talk_command.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **_remainder_from_command_data()** (5 connections) — `server/commands/talk_command.py`
- **UUID** (5 connections)
- **test_talk_with_npc_success()** (4 connections) — `server/tests/unit/commands/test_talk_command.py`
- **asyncio** (4 connections)
- **test_emit_prompt_ended()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_emit_prompt_with_options()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_usage()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_talk_by_option_index_error_string()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_format_dialogue_prompt_numbers_options()** (3 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_remainder_from_command_data_list()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_remainder_from_command_data_string()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_resolve_player_id_invalid()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_resolve_player_id_uuid()** (2 connections) — `server/tests/unit/commands/test_talk_command.py`
- **talk / talk <n> command for NPC dialogue trees (#583).** (1 connections) — `server/commands/talk_command.py`
- *... and 11 more nodes in this community*

## Relationships

- [DialogueService](DialogueService.md) (16 shared connections)
- [communication_commands_flows.py](communication_commands_flows.py.md) (7 shared connections)
- [quest_commands.py](quest_commands.py.md) (5 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/talk_command.py`
- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/tests/unit/commands/test_talk_command.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 104 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*