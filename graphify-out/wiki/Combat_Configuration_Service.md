# Combat Configuration Service

> 27 nodes

## Key Concepts

- **UserManagerProtocol** (21 connections) — `server/game/chat_moderation.py`
- **Protocol** (2 connections)
- **.mute_channel()** (2 connections) — `server/game/chat_moderation.py`
- **.unmute_channel()** (2 connections) — `server/game/chat_moderation.py`
- **.is_channel_muted()** (2 connections) — `server/game/chat_moderation.py`
- **.mute_player()** (2 connections) — `server/game/chat_moderation.py`
- **.unmute_player()** (2 connections) — `server/game/chat_moderation.py`
- **.is_player_muted()** (2 connections) — `server/game/chat_moderation.py`
- **.is_globally_muted()** (2 connections) — `server/game/chat_moderation.py`
- **.is_admin()** (2 connections) — `server/game/chat_moderation.py`
- **.can_send_message()** (2 connections) — `server/game/chat_moderation.py`
- **.get_player_mutes()** (2 connections) — `server/game/chat_moderation.py`
- **.load_player_mutes()** (2 connections) — `server/game/chat_moderation.py`
- **.mute_global()** (1 connections) — `server/game/chat_moderation.py`
- **.unmute_global()** (1 connections) — `server/game/chat_moderation.py`
- **.add_admin()** (1 connections) — `server/game/chat_moderation.py`
- **.remove_admin()** (1 connections) — `server/game/chat_moderation.py`
- **Protocol for user manager.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a channel for a player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if channel is muted.** (1 connections) — `server/game/chat_moderation.py`
- **Mute a player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Unmute a player for another player.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player is muted.** (1 connections) — `server/game/chat_moderation.py`
- **Check if player is globally muted.** (1 connections) — `server/game/chat_moderation.py`
- *... and 2 more nodes in this community*

## Relationships

- [Chat Moderation Service](Chat_Moderation_Service.md) (5 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (1 shared connections)
- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (1 shared connections)

## Source Files

- `server/game/chat_moderation.py`

## Audit Trail

- EXTRACTED: 58 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*