# EmoteService

> 42 nodes

## Key Concepts

- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **handle_emote_command()** (15 connections) — `server/commands/emote_commands.py`
- **emote_commands.py** (14 connections) — `server/commands/emote_commands.py`
- **test_emote_commands.py** (6 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **_get_emote_services()** (5 connections) — `server/commands/emote_commands.py`
- **Any** (5 connections)
- **_extract_emote_action()** (4 connections) — `server/commands/emote_commands.py`
- **_format_emote_messages()** (4 connections) — `server/commands/emote_commands.py`
- **_handle_emote_result()** (4 connections) — `server/commands/emote_commands.py`
- **_validate_player_for_emote()** (4 connections) — `server/commands/emote_commands.py`
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **test_handle_emote_command()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_message()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **asyncio** (3 connections)
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **Emote command handlers for MythosMUD. This module contains handlers for the…** (1 connections) — `server/commands/emote_commands.py`
- **Handle the result from chat service after sending emote. Args: result: Result…** (1 connections) — `server/commands/emote_commands.py`
- **Handle the emote command for performing emotes. Args: command_data: Command…** (1 connections) — `server/commands/emote_commands.py`
- *... and 17 more nodes in this community*

## Relationships

- [ScheduleEntry](ScheduleEntry.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [command_input.py](command_input.py.md) (2 shared connections)
- [chat_message_senders.py](chat_message_senders.py.md) (2 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/game/emote_service.py`
- `server/tests/unit/commands/test_emote_commands.py`

## Audit Trail

- EXTRACTED: 136 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*