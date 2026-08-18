# server game chat moderation chatmoderation

> 9 nodes

## Key Concepts

- **._format_mute_entry()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_section()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_duration()** (4 connections) — `server/game/chat_moderation.py`
- **.get_mute_status()** (4 connections) — `server/game/chat_moderation.py`
- **datetime** (2 connections)
- **Format mute duration text with remaining time or expiration status.** (1 connections) — `server/game/chat_moderation.py`
- **Format a single mute entry for display.** (1 connections) — `server/game/chat_moderation.py`
- **Format a section of mutes (personal or global) for display.** (1 connections) — `server/game/chat_moderation.py`
- **Get comprehensive mute status for a player. Args: player_id: Player ID to get…** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [server game chat moderation chatmoderation](server_game_chat_moderation_chatmoderation.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*