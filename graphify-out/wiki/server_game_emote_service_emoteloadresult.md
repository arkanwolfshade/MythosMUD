# server game emote service emoteloadresult

> 5 nodes

## Key Concepts

- **._async_load_emotes()** (4 connections) — `server/game/emote_service.py`
- **_EmoteLoadResult** (3 connections) — `server/game/emote_service.py`
- **TypedDict** (3 connections)
- **_EmoteRowData** (2 connections) — `server/game/emote_service.py`
- **Async helper to load emotes from PostgreSQL database.** (1 connections) — `server/game/emote_service.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server game emote service emotedefinition](server_game_emote_service_emotedefinition.md) (2 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (1 shared connections)

## Source Files

- `server/game/emote_service.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*