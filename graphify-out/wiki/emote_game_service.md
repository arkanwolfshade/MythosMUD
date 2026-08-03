# emote game service

> 27 nodes

## Key Concepts

- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **EmoteDefinition** (5 connections) — `server/game/emote_service.py`
- **.format_emote_messages()** (5 connections) — `server/game/emote_service.py`
- **_get_emote_validator()** (4 connections) — `server/game/emote_service.py`
- **_EmoteLoadResult** (4 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **._async_load_emotes()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **_EmoteRowData** (3 connections) — `server/game/emote_service.py`
- **TypedDict** (3 connections)
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **Lazily instantiate and cache the emote schema validator.** (1 connections) — `server/game/emote_service.py`
- **Public emote payload returned by EmoteService lookups.** (1 connections) — `server/game/emote_service.py`
- **Service for managing predefined emote actions and their messages.** (1 connections) — `server/game/emote_service.py`
- **Initialize the EmoteService.          Args:             emote_file_path: DEPRECA** (1 connections) — `server/game/emote_service.py`
- **Load emote definitions from PostgreSQL database.** (1 connections) — `server/game/emote_service.py`
- **Async helper to load emotes from PostgreSQL database.** (1 connections) — `server/game/emote_service.py`
- **Check if a command is an emote alias.          Args:             command: The co** (1 connections) — `server/game/emote_service.py`
- **Get the emote definition for a command.          Args:             command: The** (1 connections) — `server/game/emote_service.py`
- **Format emote messages for the player and room occupants.          Args:** (1 connections) — `server/game/emote_service.py`
- **Get a list of all available emotes and their aliases.          Returns:** (1 connections) — `server/game/emote_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (6 shared connections)
- [schemas validator rationale](schemas_validator_rationale.md) (5 shared connections)
- [command input commands](command_input_commands.md) (2 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (2 shared connections)
- [chat game message](chat_game_message.md) (2 shared connections)
- [database config helpers](database_config_helpers.md) (1 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`

## Audit Trail

- EXTRACTED: 74 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*