# server commands emote commands

> 24 nodes

## Key Concepts

- **handle_emote_command()** (15 connections) — `server/commands/emote_commands.py`
- **emote_commands.py** (14 connections) — `server/commands/emote_commands.py`
- **test_emote_commands.py** (7 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **_get_emote_services()** (5 connections) — `server/commands/emote_commands.py`
- **Any** (5 connections)
- **_extract_emote_action()** (4 connections) — `server/commands/emote_commands.py`
- **_format_emote_messages()** (4 connections) — `server/commands/emote_commands.py`
- **_handle_emote_result()** (4 connections) — `server/commands/emote_commands.py`
- **_validate_player_for_emote()** (4 connections) — `server/commands/emote_commands.py`
- **test_handle_emote_command()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_chat_service()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_message()** (4 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **asyncio** (3 connections)
- **Emote command handlers for MythosMUD. This module contains handlers for the…** (1 connections) — `server/commands/emote_commands.py`
- **Handle the result from chat service after sending emote. Args: result: Result…** (1 connections) — `server/commands/emote_commands.py`
- **Handle the emote command for performing emotes. Args: command_data: Command…** (1 connections) — `server/commands/emote_commands.py`
- **Extract action from command_data. Args: command_data: Command data dictionary…** (1 connections) — `server/commands/emote_commands.py`
- **Get chat service and player service from app state. Args: request: FastAPI…** (1 connections) — `server/commands/emote_commands.py`
- **Validate player and extract required information for emote. Args:…** (1 connections) — `server/commands/emote_commands.py`
- **Format emote messages for predefined or custom emotes. Args: action: Emote…** (1 connections) — `server/commands/emote_commands.py`
- **Unit tests for emote command handlers. Tests the emote command functionality.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() processes emote.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() handles missing message.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() handles missing chat service.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`

## Relationships

- [server game emote service emotedefinition](server_game_emote_service_emotedefinition.md) (2 shared connections)
- [server commands utility commands](server_commands_utility_commands.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (1 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/tests/unit/commands/test_emote_commands.py`

## Audit Trail

- EXTRACTED: 48 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*