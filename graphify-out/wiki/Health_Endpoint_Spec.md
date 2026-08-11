# Health Endpoint Spec

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

- [Schemas Maps Map](Schemas_Maps_Map.md) (6 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (4 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (2 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (2 shared connections)
- [Chat Message Helpers](Chat_Message_Helpers.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Test Migration Report](Test_Migration_Report.md) (1 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`

## Audit Trail

- EXTRACTED: 74 (94%)
- INFERRED: 5 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*