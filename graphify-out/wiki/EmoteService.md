# EmoteService

> 18 nodes · cohesion 0.13

## Key Concepts

- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **.format_emote_messages()** (5 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **Check if a command is an emote alias.          Args:             command: The co** (1 connections) — `server/game/emote_service.py`
- **Get the emote definition for a command.          Args:             command: The** (1 connections) — `server/game/emote_service.py`
- **Format emote messages for the player and room occupants.          Args:** (1 connections) — `server/game/emote_service.py`
- **Get a list of all available emotes and their aliases.          Returns:** (1 connections) — `server/game/emote_service.py`
- **Reload emote definitions from the file.** (1 connections) — `server/game/emote_service.py`
- **Validate emote definitions against the shared schema when available.          Ar** (1 connections) — `server/game/emote_service.py`
- **Service for managing predefined emote actions and their messages.** (1 connections) — `server/game/emote_service.py`
- **Initialize the EmoteService.          Args:             emote_file_path: DEPRECA** (1 connections) — `server/game/emote_service.py`
- **Load emote definitions from PostgreSQL database.** (1 connections) — `server/game/emote_service.py`

## Relationships

- [SchemaValidator](SchemaValidator.md) (4 shared connections)
- [command_input.py](command_input.py.md) (2 shared connections)
- [handle_emote_command](handle_emote_command.md) (2 shared connections)
- [chat_service.py](chat_service.py.md) (2 shared connections)
- [get_asyncpg_server_settings_for_database_url](get_asyncpg_server_settings_for_database_url.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*