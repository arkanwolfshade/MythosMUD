# UserManagerProtocol

> 25 nodes

## Key Concepts

- **UserManagerProtocol** (20 connections) — `server/game/chat_moderation.py`
- **.can_send_message()** (2 connections) — `server/game/chat_moderation.py`
- **.is_admin()** (2 connections) — `server/game/chat_moderation.py`
- **.is_channel_muted()** (2 connections) — `server/game/chat_moderation.py`
- **.is_globally_muted()** (2 connections) — `server/game/chat_moderation.py`
- **.is_player_muted()** (2 connections) — `server/game/chat_moderation.py`
- **.mute_channel()** (2 connections) — `server/game/chat_moderation.py`
- **.mute_player()** (2 connections) — `server/game/chat_moderation.py`
- **.unmute_channel()** (2 connections) — `server/game/chat_moderation.py`
- **.unmute_player()** (2 connections) — `server/game/chat_moderation.py`
- **.add_admin()** (1 connections) — `server/game/chat_moderation.py`
- **.load_player_mutes()** (1 connections) — `server/game/chat_moderation.py`
- **.mute_global()** (1 connections) — `server/game/chat_moderation.py`
- **.remove_admin()** (1 connections) — `server/game/chat_moderation.py`
- **.unmute_global()** (1 connections) — `server/game/chat_moderation.py`
- **Protocol for user manager.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if channel is muted.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player is muted.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player is globally muted.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player is admin.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player can send message.** (1 connections) — `server/game/chat_moderation.py`

## Relationships

- [ChatModeration](ChatModeration.md) (4 shared connections)
- [chat_service.py](chat_service.py.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*