# handle_emote_command

> 26 nodes

## Key Concepts

- **handle_emote_command()** (16 connections) — `server/commands/emote_commands.py`
- **emote_commands.py** (13 connections) — `server/commands/emote_commands.py`
- **test_emote_commands.py** (8 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Any** (6 connections)
- **_get_emote_services()** (5 connections) — `server/commands/emote_commands.py`
- **_extract_emote_action()** (4 connections) — `server/commands/emote_commands.py`
- **_format_emote_messages()** (4 connections) — `server/commands/emote_commands.py`
- **_handle_emote_result()** (4 connections) — `server/commands/emote_commands.py`
- **_validate_player_for_emote()** (4 connections) — `server/commands/emote_commands.py`
- **test_handle_emote_command()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_message()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_predefined_emote()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **asyncio** (4 connections)
- **Emote command handlers for MythosMUD. This module contains handlers for the…** (1 connections) — `server/commands/emote_commands.py`
- **Handle the result from chat service after sending emote. Args: result: Result…** (1 connections) — `server/commands/emote_commands.py`
- **Handle the emote command for performing emotes. Args: command_data: Command…** (1 connections) — `server/commands/emote_commands.py`
- **Extract action from command_data. Args: command_data: Command data dictionary…** (1 connections) — `server/commands/emote_commands.py`
- **Get chat service, player service, and emote service from app state. Args:…** (1 connections) — `server/commands/emote_commands.py`
- **Validate player and extract required information for emote. Args:…** (1 connections) — `server/commands/emote_commands.py`
- **Format emote messages for predefined or custom emotes. Args: action: Emote…** (1 connections) — `server/commands/emote_commands.py`
- **Unit tests for emote command handlers. Tests the emote command functionality.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() processes emote.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() formats a predefined emote via the injected…** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() handles missing message.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- *... and 1 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (4 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/tests/unit/commands/test_emote_commands.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*