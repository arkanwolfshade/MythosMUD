# talk_command.py

> 59 nodes

## Key Concepts

- **talk_command.py** (30 connections) — `server/commands/talk_command.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **handle_talk_command()** (14 connections) — `server/commands/talk_command.py`
- **test_talk_command.py** (14 connections) — `server/tests/unit/commands/test_talk_command.py`
- **DialoguePrompt** (12 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (12 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **_emit_prompt()** (10 connections) — `server/commands/talk_command.py`
- **resolve_npc_in_player_room()** (9 connections) — `server/commands/quest_commands.py`
- **_talk_with_npc()** (9 connections) — `server/commands/talk_command.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **game/dialogue/__init__.py** (9 connections) — `server/game/dialogue/__init__.py`
- **npc_definition_id()** (7 connections) — `server/commands/quest_commands.py`
- **_resolve_player_id()** (7 connections) — `server/commands/talk_command.py`
- **_talk_by_option_index()** (7 connections) — `server/commands/talk_command.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **_remainder_from_command_data()** (5 connections) — `server/commands/talk_command.py`
- **test_dialogue_service_start_and_choose()** (5 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **UUID** (5 connections)
- **test_talk_with_npc_success()** (4 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_dialogue_service_choose_without_cursor()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **asyncio** (4 connections)
- **test_emit_prompt_ended()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_emit_prompt_with_options()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_handle_talk_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_talk_command.py`
- *... and 34 more nodes in this community*

## Relationships

- [DialogueService](DialogueService.md) (12 shared connections)
- [get_username_from_user](get_username_from_user.md) (8 shared connections)
- [communication_commands_flows.py](communication_commands_flows.py.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (3 shared connections)
- [go_command.py](go_command.py.md) (3 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (3 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (2 shared connections)
- [MessageCategory](MessageCategory.md) (2 shared connections)
- [command_error](command_error.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/commands/talk_command.py`
- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/tests/unit/commands/test_talk_command.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 153 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*