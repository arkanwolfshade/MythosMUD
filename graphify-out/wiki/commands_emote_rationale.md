# commands emote rationale

> 23 nodes

## Key Concepts

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
- **Unit tests for emote command handlers.  Tests the emote command functionality.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() processes emote.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() handles missing message.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`
- **Test handle_emote_command() handles missing chat service.** (1 connections) — `server/tests/unit/commands/test_emote_commands.py`

## Relationships

- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [schemas validator rationale](schemas_validator_rationale.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [commands who rationale](commands_who_rationale.md) (2 shared connections)
- [commands position system](commands_position_system.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (1 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)

## Source Files

- `server/commands/emote_commands.py`
- `server/tests/unit/commands/test_emote_commands.py`

## Audit Trail

- EXTRACTED: 79 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*