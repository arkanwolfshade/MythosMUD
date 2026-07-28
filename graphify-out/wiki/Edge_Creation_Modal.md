# Edge Creation Modal

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

- [Server Config Loading](Server_Config_Loading.md) (4 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (2 shared connections)
- [Commands Emote](Commands_Emote.md) (2 shared connections)
- [Chat Message Helpers](Chat_Message_Helpers.md) (2 shared connections)
- [Lucidity Rate Overrides](Lucidity_Rate_Overrides.md) (1 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (1 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*