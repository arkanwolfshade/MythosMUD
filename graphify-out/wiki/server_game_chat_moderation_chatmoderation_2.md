# server game chat moderation chatmoderation

> 13 nodes

## Key Concepts

- **Any** (8 connections)
- **PlayerServiceProtocol** (6 connections) — `server/game/chat_moderation.py`
- **.get_player_mutes()** (5 connections) — `server/game/chat_moderation.py`
- **.get_user_management_stats()** (3 connections) — `server/game/chat_moderation.py`
- **.get_player_by_id()** (3 connections) — `server/game/chat_moderation.py`
- **.resolve_player_name()** (3 connections) — `server/game/chat_moderation.py`
- **.get_player_mutes()** (2 connections) — `server/game/chat_moderation.py`
- **.get_system_stats()** (2 connections) — `server/game/chat_moderation.py`
- **Protocol** (2 connections)
- **Protocol for player service.** (1 connections) — `server/game/chat_moderation.py`
- **Resolve player name to player object.** (1 connections) — `server/game/chat_moderation.py`
- **Get all mutes applied by a player.** (1 connections) — `server/game/chat_moderation.py`
- **Get user management system statistics.** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [server game chat moderation chatmoderation](server_game_chat_moderation_chatmoderation.md) (7 shared connections)
- [server game chat moderation rationale](server_game_chat_moderation_rationale.md) (3 shared connections)
- [server game chat channel message](server_game_chat_channel_message.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*