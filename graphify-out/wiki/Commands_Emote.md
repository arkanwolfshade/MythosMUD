# Commands Emote

> 22 nodes · cohesion 0.12

## Key Concepts

- **handle_emote_command()** (14 connections) — `server/commands/emote_commands.py`
- **test_emote_commands.py** (5 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Any** (5 connections) — `server/commands/emote_commands.py`
- **_extract_emote_action()** (4 connections) — `server/commands/emote_commands.py`
- **_format_emote_messages()** (4 connections) — `server/commands/emote_commands.py`
- **_get_emote_services()** (4 connections) — `server/commands/emote_commands.py`
- **_handle_emote_result()** (4 connections) — `server/commands/emote_commands.py`
- **_validate_player_for_emote()** (4 connections) — `server/commands/emote_commands.py`
- **test_handle_emote_command()** (3 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_message()** (3 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Handle the result from chat service after sending emote.      Args:         resu** (1 connections) — `server/commands/emote_commands.py`
- **Handle the emote command for performing emotes.      Args:         command_data:** (1 connections) — `server/commands/emote_commands.py`
- **Extract action from command_data.      Args:         command_data: Command data** (1 connections) — `server/commands/emote_commands.py`
- **Get chat service and player service from app state.      Args:         request:** (1 connections) — `server/commands/emote_commands.py`
- **Validate player and extract required information for emote.      Args:         p** (1 connections) — `server/commands/emote_commands.py`
- **Format emote messages for predefined or custom emotes.      Args:         action** (1 connections) — `server/commands/emote_commands.py`
- **Unit tests for emote command handlers.  Tests the emote command functionality.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() processes emote.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() handles missing message.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() handles missing chat service.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **AliasStorage** (1 connections) — `server/commands/emote_commands.py`

## Relationships

- [[Alias Expansion Logic]] (7 shared connections)
- [[Chat Message Helpers]] (1 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/tests/unit/commands/test_emote_commands.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
