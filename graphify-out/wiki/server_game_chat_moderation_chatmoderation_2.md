# server game chat moderation chatmoderation

> 20 nodes

## Key Concepts

- **Any** (8 connections)
- **PlayerServiceProtocol** (6 connections) — `server/game/chat_moderation.py`
- **._format_mute_entry()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_section()** (5 connections) — `server/game/chat_moderation.py`
- **._format_mute_duration()** (4 connections) — `server/game/chat_moderation.py`
- **.get_mute_status()** (4 connections) — `server/game/chat_moderation.py`
- **.get_user_management_stats()** (3 connections) — `server/game/chat_moderation.py`
- **.get_player_by_id()** (3 connections) — `server/game/chat_moderation.py`
- **.resolve_player_name()** (3 connections) — `server/game/chat_moderation.py`
- **.get_player_mutes()** (2 connections) — `server/game/chat_moderation.py`
- **.get_system_stats()** (2 connections) — `server/game/chat_moderation.py`
- **datetime** (2 connections)
- **Protocol** (2 connections)
- **Protocol for player service.** (1 connections) — `server/game/chat_moderation.py`
- **Resolve player name to player object.** (1 connections) — `server/game/chat_moderation.py`
- **Get user management system statistics.** (1 connections) — `server/game/chat_moderation.py`
- **Format mute duration text with remaining time or expiration status.** (1 connections) — `server/game/chat_moderation.py`
- **Format a single mute entry for display.** (1 connections) — `server/game/chat_moderation.py`
- **Format a section of mutes (personal or global) for display.** (1 connections) — `server/game/chat_moderation.py`
- **Get comprehensive mute status for a player. Args: player_id: Player ID to get…** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [server game chat moderation chatmoderation](server_game_chat_moderation_chatmoderation.md) (8 shared connections)
- [server game chat moderation rationale](server_game_chat_moderation_rationale.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [chatresult](chatresult.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*