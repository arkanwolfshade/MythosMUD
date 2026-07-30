# PlayerIdCarrier

> 14 nodes

## Key Concepts

- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **._load_emotes()** (4 connections) — `server/game/emote_service.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **Service for managing predefined emote actions and their messages.** (1 connections) — `server/game/emote_service.py`
- **Initialize the EmoteService.          Args:             emote_file_path: DEPRECA** (1 connections) — `server/game/emote_service.py`
- **Load emote definitions from PostgreSQL database.** (1 connections) — `server/game/emote_service.py`
- **Check if a command is an emote alias.          Args:             command: The co** (1 connections) — `server/game/emote_service.py`
- **Get a list of all available emotes and their aliases.          Returns:** (1 connections) — `server/game/emote_service.py`
- **Reload emote definitions from the file.** (1 connections) — `server/game/emote_service.py`
- **Validate emote definitions against the shared schema when available.          Ar** (1 connections) — `server/game/emote_service.py`

## Relationships

- [AuthSlice](AuthSlice.md) (5 shared connections)
- [.get uuid mapping()](get_uuid_mapping%28%29.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [ChatMessage](ChatMessage.md) (2 shared connections)
- [rate overrides](rate_overrides.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`

## Audit Trail

- EXTRACTED: 41 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*