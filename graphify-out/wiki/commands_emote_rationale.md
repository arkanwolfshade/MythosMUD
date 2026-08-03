# commands emote rationale

> 25 nodes

## Key Concepts

- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **emote_commands.py** (14 connections) — `server/commands/emote_commands.py`
- **handle_emote_command()** (14 connections) — `server/commands/emote_commands.py`
- **_get_emote_services()** (7 connections) — `server/commands/emote_commands.py`
- **test_emote_commands.py** (6 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Any** (5 connections)
- **_extract_emote_action()** (4 connections) — `server/commands/emote_commands.py`
- **_validate_player_for_emote()** (4 connections) — `server/commands/emote_commands.py`
- **_format_emote_messages()** (4 connections) — `server/commands/emote_commands.py`
- **_handle_emote_result()** (4 connections) — `server/commands/emote_commands.py`
- **test_handle_emote_command()** (3 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_message()** (3 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **test_handle_emote_command_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Emote command handlers for MythosMUD.  This module contains handlers for the emo** (1 connections) — `server/commands/emote_commands.py`
- **Extract action from command_data.      Args:         command_data: Command data** (1 connections) — `server/commands/emote_commands.py`
- **Get chat service and player service from app state.      Args:         request:** (1 connections) — `server/commands/emote_commands.py`
- **Validate player and extract required information for emote.      Args:         p** (1 connections) — `server/commands/emote_commands.py`
- **Format emote messages for predefined or custom emotes.      Args:         action** (1 connections) — `server/commands/emote_commands.py`
- **Handle the result from chat service after sending emote.      Args:         resu** (1 connections) — `server/commands/emote_commands.py`
- **Handle the emote command for performing emotes.      Args:         command_data:** (1 connections) — `server/commands/emote_commands.py`
- **Utility commands for MythosMUD.  This module contains handlers for utility comma** (1 connections) — `server/commands/utility_commands.py`
- **Unit tests for emote command handlers.  Tests the emote command functionality.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() processes emote.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() handles missing message.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() handles missing chat service.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`

## Relationships

- [commands admin mute](commands_admin_mute.md) (8 shared connections)
- [commands logout rationale](commands_logout_rationale.md) (3 shared connections)
- [commands status rationale](commands_status_rationale.md) (3 shared connections)
- [commands who rationale](commands_who_rationale.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [player respawn event](player_respawn_event.md) (2 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)
- [commands time handle](commands_time_handle.md) (1 shared connections)
- [logout command commands](logout_command_commands.md) (1 shared connections)
- [commands whoami utility](commands_whoami_utility.md) (1 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/commands/utility_commands.py`
- `server/tests/unit/commands/test_emote_commands.py`

## Audit Trail

- EXTRACTED: 100 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*