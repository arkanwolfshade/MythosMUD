# server game emote service emotedefinition

> 33 nodes

## Key Concepts

- **EmoteService** (20 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (16 connections) — `server/tests/unit/game/test_emote_service.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **EmoteDefinition** (6 connections) — `server/game/emote_service.py`
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **test_format_emote_messages_unknown_raises()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **test_emote_service_init_loads_via_mock()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_format_emote_messages()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_is_emote_alias_and_get_definition()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_list_available_emotes()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_reload_emotes_calls_load()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_validate_emote_payload_no_validator()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_validate_emote_payload_with_validator()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **Check if a command is an emote alias. Args: command: The command to check…** (1 connections) — `server/game/emote_service.py`
- **Get the emote definition for a command. Args: command: The command (emote name…** (1 connections) — `server/game/emote_service.py`
- **Format emote messages for the player and room occupants. Args: command: The…** (1 connections) — `server/game/emote_service.py`
- **Get a list of all available emotes and their aliases. Returns: Dict mapping…** (1 connections) — `server/game/emote_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server game emote service emoteloadresult](server_game_emote_service_emoteloadresult.md) (2 shared connections)
- [server command handler command input](server_command_handler_command_input.md) (2 shared connections)
- [server commands emote commands](server_commands_emote_commands.md) (2 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (2 shared connections)
- [chatresult](chatresult.md) (1 shared connections)
- [server game chat message chatmessage](server_game_chat_message_chatmessage.md) (1 shared connections)
- [schemas validator](schemas_validator.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`
- `server/tests/unit/game/test_emote_service.py`

## Audit Trail

- EXTRACTED: 59 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*