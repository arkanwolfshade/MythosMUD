# EmoteService

> 27 nodes

## Key Concepts

- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **EmoteDefinition** (5 connections) — `server/game/emote_service.py`
- **_EmoteLoadResult** (4 connections) — `server/game/emote_service.py`
- **._async_load_emotes()** (4 connections) — `server/game/emote_service.py`
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **_EmoteRowData** (3 connections) — `server/game/emote_service.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **TypedDict** (3 connections)
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **Async helper to load emotes from PostgreSQL database.** (1 connections) — `server/game/emote_service.py`
- **Check if a command is an emote alias. Args: command: The command to check…** (1 connections) — `server/game/emote_service.py`
- **Get the emote definition for a command. Args: command: The command (emote name…** (1 connections) — `server/game/emote_service.py`
- **Format emote messages for the player and room occupants. Args: command: The…** (1 connections) — `server/game/emote_service.py`
- **Get a list of all available emotes and their aliases. Returns: Dict mapping…** (1 connections) — `server/game/emote_service.py`
- **Reload emote definitions from the file.** (1 connections) — `server/game/emote_service.py`
- **Validate emote definitions against the shared schema when available. Args:…** (1 connections) — `server/game/emote_service.py`
- **Lazily instantiate and cache the emote schema validator.** (1 connections) — `server/game/emote_service.py`
- **Public emote payload returned by EmoteService lookups.** (1 connections) — `server/game/emote_service.py`
- **Service for managing predefined emote actions and their messages.** (1 connections) — `server/game/emote_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (6 shared connections)
- [SchemaValidator](SchemaValidator.md) (5 shared connections)
- [command_input.py](command_input.py.md) (2 shared connections)
- [handle_emote_command](handle_emote_command.md) (2 shared connections)
- [chat_message_senders.py](chat_message_senders.py.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`

## Audit Trail

- EXTRACTED: 44 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*