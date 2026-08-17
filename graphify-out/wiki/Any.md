# Any

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

- [ChatModeration](ChatModeration.md) (5 shared connections)
- [UserManagerProtocol](UserManagerProtocol.md) (3 shared connections)
- [._format_mute_entry](_format_mute_entry.md) (2 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*